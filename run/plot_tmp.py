
import sysbench
import os

from plot import draw_cpu_memory_figure

data_base_path = sysbench.get_data_path()
data_path = os.path.join(data_base_path, '2023_08_24', 'read_write_split_enable_with_read_pct_80_time_00_06_34')
draw_cpu_memory_figure.draw_figure_from_aggregation_result(data_path, "WeSQL-Scale vs MySQL (CPU & Memory)")
