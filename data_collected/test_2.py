# string = 'https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=9991&propertytypes=maison,appartement&noindex=1&page=1'

# string_2 = string[:-1] + '12'
# print(string
import pprint
new_dict = {"https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=1000&propertytypes=maison,appartement&noindex=1&page=1": 20, "https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=1020&propertytypes=maison,appartement&noindex=1&page=1": 8, "https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=1030&propertytypes=maison,appartement&noindex=1&page=1": 17, "https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=1040&propertytypes=maison,appartement&noindex=1&page=1": 8, "https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=1050&propertytypes=maison,appartement&noindex=1&page=1": 20}


list_of_all_main = []
for key, value in new_dict.items():
    if value == 1:
        list_of_all_main.append(key)
    else:
        for x in range(1,value+1):
            list_of_all_main.append(key[:-1]+f"{x}")

pprint.pp(list_of_all_main)