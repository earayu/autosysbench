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

#######################################################################################################################################

source sysbenchdefinition.sh

#######################################################################################################################################


sysbench_mysql_then_vtgate_175_threads_loop() {
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

sysbench_vtgate_then_mysql_175_threads_loop() {
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

sysbench_run_and_rest() {
  local podDefinition=$1
  create_and_wait_for_pod $podDefinition
  rest 60
}


#######################################################################################################################################

main() {
  test_result_path="$(pwd)/data/sysbench1"
  mkdir $test_result_path
  deleteSysbenchPods

  # sysbench_vtgate_then_mysql_175_threads_loop 5

  sysbench_run_and_rest sysbench_vtgate_4
  sysbench_run_and_rest sysbench_vtgate_8
  sysbench_run_and_rest sysbench_vtgate_16
  sysbench_run_and_rest sysbench_vtgate_25
  sysbench_run_and_rest sysbench_vtgate_50
  sysbench_run_and_rest sysbench_vtgate_75
  sysbench_run_and_rest sysbench_vtgate_100
  sysbench_run_and_rest sysbench_vtgate_125
  sysbench_run_and_rest sysbench_vtgate_150
  sysbench_run_and_rest sysbench_vtgate_175

  sysbench_run_and_rest sysbench_mysql_4
  sysbench_run_and_rest sysbench_mysql_8
  sysbench_run_and_rest sysbench_mysql_16
  sysbench_run_and_rest sysbench_mysql_25
  sysbench_run_and_rest sysbench_mysql_50
  sysbench_run_and_rest sysbench_mysql_75
  sysbench_run_and_rest sysbench_mysql_100
  sysbench_run_and_rest sysbench_mysql_125
  sysbench_run_and_rest sysbench_mysql_150
  sysbench_run_and_rest sysbench_mysql_175


  getPodLogs $test_result_path
  transform /Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser $test_result_path
}



