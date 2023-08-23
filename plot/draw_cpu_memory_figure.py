import csv
import os

import pandas as pd
import plot.cpu_memory_figure_util as cpu_memory_figure_util


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

    sorted_data = sorted(zip(mysql_data['Thread'], mysql_data['cpu'], mysql_data['memory']))
    mysql_data['Thread'], mysql_data['cpu'], mysql_data['memory'] = zip(*sorted_data)

    sorted_data = sorted(zip(vtgate_data['Thread'], vtgate_data['cpu'], vtgate_data['memory']))
    vtgate_data['Thread'], vtgate_data['cpu'], vtgate_data['memory'] = zip(*sorted_data)

    mysql_data_df = pd.DataFrame(mysql_data)
    vtgate_data_df = pd.DataFrame(vtgate_data)
    mysql_data_df.to_csv(os.path.join(path, "monitor-mysql-cpu-memory.csv"), index=False)
    vtgate_data_df.to_csv(os.path.join(path, "monitor-vtgate-cpu-memory.csv"), index=False)


def draw_figure_from_aggregation_result(path, figureTitle):
    # dictionary to store filenames and their full paths
    config_list = []
    # iterate over all files in the directory
    for filename in os.listdir(path):
        file_dict = {}
        if not (filename == 'monitor-mysql-cpu-memory.csv' or filename == 'monitor-vtgate-cpu-memory.csv'):
            continue
            # store the filename and its full path in the dictionary
        file_dict['fileName'] = os.path.join(path, filename)
        if 'mysql' in filename:
            file_dict['barName'] = 'MySQL CPU USAGE'
            file_dict['lineName'] = 'MySQL MEMORY USAGE'
        elif 'vtgate' in filename:
            file_dict['barName'] = 'VTGate CPU USAGE'
            file_dict['lineName'] = 'VTGate MEMORY USAGE'
        else:
            pass
        config_list.append(file_dict)

    print(file_dict)

    cpu_memory_figure_util.Draw(
        figureTitle=figureTitle,
        configs=config_list,
        path=path
    )