import sysbench


def debug_workload():
    return sysbench.generate_workload(times=200, read_pct=20, threads=[4, 8])


sysbench.run_sysbench_tests('read_after_write_disable_with_monitor_debug', debug_workload(), enable_monitor=True)
