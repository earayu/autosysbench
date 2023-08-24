import sys
import os
import random
from datetime import datetime

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../common')
import common.autosysbench as autosysbench
import common.sysbenchdefinition as sysbenchdefinition
from common.config import RestSeconds
from common.config import ParserBinPath

sys.path.append(current_path + '/../plot')
import plot.draw_qps_latency_figure as draw_qps_latency_figure
import plot.draw_cpu_memory_figure as draw_cpu_memory_figure


def get_current_date_for_path():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y_%m_%d")
    return formatted_time


def get_current_time_for_path():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H_%M_%S")
    return formatted_time

def get_data_path():
    return os.path.join(current_path, '..', 'data')

def generate_workload(times=100, read_pct=20, threads=[4, 8]):
    workload = []
    for t in threads:
        workload.append(sysbenchdefinition.sysbench_mysql_yaml(times=times, threads=t, read_pct=read_pct))
        workload.append(sysbenchdefinition.sysbench_vtgate_yaml(times=times, threads=t, read_pct=read_pct))
    return workload


def run_sysbench_tests(testname, workload, shuffle=False, enable_monitor=True):
    # prepare
    test_result_path = os.path.join(current_path, '..', 'data', get_current_date_for_path(),
                                    testname + '_time_' + get_current_time_for_path())
    os.makedirs(test_result_path, exist_ok=True)
    autosysbench.delete_sysbench_pods()

    # prepare sysbench workload

    # run sysbench workload
    if shuffle:
        random.shuffle(workload)
    count = 0
    for work in workload:
        pod_yaml = work[0]
        pod_run_time = work[1]
        autosysbench.sysbench_run_and_rest(pod_yaml, pod_run_time, data_path=test_result_path,
                                           enable_monitor=enable_monitor)
        count += 1
        print("===== complete workload (%s/%s) =====" % (count, len(workload)))
        print("===== estimate remaining time: %s seconds =====\n" %
              ((len(workload) - count) * (pod_run_time + RestSeconds)))

    # process sysbench result
    autosysbench.transform_qps_latency_result(ParserBinPath, test_result_path)

    # plot
    autosysbench.aggregate_result(test_result_path)
    draw_qps_latency_figure.draw_figure_from_aggregation_result(test_result_path, testname)
    draw_cpu_memory_figure.sum_all_pod_data(test_result_path)
    draw_cpu_memory_figure.draw_figure_from_aggregation_result(test_result_path, testname)

