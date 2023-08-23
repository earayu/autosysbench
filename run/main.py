import sys
import os
import random


current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../common')
import autosysbench
import sysbenchdefinition
sys.path.append(current_path + '/../plot')
import draw_qps_latency_figure
import draw_cpu_memory_figure

def generate_workload(times=60, read_pct=20, threads=[4,8,16,25,50,75,100,125,150,175,200]):
    workload = []
    for t in threads:
        workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=times, threads=t, read_pct=read_pct))
    return workload

def read_pct_20_workload():
    return generate_workload(times=60, read_pct=20, threads=[4,8,16,25,50,75,100,125,150,175,200])

def read_pct_50_workload():
    return generate_workload(times=60, read_pct=50, threads=[4,8,16,25,50,75,100,125,150,175,200])

def read_pct_80_workload():
    return generate_workload(times=60, read_pct=80, threads=[4,8,16,25,50,75,100,125,150,175,200])



# read_write_split_disable2
def run_sysbench_tests(testname, workload):
    # prepare
    test_result_path = os.path.join(current_path, '../data/' + testname)
    os.makedirs(test_result_path, exist_ok=True)
    autosysbench.delete_sysbench_pods()

    # prepare sysbench workload

    # run sysbench workload
    random.shuffle(workload)
    count = 0
    for work in workload:
        pod_yaml = work[0]
        pod_run_time = work[1]
        autosysbench.sysbench_run_and_rest(pod_yaml, pod_run_time, data_path=test_result_path)
        count += 1
        print("===== complete workload (%s/%s) =====" % (count, len(workload)))
        print("===== estimate remaining time: %s seconds =====" % (len(workload) - count) * pod_run_time )

    # process sysbench result
    autosysbench.transform_qps_latency_result('/Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser', test_result_path)

    # plot
    autosysbench.aggregate_result(test_result_path)
    draw_qps_latency_figure.draw_figure_from_aggregation_result(test_result_path, testname)
    draw_cpu_memory_figure.sum_all_pod_data(test_result_path)

if __name__ == "__main__":
    for round in range(8, 9):
        run_sysbench_tests('read_write_split_enable_%s_with_read_pct_20' % round, read_pct_20_workload())
        # run_sysbench_tests('read_write_split_enable_%s_with_read_pct_50' % round, read_pct_50_workload())
        # run_sysbench_tests('read_write_split_enable_%s_with_read_pct_80' % round, read_pct_80_workload())
