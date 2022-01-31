import main_scrap
import time
import os 
import json

test = {}

urls_list = main_scrap.generating_main_links()


# url_max_page = []
# for nb in range (20)
# test = main_scrap.Immovlan(url[0])
# url_max_page.append(main_scrap.Immovlan.nb_of_page(test))
# time.sleep(3)
for url in urls_list:
    extract_data = main_scrap.Immovlan(url)
    url_max_page = main_scrap.Immovlan.nb_of_page(extract_data)

    if url_max_page:
        test[f"{url}"] = url_max_page
        #find a solution to extract data on different time (not at once) with add ? 
        if len(test) % 250 == 0:
            pass
    time.sleep(2)

#save the dict on a field (txt ?)
path = os.path.join(os.path.abspath(''), "dict_max_page.json")
with open(path, "w") as file:
    json.dump(test, file)

