import os 
import json


my_postal_codes = []

dir_path = os.path.join(os.path.abspath(''), "ressources")

file_path = os.path.join(dir_path,"zipcodes.txt")
file_path_v2 = os.path.join(dir_path,"zipcodes_v2.txt")

with open(file_path, "r") as file:
    for line in file.readlines():
        my_postal_codes.append(line.strip())

my_postal_codes = list(dict.fromkeys(my_postal_codes))
print(my_postal_codes)

with open(file_path_v2,"w") as file:
    for zip in my_postal_codes:
        file.write(zip + "\n")
