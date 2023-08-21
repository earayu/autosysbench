import os 
import draw_figure



current_path = os.path.dirname(os.path.abspath(__file__))

draw_figure.read_file_and_draw(current_path + '/../data/debug', "Debug Plot")

# draw_figure.read_file_and_draw(current_path + '/../data/read_write_split_disable', "MySQL vs WeSQL-Scale (With Read Write Split Disabled)")
# draw_figure.read_file_and_draw(current_path + '/../data/read_write_split_enable', "MySQL vs WeSQL-Scale (With Read Write Split Enabled)")