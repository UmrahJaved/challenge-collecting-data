from email import header
from typing import dict, List
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
import pprint

path_ressources_file = os.path.join(os.path.abspath(''), "ressources")

class Generating_links():
    """
    This class is regrouping all the method to get all links from immovlan. 
    Each item has a specific url that we will be able to use to get the specifics datas.
    """
    def __init__(self):
        self.zip_path = os.path.join(path_ressources_file, "zipcodes.txt")
        self.path_dict = os.path.join(path_ressources_file, "dict_max_page.json")
        self.main_links_postcodes = None

    def generating_main_links_postcode(self) -> List[str]:
        """
        We create a link to immovlan for each postcodes in Belgium. 
        """
        with open(f"{self.zip_path}", "r") as file:
            belgian_postcodes = [postcode.rstrip('\n') for postcode in file]
        if self.main_links_postcodes == None:
            self.main_links_postcodes = []
        for zip in belgian_postcodes:
            self.main_links_postcodes.append(f"https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns={zip}&propertytypes=maison,appartement&noindex=1&page=1")

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


    def generating_max_page_each_postcodes(self) -> dict[str:int]:
        """
        This method allows us to make a dictionnary with the working
        url for each postcode as index and the max page as value. 
        This dic is then store into a json file (dict_max_page.json)
        """
        for link in self.main_links_postcodes:
            soup = self.request_soup(link)
            sub_soup = soup.find("div", attrs={"class": "col-12 mb-2"})
            total_res = int(sub_soup.text.split()[0])
            max_page = self.calculate_max_page(total_res)
            if max_page:
                with open(self.path_dict, "a") as file:
                    json.dump({f"{link}":f"{max_page}"}, file)
                    file.write("\n")
            time.sleep(random.randint(1,3))

    def generating_all_main_page_links(self):
        """
        This method allows us to generate all the links based on
        the postcode and the number of max page. 
        """
        if os.path.isfile(self.path_dict) == False:
            self.generating_max_page_each_postcodes()
        with open(self.path_dict, "r")as file:
            for line in file.readlines():
                dic = json.loads(line)




            



        

