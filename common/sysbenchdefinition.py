import os
from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d")

def getCurrentTime():
    current_time = datetime.now()
    formatted_time = current_time.strftime("time-%Y-%m-%d-%H-%M")
    return formatted_time

def generate_pod_yaml(type, read_write_pct_name_suffix, threads_name_suffix, sysbench_value):
    return f"""
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  name: test-{type}-run-{read_write_pct_name_suffix}-{threads_name_suffix}-{getCurrentTime()}
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

def sysbench_mysql_yaml(times, threads, read_pct):
    times_param = "times:%s" % times
    threads_param = "threads:%s" % threads
    read_write_pct_param = "--read-percent=%s --write-percent=%s" % (read_pct, 100-read_pct)
    read_write_pct_name_suffix = "%s-%s" % (read_pct, 100-read_pct)
    threads_name_suffix = "%s" % threads
    return generate_pod_yaml("mysql", read_write_pct_name_suffix, threads_name_suffix, f"mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,{times_param},type:oltp_read_write_pct,{threads_param},others:{read_write_pct_param} --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable")

def sysbench_vtgate_yaml(times, threads, read_pct):
    times_param = "times:%s" % times
    threads_param = "threads:%s" % threads
    read_write_pct_param = "--read-percent=%s --write-percent=%s" % (read_pct, 100-read_pct)
    read_write_pct_name_suffix = "%s-%s" % (read_pct, 100-read_pct)
    threads_name_suffix = "%s" % threads
    return generate_pod_yaml("vtgate", read_write_pct_name_suffix, threads_name_suffix, f"mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,{times_param},type:oltp_read_write_pct,{threads_param},others:{read_write_pct_param} --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable")

#################################################################################

print(getCurrentTime())