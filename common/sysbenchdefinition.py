import os

def generate_pod_yaml(type, read_write_pct_name_suffix, threads_name_suffix, sysbench_value):
    return f"""
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-{type}-run-{read_write_pct_name_suffix}-{threads_name_suffix}
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

def generate_mysql_pod_yaml_by_times_threads(times, threads, read_pct):
    times_param = "times:%s" % times
    threads_param = "threads:%s" % threads
    read_write_pct_param = "--read-percent=%s --write-percent=%s" % (read_pct, 100-read_pct)
    read_write_pct_name_suffix = "%s-%s" % (read_pct, 100-read_pct)
    threads_name_suffix = "%s" % threads
    return generate_pod_yaml("mysql", read_write_pct_name_suffix, threads_name_suffix, f"mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,{times},type:oltp_read_write_pct,{threads},others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable")

def generate_vtgate_pod_yaml_by_times_threads(times, threads, read_pct):
    times_param = "times:%s" % times
    threads_param = "threads:%s" % threads
    read_write_pct_param = "--read-percent=%s --write-percent=%s" % (read_pct, 100-read_pct)
    read_write_pct_name_suffix = "%s-%s" % (read_pct, 100-read_pct)
    threads_name_suffix = "%s" % threads
    return generate_pod_yaml("vtgate", read_write_pct_name_suffix, threads_name_suffix, f"mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,{times},type:oltp_read_write_pct,{threads},others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable")

#################################################################################

# sysbench_mysql_yaml(times=60, threads=4, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=8, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=16, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=25, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=50, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=75, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=100, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=125, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=150, read_pct=20)
# sysbench_mysql_yaml(times=60, threads=175, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=4, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=8, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=16, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=25, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=50, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=75, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=100, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=125, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=150, read_pct=20)
# sysbench_vtgate_yaml(times=60, threads=175, read_pct=20)

print(sysbench_vtgate_yaml(times=60, threads=175, read_pct=20))