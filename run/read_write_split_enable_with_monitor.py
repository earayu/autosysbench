import sysbench


def read_pct_20_workload():
    return sysbench.generate_workload(times=100, read_pct=20, threads=[4, 25, 50, 100, 200])


def read_pct_50_workload():
    return sysbench.generate_workload(times=100, read_pct=50, threads=[4, 25, 50, 100, 200])


def read_pct_80_workload():
    return sysbench.generate_workload(times=100, read_pct=80, threads=[4, 25, 50, 100, 200])


sysbench.run_sysbench_tests('read_write_split_enable_with_read_pct_20', read_pct_20_workload(), enable_monitor=True)
sysbench.run_sysbench_tests('read_write_split_enable_with_read_pct_50', read_pct_50_workload(), enable_monitor=True)
sysbench.run_sysbench_tests('read_write_split_enable_with_read_pct_80', read_pct_80_workload(), enable_monitor=True)
