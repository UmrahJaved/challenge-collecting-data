import time 
import os
import re
import math

from bs4 import BeautifulSoup
from lxml import html
import requests
import pandas as pd
import numpy as np
import selenium


class Immovlan():
    """
    scrapping the page of a website (immo)
    """
    def __init__(self,url):
        self.url = url
        self.links = None
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
        r = requests.get(self.url, headers=headers)
        self.soup = BeautifulSoup(r.content, "lxml")

    def request(self):
        """
        Extracting all the links of the items listed on the page (ImmoVlan) 
        """
        search_results_a = []
        if self.links == None:
            self.links = []
        sub_soup = self.soup.find_all("div", attrs= {"class":"col-lg-5 card-image"})
        for elem in sub_soup:
            search_results_a.append(elem.find("a"))
        for links in search_results_a:
            x = links.get("href")
            print(x)
            self.links.append(x)
    
    def nb_of_page(self):
        """
        Getting the nomber of pages needed to extract all the information (max 20)
        """
        soup_result = self.soup.find_all("div", attrs={"class":"col-12 mb-2"})
        for elem in soup_result:
            page = int(elem.text.split()[0])
        if page == 0:
            max_page = 0
        elif page <= 20:
            max_page = 1
        elif page >= 400:
            max_page = 20
        else:
            max_page = math.ceil((page / 20))
        return max_page

    def loop_postcode(self):
        pass



url_1 = "https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=1450&noindex=1&page=1"

test = Immovlan(url_1)
print(test.nb_of_page())
