# from hashlib import new
# import os
# import json
# import lxml
# import pprint


# #save the dict on a field (txt ?)
# path = os.path.join(os.path.abspath(''), "dict_max_page.json")

# with open(path, "r") as file:
#     txt = file.read()
# new_dict = json.loads(txt)

# pprint.pp(new_dict)
# print(len(new_dict))

# value_tot = 0
# for key, value in new_dict.items():
#     value_tot += value

# print(value_tot)
# print(value_tot*15)

# from email import header
# from wsgiref import headers
# from bs4 import BeautifulSoup
# import requests
# import lxml

# url = "https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=1080&propertytypes=maison,appartement&noindex=1&page=1"
# head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

# r = requests.get(url, headers=head)
# soup = BeautifulSoup(r.content, 'lxml')
# sub_soup = soup.find("div", attrs={"class": "col-12 mb-2"})
# print(sub_soup)
# total_res = int(sub_soup.text.split()[0])
# print(total_res)
import json
import os
from textwrap import indent

list =[x for x in range(1,20)]
max_page = 10


path = os.path.join(os.path.abspath(''), "test.json")
for x in list:
    with open(path, "a") as file:
        json.dump({f"{x}":f"{max_page}"}, file)
        file.write("\n")

with open(path,'r') as file:
    for line in file.readlines():
        dic = json.loads(line)
        print(type(dic))
