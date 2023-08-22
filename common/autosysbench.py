import os
import subprocess
import time
import glob

def create_and_wait_for_pod(script):
    createPodCmd = f"""
kubectl create -f - <<EOF
{script}
EOF
"""
    print(createPodCmd)
    pod_name = subprocess.check_output(createPodCmd, shell=True).decode().strip().split()[0]
    print("pod name: " + pod_name)
    
    waitPodCmd = f'kubectl wait --for=jsonpath="{{.status.phase}}"=Succeeded --timeout=15m {pod_name}'
    print(waitPodCmd)
    waitPodResult = subprocess.check_output(waitPodCmd, shell=True)
    print(waitPodResult)
    return pod_name


def get_all_pod_logs(dest_path):
    pods = subprocess.check_output("kubectl get pods --no-headers | awk '/^test-/ {print $1}'", shell=True).decode().splitlines()
    for pod_name in pods:
        with open(f"{dest_path}/{pod_name}.txt", "w") as log_file:
            log_file.write(subprocess.check_output(f"kubectl logs {pod_name}", shell=True).decode())

def get_pod_log(dest_path, pod_name):
    if pod_name.startswith("pod/"):
        pod_name = pod_name.replace("pod/", "")
    with open(f"{dest_path}/{pod_name}.txt", "w") as log_file:
        log_file.write(subprocess.check_output(f"kubectl logs {pod_name}", shell=True).decode())


def delete_sysbench_pods():
    subprocess.run("kubectl delete pod --field-selector=status.phase==Succeeded", shell=True)

def transform(sysparser_binary, path):
    if not os.path.isdir(path):
        print("Path does not exist")
        exit(1)

    for file in glob.glob(f"{path}/*.txt"):
        if os.path.exists(file):
            filename = os.path.basename(file).replace('.txt', '')
            subprocess.run(f'{sysparser_binary} --file="{file}" > {path}/{filename}.csv', shell=True)
            print(f"Processing completed: {file}")



def rest(seconds):
    print("current time: " + time.ctime())
    time.sleep(seconds)
    print("current time: " + time.ctime())

IsFirstWorkload = True


def sysbench_run_and_rest(script):
    global IsFirstWorkload
    if not IsFirstWorkload:
        rest(60)
        IsFirstWorkload = False
    pod_name = create_and_wait_for_pod(script)
    return pod_name


import pandas as pd
from pathlib import Path

def aggregate_result(path):
    mysql_data = []
    vtgate_data = []

    for file in Path(path).glob("test-*.csv"):
        df = pd.read_csv(file, sep="\t")
        if "mysql" in file.name:
            mysql_data.append(df)
        elif "vtgate" in file.name:
            vtgate_data.append(df)

    mysql_data = pd.concat(mysql_data).sort_values(by="Threads")
    vtgate_data = pd.concat(vtgate_data).sort_values(by="Threads")

    mysql_data.to_csv(os.path.join(path, "mysql.csv"), index=False, sep="\t")
    vtgate_data.to_csv(os.path.join(path, "vtgate.csv"), index=False, sep="\t")
