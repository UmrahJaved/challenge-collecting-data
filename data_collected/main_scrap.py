import time 
import os
import re

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
        max_result = self.soup.find_all("div", attrs={"class":"col-12 mb-2"})
        nb_page = []
        for elem in max_result:
            page = elem.text.split()
            nb_page.append(page[0])
        print(nb_page)

    def loop_postcode(self):
        pass



url_1 = "https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns=1450&noindex=1&page=1"

test = Immovlan(url_1)
test.nb_of_page()
