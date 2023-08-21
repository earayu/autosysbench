

import os
import figure_util

def read_file_and_draw(path, figureTitle):
    # dictionary to store filenames and their full paths
    config_list = []
    # iterate over all files in the directory
    for filename in os.listdir(path):
        file_dict = {}
        # check if the file is a '.txt' file
        if not filename.endswith('.csv'):
            continue 
        # store the filename and its full path in the dictionary
        file_dict['fileName'] = os.path.join(path, filename)
        if filename.startswith('test-mysql'):
            file_dict['barName'] = 'MySQL'
            file_dict['lineName'] = 'MySQL Latency'
        else:
            file_dict['barName'] = 'VTGate'
            file_dict['lineName'] = 'VTGate Latency'
        config_list.append(file_dict)
        
    print(file_dict)

    figure_util.Draw(
        figureTitle=figureTitle,
        configs=config_list
    )