import csv
import os
import subprocess
import time
import threading
from config import RestSeconds
from datetime import datetime


def create_and_wait_for_pod(pod_yaml, pod_run_time, data_path, enable_monitor=True):
    createPodCmd = f"""
kubectl create -f - <<EOF
{pod_yaml}
EOF
"""
    pod_name = subprocess.check_output(createPodCmd, shell=True).decode().strip().split()[0]
    pod_data_path = os.path.join(data_path, pod_name)
    os.makedirs(pod_data_path, exist_ok=True)

    if enable_monitor:
        t1 = threading.Thread(target=create_minotor_process, args=(pod_data_path, pod_run_time))
        t1.start()

    waitPodCmd = f'kubectl wait --for=jsonpath="{{.status.phase}}"=Succeeded --timeout=15m {pod_name}'
    print(waitPodCmd)
    waitPodResult = subprocess.check_output(waitPodCmd, shell=True).decode().strip()
    print(waitPodResult)

    # save sysbench log
    get_pod_log(pod_data_path, pod_name)
    return pod_name


def create_minotor_process(pod_data_path, run_time: int):
    def save_to_csv(container_data, key, output_dir):
        filename = os.path.join(output_dir, f"{key}.csv")
        if not os.path.exists(filename):
            with open(filename, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(["timeStamp", "POD", "NAME", "CPU(cores)", "MEMORY(bytes)"])
        with open(filename, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(container_data)

    def fetch_data():
        cmd = ["kubectl", "top", "pod", "--containers"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        lines = result.stdout.split("\n")
        timestamp = datetime.now().strftime('%H:%M:%S')
        return timestamp, lines[1:-1]

    def parse_data(timestamp, lines):
        monitor_containers = ["mysql", "vttablet", "etcd", "vtconsensus", "vtgate"]
        data_dict = {}
        for line in lines:
            parts = line.split()
            pod_name, container_name, cpu, memory = parts[0], parts[1], parts[2], parts[3]
            if container_name not in monitor_containers:
                continue
            key = f"monitor-{pod_name}-{container_name}"
            if key not in data_dict:
                data_dict[key] = []
            data_dict[key].append([timestamp, pod_name, container_name, cpu, memory])
        return data_dict

    time.sleep(30)
    print("--------------- begin monitor ---------------")
    end_time = time.time() + run_time-30-10
    try:
        while time.time() < end_time:
            timestamp, lines = fetch_data()
            data_dict = parse_data(timestamp, lines)
            for key, container_data in data_dict.items():
                save_to_csv(container_data, key, pod_data_path)
                # print(f"Data for {key} saved to {key}.csv in {data_path}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    print("--------------- end monitor ---------------")


def get_all_pod_logs(dest_path):
    pods = subprocess.check_output("kubectl get pods --no-headers | awk '/^test-/ {print $1}'",
                                   shell=True).decode().splitlines()
    for pod_name in pods:
        if pod_name.startswith("test-mysql"):
            file_name = "mysql_qps_latency.txt"
        elif pod_name.startswith("test-vtgate"):
            file_name = "vtgate_qps_latency.txt"
        else:
            raise Exception('unexpected pod_name:{}'.format(pod_name))
        with open(f"{dest_path}/{file_name}", "w") as log_file:
            log_file.write(subprocess.check_output(f"kubectl logs {pod_name}", shell=True).decode())


def get_pod_log(dest_path, pod_name):
    if pod_name.startswith("pod/"):
        pod_name = pod_name.replace("pod/", "")
    if pod_name.startswith("test-mysql"):
        file_name = "mysql_qps_latency.txt"
    elif pod_name.startswith("test-vtgate"):
        file_name = "vtgate_qps_latency.txt"
    else:
        raise Exception('unexpected pod_name:{}'.format(pod_name))
    with open(f"{dest_path}/{file_name}", "w") as log_file:
        log_file.write(subprocess.check_output(f"kubectl logs {pod_name}", shell=True).decode())


def delete_sysbench_pods():
    subprocess.run("kubectl delete pod --field-selector=status.phase==Succeeded", shell=True)


def rest():
    print("current time: " + time.ctime())
    time.sleep(RestSeconds)
    print("current time: " + time.ctime())


IsFirstWorkload = True
DryRun = False


def sysbench_run_and_rest(pod_yaml, pod_run_time, data_path, enable_monitor=True):
    global DryRun
    if DryRun:
        return
    global IsFirstWorkload
    if not IsFirstWorkload:
        rest()
    IsFirstWorkload = False
    create_and_wait_for_pod(pod_yaml, pod_run_time, data_path, enable_monitor)


import pandas as pd


def transform_qps_latency_result(sysparser_binary, path):
    if not os.path.isdir(path):
        print("Path does not exist")
        exit(1)

    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "mysql_qps_latency.txt" or file == "vtgate_qps_latency.txt":
                filepath = os.path.join(root, file)
                filename = os.path.basename(filepath).replace('.txt', '')
                subprocess.run(f'{sysparser_binary} --file="{filepath}" > {os.path.join(root, filename)}.csv',
                               shell=True)
                print(f"Processing completed: {filepath}")


def aggregate_result(path):
    mysql_data = []
    vtgate_data = []
    # path = os.path.join(path, "pod")
    for root, dirs, files in os.walk(path):
        for file in files:
            full_file_name = os.path.join(root, file)
            df = pd.read_csv(full_file_name, sep="\t")
            if file == "mysql_qps_latency.csv":
                mysql_data.append(df)
            elif file == "vtgate_qps_latency.csv":
                vtgate_data.append(df)
            else:
                pass

    mysql_data = pd.concat(mysql_data).sort_values(by="Threads")
    vtgate_data = pd.concat(vtgate_data).sort_values(by="Threads")

    mysql_data.to_csv(os.path.join(path, "aggregated_mysql_qps_latency.csv"), index=False, sep="\t")
    vtgate_data.to_csv(os.path.join(path, "aggregated_vtgate_qps_latency.csv"), index=False, sep="\t")
