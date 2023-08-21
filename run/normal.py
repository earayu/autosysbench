import sys
import os
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../common')
import autosysbench
import sysbenchdefinition
import subprocess



def main():
    test_result_path = os.path.join(current_path, '../data/debug')
    os.makedirs(test_result_path, exist_ok=True)
    autosysbench.delete_sysbench_pods()

    
    autosysbench.sysbench_run_and_rest(sysbenchdefinition.sysbench_vtgate_times_60_threads_8())


    autosysbench.get_pod_logs(test_result_path)
    autosysbench.transform('/Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser', test_result_path)


if __name__ == "__main__":
    main()