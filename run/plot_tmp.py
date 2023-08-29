
import sysbench
import os

from plot import draw_cpu_memory_figure
from plot import draw_qps_latency_figure

data_base_path = sysbench.get_data_path()


def draw_qps_latency(date, test_name, title):
    data_path = os.path.join(data_base_path, date, test_name)
    draw_qps_latency_figure.draw_figure_from_aggregation_result(data_path, title)


def draw_cpu_memory(date, test_name, title):
    data_path = os.path.join(data_base_path, date, test_name)
    draw_cpu_memory_figure.draw_figure_from_aggregation_result(data_path, title)


draw_qps_latency('article', 'read_write_split_disable', "WeSQL-Scale vs MySQL (With Read-Write-Split Disabled)")
draw_cpu_memory('article', 'read_write_split_disable', 'WeSQL-Scale vs MySQL (With Read-Write-Split Disabled)')

draw_qps_latency('article', 'read_write_split_enable', 'WeSQL-Scale vs MySQL (With Read-Write-Split Enabled)')
draw_cpu_memory('article', 'read_write_split_enable', 'WeSQL-Scale vs MySQL (With Read-Write-Split Enabled)')
