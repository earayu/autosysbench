import os 
import draw_figure



current_path = os.path.abspath(__file__)
directory_path = os.path.dirname(current_path)


draw_figure.read_file_and_draw(directory_path + '/../data/debug', "Debug Plot")

draw_figure.read_file_and_draw(directory_path + '/../data/read_write_split_disable', "MySQL vs WeSQL-Scale (With Read Write Split Disabled)")
draw_figure.read_file_and_draw(directory_path + '/../data/read_write_split_enable', "MySQL vs WeSQL-Scale (With Read Write Split Enabled)")