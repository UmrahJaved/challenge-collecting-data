from hashlib import new
import os
import json
import lxml
import pprint


#save the dict on a field (txt ?)
path = os.path.join(os.path.abspath(''), "dict_max_page.json")

with open(path, "r") as file:
    txt = file.read()
new_dict = json.loads(txt)

pprint.pp(new_dict)
print(len(new_dict))

value_tot = 0
for key, value in new_dict.items():
    value_tot += value

print(value_tot)
print(value_tot*15)


