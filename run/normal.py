import sys
import os
import random


current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../common')
import autosysbench
import sysbenchdefinition
sys.path.append(current_path + '/../plot')
import draw_figure



# read_write_split_disable2
def run_sysbench_tests(testname):
    # prepare
    test_result_path = os.path.join(current_path, '../data/' + testname)
    os.makedirs(test_result_path, exist_ok=True)
    autosysbench.delete_sysbench_pods()

    # prepare sysbench workload
    workload = []

    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=4, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=8, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=16, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=25, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=50, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=75, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=100, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=125, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=150, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=60, threads=175, read_pct=50))

    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=4, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=8, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=16, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=25, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=50, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=75, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=100, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=125, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=150, read_pct=50))
    workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=60, threads=175, read_pct=50))


    # run sysbench workload
    random.shuffle(workload)
    count = 0
    for work in workload:
        autosysbench.sysbench_run_and_rest(work)
        count += 1
        print("complete workload (%s/%s)" % (count, len(workload)))

    # process sysbench result
    autosysbench.get_pod_logs(test_result_path)
    autosysbench.transform('/Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser', test_result_path)

    # plot
    autosysbench.aggregate_result(test_result_path)
    draw_figure.draw_figure_from_aggregation_result(test_result_path, testname)


if __name__ == "__main__":
    run_sysbench_tests('read_write_split_disable8_with_read_pct_50')