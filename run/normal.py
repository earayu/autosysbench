import sys
import os
import subprocess

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../common')
import autosysbench
import sysbenchdefinition
sys.path.append(current_path + '/../plot')
import draw_figure




def main():
    # prepare
    test_result_path = os.path.join(current_path, '../data/debug')
    os.makedirs(test_result_path, exist_ok=True)
    autosysbench.delete_sysbench_pods()

    # run sysbench
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_4())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_8())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_16())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_25())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_50())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_75())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_100())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_125())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_150())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_175())

    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_4())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_8())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_16())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_25())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_50())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_75())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_100())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_125())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_150())
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_mysql_times_60_threads_175())

    # process sysbench result
    autosysbench.get_pod_logs(test_result_path)
    autosysbench.transform('/Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser', test_result_path)

    # plot
    autosysbench.aggregate_result(test_result_path)
    draw_figure.draw_figure_from_aggregation_result(test_result_path, "Debug Plot")


if __name__ == "__main__":
    main()