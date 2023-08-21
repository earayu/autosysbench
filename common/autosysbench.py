import os
import subprocess
import time
import glob

auto_sysbench_sh_path = os.path.dirname(os.path.realpath(__file__))
exec(open(f"{auto_sysbench_sh_path}/sysbenchdefinition.sh").read())

def create_and_wait_for_pod(script):
    print("Creating pod using script:")
    print(script)
    pod_name = subprocess.check_output(f'echo "{script}" | kubectl create -f -', shell=True).decode().split()[0]
    print(f"Waiting for pod {pod_name} to complete...")
    subprocess.run(f'kubectl wait --for=jsonpath="{{.status.phase}}"=Succeeded --timeout=15m {pod_name}', shell=True)
    print(f"Pod {pod_name} completed.")

def getPodLogs(destPath):
    pods = subprocess.check_output('kubectl get pods --no-headers', shell=True).decode().split('\n')
    pods = [pod.split()[0] for pod in pods if pod.startswith('test-')]

    for podName in pods:
        subprocess.run(f'kubectl logs {podName} > {destPath}/{podName}.txt', shell=True)

def deleteSysbenchPods():
    subprocess.run('kubectl delete pod --field-selector=status.phase==Succeeded', shell=True)

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
    print(time.ctime())
    time.sleep(seconds)
    print(time.ctime())

def sysbench_mysql_then_vtgate_175_threads_loop(iterations):
    for i in range(iterations):
        create_and_wait_for_pod(sysbench_mysql_175)
        rest(60)
        create_and_wait_for_pod(sysbench_vtgate_175)
        if i != iterations - 1:
            rest(60)

def sysbench_vtgate_then_mysql_175_threads_loop(iterations):
    for i in range(iterations):
        create_and_wait_for_pod(sysbench_vtgate_175)
        rest(60)
        create_and_wait_for_pod(sysbench_mysql_175)
        if i != iterations - 1:
            rest(60)

def sysbench_run_and_rest(script):
    create_and_wait_for_pod(script)
    # rest(60)