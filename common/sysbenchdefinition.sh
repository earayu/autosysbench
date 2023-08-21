function sysbench_mysql_times_60_threads_4 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:4"
}

function sysbench_mysql_times_60_threads_8 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:8"
}

function sysbench_mysql_times_60_threads_16 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:16"
}

function sysbench_mysql_times_60_threads_25 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:25"
}

function sysbench_mysql_times_60_threads_50 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:50"
}

function sysbench_mysql_times_60_threads_75 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:75"
}

function sysbench_mysql_times_60_threads_100 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:100"
}

function sysbench_mysql_times_60_threads_125 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:125"
}

function sysbench_mysql_times_60_threads_150 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:150"
}

function sysbench_mysql_times_60_threads_175 {
  generate_mysql_pod_yaml_by_times_threads "times:60" "threads:175"
}









function sysbench_vtgate_times_60_threads_4 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:4"
}

function sysbench_vtgate_times_60_threads_8 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:8"
}

function sysbench_vtgate_times_60_threads_16 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:16"
}

function sysbench_vtgate_times_60_threads_25 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:25"
}

function sysbench_vtgate_times_60_threads_50 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:50"
}

function sysbench_vtgate_times_60_threads_75 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:75"
}

function sysbench_vtgate_times_60_threads_100 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:100"
}

function sysbench_vtgate_times_60_threads_125 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:125"
}

function sysbench_vtgate_times_60_threads_150 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:150"
}

function sysbench_vtgate_times_60_threads_175 {
  generate_vtgate_pod_yaml_by_times_threads "times:60" "threads:175"
}





#################################################################################################################################################


function generate_mysql_pod_yaml_by_times_threads {
  # times:60
  local times=$1
  # threads:4 8 16 25 50 75 100 125 150 175
  local threads=$2
  generate_pod_yaml "mysql" "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,$times,type:oltp_read_write_pct,$threads,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
}

function generate_vtgate_pod_yaml_by_times_threads {
   # times:60
  local times=$1
  # threads:4 8 16 25 50 75 100 125 150 175
  local threads=$2
  generate_pod_yaml "vtgate" "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,$times,type:oltp_read_write_pct,$threads,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
}


#################################################################################################################################################


function generate_pod_yaml {
  local type=$1
  local sysbench_value=$2

  cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-$type-run-
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
          value: "$sysbench_value"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF

}

