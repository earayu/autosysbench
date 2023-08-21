import os

def generate_pod_yaml(type, sysbench_value):
    return f"""
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-{type}-run-
spec:
  containers:
    - name: test-sysbench
      image: registry.cn-hangzhou.aliyuncs.com/apecloud/customsuites:latest
      env:
        - name: TYPE
          value: "2"
        - name: FLAG
          value: "0"
        - name: CONFIGS
          value: "{sysbench_value}"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
"""

#################################################################################

def generate_mysql_pod_yaml_by_times_threads(times, threads):
    return generate_pod_yaml("mysql", f"mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,{times},type:oltp_read_write_pct,{threads},others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable")

def generate_vtgate_pod_yaml_by_times_threads(times, threads):
    return generate_pod_yaml("vtgate", f"mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,{times},type:oltp_read_write_pct,{threads},others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable")

#################################################################################

def sysbench_mysql_times_60_threads_4():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:4")
def sysbench_mysql_times_60_threads_8():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:8")
def sysbench_mysql_times_60_threads_16():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:16")
def sysbench_mysql_times_60_threads_25():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:25")
def sysbench_mysql_times_60_threads_50():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:50")
def sysbench_mysql_times_60_threads_75():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:75")
def sysbench_mysql_times_60_threads_100():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:100")
def sysbench_mysql_times_60_threads_125():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:125")
def sysbench_mysql_times_60_threads_150():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:150")
def sysbench_mysql_times_60_threads_175():
    return generate_mysql_pod_yaml_by_times_threads("times:60", "threads:175")


def sysbench_vtgate_times_60_threads_4():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:4")
def sysbench_vtgate_times_60_threads_8():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:8")
def sysbench_vtgate_times_60_threads_16():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:16")
def sysbench_vtgate_times_60_threads_25():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:25")
def sysbench_vtgate_times_60_threads_50():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:50")
def sysbench_vtgate_times_60_threads_75():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:75")
def sysbench_vtgate_times_60_threads_100():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:100")
def sysbench_vtgate_times_60_threads_125():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:125")
def sysbench_vtgate_times_60_threads_150():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:150")
def sysbench_vtgate_times_60_threads_175():
    return generate_vtgate_pod_yaml_by_times_threads("times:60", "threads:175")