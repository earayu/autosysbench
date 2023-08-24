import os
import qps_latency_figure_util
import subprocess
import pandas as pd


def transform_qps_latency_result(sysparser_binary, path):
    if not os.path.isdir(path):
        print("Path does not exist")
        exit(1)

    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "mysql_qps_latency.txt" or file == "vtgate_qps_latency.txt":
                filepath = os.path.join(root, file)
                filename = os.path.basename(filepath).replace('.txt', '')
                subprocess.run(f'{sysparser_binary} --file="{filepath}" > {os.path.join(root, filename)}.csv',
                               shell=True)
                print(f"Processing completed: {filepath}")


def aggregate_result(path):
    mysql_data = []
    vtgate_data = []
    # path = os.path.join(path, "pod")
    for root, dirs, files in os.walk(path):
        for file in files:
            full_file_name = os.path.join(root, file)
            df = pd.read_csv(full_file_name, sep="\t")
            if file == "mysql_qps_latency.csv":
                mysql_data.append(df)
            elif file == "vtgate_qps_latency.csv":
                vtgate_data.append(df)
            else:
                pass

    mysql_data = pd.concat(mysql_data).sort_values(by="Threads")
    vtgate_data = pd.concat(vtgate_data).sort_values(by="Threads")

    mysql_data.to_csv(os.path.join(path, "aggregated_mysql_qps_latency.csv"), index=False, sep="\t")
    vtgate_data.to_csv(os.path.join(path, "aggregated_vtgate_qps_latency.csv"), index=False, sep="\t")

def draw_figure_from_aggregation_result(path, figureTitle):
    # dictionary to store filenames and their full paths
    config_list = []
    # iterate over all files in the directory
    for filename in os.listdir(path):
        file_dict = {}
        if not (filename == 'aggregated_mysql_qps_latency.csv' or filename == 'aggregated_vtgate_qps_latency.csv'):
            continue 
        # store the filename and its full path in the dictionary
        file_dict['fileName'] = os.path.join(path, filename)
        if 'mysql' in filename:
            file_dict['barName'] = 'MySQL'
            file_dict['lineName'] = 'MySQL Latency'
        elif 'vtgate' in filename:
            file_dict['barName'] = 'WeSQL-Scale'
            file_dict['lineName'] = 'WeSQL-Scale Latency'
        else:
            pass
        config_list.append(file_dict)

    config_list = sorted(config_list, key=lambda x: sorted(x['barName']))
    print(config_list)
    qps_latency_figure_util.Draw(
        figureTitle=figureTitle,
        configs=config_list,
        path=path
    )