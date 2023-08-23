import csv
import os

import pandas as pd


def calculate_average_usage(filename):
    """计算CSV文件中的CPU和内存的平均使用率."""
    total_cpu = 0
    total_memory = 0

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # 跳过表头
        next(reader)

        # 计数器，记录总行数
        count = 0

        for row in reader:
            cpu = int(row[3][:-1])  # 提取CPU值，去掉末尾的"m"并转换为整数
            memory = int(row[4][:-2])  # 提取内存值，去掉末尾的"Mi"并转换为整数

            total_cpu += cpu
            total_memory += memory
            count += 1

    # 计算平均值
    avg_cpu = total_cpu / count
    avg_memory = total_memory / count
    # print(filename)
    # print("avg_cpu : " + str(avg_cpu))
    # print("avg_memory :" + str(avg_memory))

    return avg_cpu, avg_memory


def sum_cpu_memory(dir_path):
    # 如果只想获取文件，可以如下操作:
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    total_cpu = 0
    total_memory = 0
    for item in files:
        if not item.startswith("monitor"):
            continue
        avg_cpu, avg_memory = calculate_average_usage(os.path.join(dir_path, item))
        total_cpu = total_cpu + avg_cpu
        total_memory = total_memory + avg_memory
    return total_cpu, total_memory


def sum_all_pod_data(path: str):
    dir_path = os.path.join(path, "pod")
    directories = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d))]
    mysql_data = {'Thread': [], 'cpu': [], 'memory': []}
    vtgate_data = {'Thread': [], 'cpu': [], 'memory': []}
    for directory in directories:
        if directory.startswith("test-mysql"):
            total_cpu, total_memory = sum_cpu_memory(os.path.join(dir_path, directory))
            str_list = directory.split("-")
            threads = int(str_list[5])
            mysql_data['Thread'].append(threads)
            mysql_data['cpu'].append(total_cpu)
            mysql_data['memory'].append(total_memory)
        elif directory.startswith("test-vtgate"):
            total_cpu, total_memory = sum_cpu_memory(os.path.join(dir_path, directory))
            str_list = directory.split("-")
            threads = int(str_list[5])
            vtgate_data['Thread'].append(threads)
            vtgate_data['cpu'].append(total_cpu)
            vtgate_data['memory'].append(total_memory)
    mysql_data_df = pd.DataFrame(mysql_data)
    vtgate_data_df = pd.DataFrame(vtgate_data)
    mysql_data_df.to_csv(os.path.join(path, "monitor-mysql-cpu-memory.csv"), index=False)
    vtgate_data_df.to_csv(os.path.join(path, "monitor-vtgate-cpu-memory.csv"), index=False)

