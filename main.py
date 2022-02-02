from typing import Dict, List
import time 
import os
import random
import math

from bs4 import BeautifulSoup
import lxml
import requests
import pandas as pd
import numpy as np
import json

path_ressources_file = os.path.join(os.path.abspath(''), "ressources")

class Generating_links():
    """
    This class is regrouping all the method to get all links from immovlan. 
    Each item has a specific url that we will be able to use to get the specifics datas.
    """
    def __init__(self):
        self.path_zip = os.path.join(path_ressources_file, "zipcodes_v2.txt")
        self.path_dict = os.path.join(path_ressources_file, "dict_max_page.json")
        self.path_all_mains = os.path.join(path_ressources_file, "all_mains_links.json")
        self.path_all_links = os.path.join(path_ressources_file, "all_items.txt")
        self.main_links_postcodes = None
        self.list_all_mains = None

    def generating_main_links_postcode(self) -> List[str]:
        """
        We create a link to immovlan for each postcodes in Belgium. 
        """
        with open(f"{self.path_zip}", "r") as file:
            belgian_postcodes = [postcode.rstrip('\n') for postcode in file]
        if self.main_links_postcodes == None:
            self.main_links_postcodes = []
        for zip in belgian_postcodes:
            self.main_links_postcodes.append(f"https://immo.vlan.be/en/real-estate?transactiontypes=for-sale,in-public-sale&towns={zip}&propertytypes=house,flat&noindex=1&page=1")

    def request_soup(self, url: str) -> str :
        """
        This method is able to extract the soup from the url insert as a paramter.
        """
        headers_agent = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
        r = requests.get(url, headers=headers_agent)
        soup = BeautifulSoup(r.content, "lxml")
        return soup
    
    def calculate_max_page(self, total_res_postcode: str) -> int:
        """
        This method allows us to calculate the number of page per postecode.
        Each search on Immovlan is limited to 400 items with 20 per page.
        """
        if total_res_postcode == None:
            return None
        elif total_res_postcode > 40000:
            return None
        elif total_res_postcode == 0:
            return None
        elif total_res_postcode <= 20:
            return 1
        elif total_res_postcode >= 400:
            return 20
        else:
            return math.ceil((total_res_postcode / 20))


    def generating_max_page_each_postcodes(self) -> Dict[str:int]:
        """
        This method allows us to make a dictionnary with the working
        url for each postcode as index and the max page as value. 
        This dic is then store into a json file (dict_max_page.json)
        """
        for link in self.main_links_postcodes:
            soup = self.request_soup(link)
            sub_soup = soup.find("div", attrs={"class": "col-12 mb-2"})
            try:
                total_res = int(sub_soup.text.split()[0])
            except AttributeError:
                total_res = 0
            max_page = self.calculate_max_page(total_res)
            if max_page:
                with open(self.path_dict, "a") as file:
                    json.dump({f"{link}":f"{max_page}"}, file)
                    file.write("\n")
            time.sleep(random.randint(1,3))

    def generating_all_main_page_links(self) -> List[str]:
        """
        This method allows us to generate all the links based on
        the postcode and the number of max page. 
        """
        if self.list_all_mains == None:
            self.list_all_mains = []
        if os.path.isfile(self.path_dict) == False:
            self.generating_max_page_each_postcodes()
        with open(self.path_dict, "r")as file:
            for line in file.readlines():
                dic = json.loads(line)
                for key, value in dic.items():
                    value = int(value)
                    if value == 1:
                        self.list_all_mains.append(key)
                    else:
                        for nb in range(1, value + 1):
                            self.list_all_mains.append(key[:-1]+f"{nb}")
        with open(self.path_all_mains, "w") as file:
            json.dump(self.list_all_mains, file)
    
    def generating_all_items_links(self) -> str:
        """
        This function goes through each link stored in the all_mains_links.json
        and extracting the soup in order to get the links of all items. 
        """
        all_information = []
        if len(self.list_all_mains) == 0:
            self.generating_all_main_page_links()
        for element in self.list_all_mains:
            soup = self.request_soup(element)
            sub_soup = soup.find_all("div", attrs= {"class":"col-lg-5 card-image"})
            for element in sub_soup:
                all_information.append(element.find("a"))
            for link in all_information:
                x = link.get("href")
                with open(self.path_all_links, "a") as file:
                    file.write(f"{x}\n")
                all_information = []
            time.sleep(random.randint(1,3))