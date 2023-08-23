import sysbench


def debug_workload():
    return sysbench.generate_workload(times=1, read_pct=20, threads=[4, 8])


def read_pct_20_workload():
    return sysbench.generate_workload(times=60, read_pct=20, threads=[4, 8, 16, 25, 50, 75, 100, 125, 150, 175, 200])


def read_pct_50_workload():
    return sysbench.generate_workload(times=60, read_pct=50, threads=[4, 8, 16, 25, 50, 75, 100, 125, 150, 175, 200])


def read_pct_80_workload():
    return sysbench.generate_workload(times=60, read_pct=80, threads=[4, 8, 16, 25, 50, 75, 100, 125, 150, 175, 200])


sysbench.run_sysbench_tests('read_write_split_enable_with_read_pct_20', read_pct_20_workload(), enable_monitor=False)
sysbench.run_sysbench_tests('read_write_split_enable_with_read_pct_50', read_pct_50_workload(), enable_monitor=False)
sysbench.run_sysbench_tests('read_write_split_enable_with_read_pct_80', read_pct_80_workload(), enable_monitor=False)
