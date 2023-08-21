#!/bin/bash

create_and_wait_for_pod() {
  local script="$1"
  echo "Creating pod using script:"
  echo "$script"
  pod_name=$(echo "$script" | kubectl create -f - | awk '{print $1}')
  echo "Waiting for pod $pod_name to complete..."
  kubectl wait --for=jsonpath='{.status.phase}'=Succeeded --timeout=15m "$pod_name"
  echo "Pod $pod_name completed."
}

getPodLogs() {
  destPath="$1"
  pods=$(kubectl get pods --no-headers | awk '/^test-/ {print $1}')

  for podName in $pods; do
    kubectl logs "$podName" > "${destPath}/${podName}.txt"
  done
}

deleteSysbenchPods() {
  kubectl delete pod --field-selector=status.phase==Succeeded
}

transform() {
  sysparser_binary=$1
  path=$2

  # Check if the given path exists
  if [ ! -d "$path" ]; then
    echo "Path does not exist"
    exit 1
  fi

  # Iterate through all txt files in the path
  for file in "$path"/*.txt; do
    # Check if the txt file exists
    if [ -e "$file" ]; then
      # Get the file name (without path and extension)
      filename=$(basename "$file" .txt)
      # Call the program to process the txt file and output to a csv file
      # /Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser --file="$file" > "$path/$filename.csv"
      $sysparser_binary --file="$file" > "$path/$filename.csv"
      echo "Processing completed: $file"
    fi
  done
}


rest(){
  date
  sleep $1
  date
}



sysbench_vtgate_4_8_16_25_50_75_100_125_150_175=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
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
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:4 8 16 25 50 75 100 125 150 175,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_4_8_16_25_50_75_100_125_150_175=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
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
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:4 8 16 25 50 75 100 125 150 175,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_vtgate_175=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-vtgate-run-
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
          value: "mode:run,driver:mysql,host:172.16.251.240,user:root,port:15306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:175,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

sysbench_mysql_175=$(cat <<EOF
apiVersion: v1
kind: Pod
metadata:
  namespace: default
  generateName: test-mysql-run-
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
          value: "mode:run,driver:mysql,host:172.16.134.200,user:root,password:sf2gxx9r,port:3306,db:mydb,size:2000000,tables:50,times:60,type:oltp_read_write_pct,threads:175,others:--read-percent=80 --write-percent=20 --skip_trx=on --mysql-ignore-errors=1062 --db-ps-mode=disable"
  restartPolicy: Never
  tolerations:
    - key: kb-vtgate
      operator: Equal
      value: "true"
      effect: NoSchedule
EOF
)

#######################################################################################################################################


sysbench_mysql_then_vtgate() {
  local iterations=$1

  for ((i=1; i<=iterations; i++)); do
    create_and_wait_for_pod "$sysbench_mysql_175"
    rest 60
    create_and_wait_for_pod "$sysbench_vtgate_175"
    if [ $i -ne $iterations ]; then
      rest 60
    fi
  done
}

sysbench_vtgate_then_mysql() {
  local iterations=$1

  for ((i=1; i<=iterations; i++)); do
    create_and_wait_for_pod "$sysbench_vtgate_175"
    rest 60
    create_and_wait_for_pod "$sysbench_mysql_175"
    if [ $i -ne $iterations ]; then
      rest 60
    fi
  done
}



#######################################################################################################################################

test_result_path=/Users/earayu/Desktop/tmp/sysbench9
mkdir $test_result_path
deleteSysbenchPods


sysbench_vtgate_then_mysql 5


getPodLogs $test_result_path
transform /Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser $test_result_path




