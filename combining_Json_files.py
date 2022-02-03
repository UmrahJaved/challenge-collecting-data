import os
from pathlib import Path
import ast
import csv

file_path_json = os.path.join(os.path.abspath(''), Path('ressources/divided_items_'))
line_num = 2340
files = []
for i in range(1, 9):
    files.append(f'{file_path_json}{i*line_num}.json')
print(files)


path_all_json_files = os.path.join(os.path.abspath(''), Path('ressources/all_json_files.json'))
key_names = []
for file in files:
    with open(file, 'r') as file_reader, open(path_all_json_files, 'a') as con_file_writer:
        content = file_reader.read().splitlines()
        for line in content:
            if len(line) > 65:
                print(line)
                line_dict = ast.literal_eval(line)
                print(type(line_dict))
                for key, value in line_dict.items():
                    if key not in key_names:
                        key_names.append(key)
                    if value == 'Yes':
                        line_dict[key] = '1'
                    elif value == 'No':
                        line_dict[key] = '0'  
                con_file_writer.write(str(line_dict))
                con_file_writer.write('\n')

    print(key_names)
    print(len(key_names))


path_all_data_csv = os.path.join(os.path.abspath(''), Path('ressources/all_data.csv'))
list_of_data_dict = []
with open(path_all_json_files, 'r') as json_reader, open(path_all_data_csv, 'a') as all_data_writer:
    data_list = json_reader.read().splitlines()
    for line in data_list:
        list_of_diction = ast.literal_eval(line)
        list_of_data_dict.append(list_of_diction)
    csvwriter = csv.DictWriter(all_data_writer, fieldnames=key_names, restval='None')
    csvwriter.writeheader()
    csvwriter.writerows(list_of_data_dict)
            

       