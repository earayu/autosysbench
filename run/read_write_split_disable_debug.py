import sysbench


def debug_workload():
    return sysbench.generate_workload(times=1, read_pct=20, threads=[4, 8])


sysbench.run_sysbench_tests('read_write_split_disable_debug', debug_workload(), enable_monitor=False)
