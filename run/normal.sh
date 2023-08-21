normal_sh_path=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
source "$normal_sh_path/../common/autosysbench.sh"
normal_sh_path=$(dirname "$(realpath "${BASH_SOURCE[0]}")")


main() {
  test_result_path="$normal_sh_path/../data/debug"
  mkdir $test_result_path
  deleteSysbenchPods

  # sysbench_vtgate_then_mysql_175_threads_loop 1

  # sysbench_run_and_rest sysbench_vtgate_4
  # sysbench_run_and_rest sysbench_vtgate_8
  # sysbench_run_and_rest sysbench_vtgate_16
  # sysbench_run_and_rest sysbench_vtgate_25
  # sysbench_run_and_rest sysbench_vtgate_50
  # sysbench_run_and_rest sysbench_vtgate_75
  # sysbench_run_and_rest sysbench_vtgate_100
  # sysbench_run_and_rest sysbench_vtgate_125
  # sysbench_run_and_rest sysbench_vtgate_150
  # sysbench_run_and_rest sysbench_vtgate_175

  # sysbench_run_and_rest sysbench_mysql_4
  # sysbench_run_and_rest sysbench_mysql_8
  # sysbench_run_and_rest sysbench_mysql_16
  # sysbench_run_and_rest sysbench_mysql_25
  # sysbench_run_and_rest sysbench_mysql_50
  # sysbench_run_and_rest sysbench_mysql_75
  # sysbench_run_and_rest sysbench_mysql_100
  # sysbench_run_and_rest sysbench_mysql_125
  # sysbench_run_and_rest sysbench_mysql_150
  # sysbench_run_and_rest sysbench_mysql_175

  getPodLogs $test_result_path
  transform /Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser $test_result_path

  python3 "$normal_sh_path/../plot/main.py"
}

main