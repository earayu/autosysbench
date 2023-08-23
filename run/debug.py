import sys
import os
import random


current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path + '/../common')
import autosysbench
import sysbenchdefinition
sys.path.append(current_path + '/../plot')
import draw_qps_latency_figure

data_path = '/Users/earayu/Documents/GitHub/autosysbench/data/archive/debug'
autosysbench.transform_qps_latency_result('/Users/earayu/Documents/GitHub/sysbench-output-parser/sysparser', data_path)
autosysbench.aggregate_result(data_path)