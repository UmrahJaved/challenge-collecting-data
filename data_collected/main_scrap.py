import time 
import os
import re
import math
import random
from statistics import mean

from bs4 import BeautifulSoup
from lxml import html
import requests
import pandas as pd
import numpy as np
import selenium
import json
import pprint


def generating_main_links():
    """
    fonction that generating the main links (page1) based on postcode (from "zipcodes.txt").
    Saving all the main links on a txt_files for memory issues. 
    """
    zip_path = os.path.join(os.path.abspath(''), "zipcodes.txt")
    with open(f"{zip_path}", "r") as file:
        belgian_postcodes = [zip.rstrip('\n') for zip in file]
    main_link_postcode = [f"https://immo.vlan.be/fr/immobilier?transactiontypes=a-vendre,en-vente-publique&towns={zip}&propertytypes=maison,appartement&noindex=1&page=1" for zip in belgian_postcodes]
    return main_link_postcode


class Immovlan():
    """
    scrapping the page of a website (immo)
    """
    def __init__(self,url):
        self.url = url
        self.links = None
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
        r = requests.get(self.url, headers=self.headers)
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
        Has to be done once per postcode.
        """
        soup_result = self.soup.find_all("div", attrs={"class":"col-12 mb-2"})
        for elem in soup_result:
            results_tot = int(elem.text.split()[0])
            if results_tot > 40000:
                return None
            if results_tot == 0:
                max_page = results_tot       
            elif results_tot <= 20:
                max_page = 1
            elif results_tot>= 400:
                max_page = 20
            else:
                max_page = math.ceil((results_tot / 20))
            return max_page
    
    def make_json_postcode_maxpage(self):
        """
        Making a dict with the links for each postcode as index and
        maximum numbers of page per postcode. 
        """
        zip_page_dic = {}
        urls_list = generating_main_links()
        for url in urls_list:
            extract_data = Immovlan(url)
            url_max_page = Immovlan.nb_of_page(extract_data)
            if url_max_page:
                zip_page_dic[f"{url}"] = url_max_page
            time.sleep(random.randint(1,5))
        path = os.path.join(os.path.abspath(''), "dict_max_page.json")
        with open(path,"w") as file:
            json.dump(zip_page_dic,file)

    def extract_single_page(self, pagelink: str):
        """
        extract the detail data for each item
        """
        r = requests.get(pagelink, headers=self.headers)
        soup = BeautifulSoup(r.content, "lxml")
        for locality in soup.find_all("span", attrs={"class": "city-line pl-1"}):
            print(locality.text)
        for type_of_property in soup.find_all("span", attrs={"class": "find class att"}):
            print("ok")
            print(type_of_property.text)
        list_right = []
        list_left = []
        for price in soup.find_all("span", attrs={"class": "d-block price-label"}):
            print(price.text)
        for col_right in soup.find_all("div", attrs={"class": "col-4 text-right"}):
            list_right.append(col_right.text)
        for col_left in soup.find_all("div", attrs={"class": "col-8"}):
            list_left.append(col_left.text)
        print(list_right)
        print(list_left)

def generating_all_main_page_links():
    """
    dumping each links based on zipcode and max page into a json file
    based on dict_max_page.json file that contain the link for each postcode and the max_page. 
    """
    list_of_all_main = []
    path_file_jason = os.path.join(os.path.abspath(''), "dict_max_page.json")
    with open(path_file_jason, "r") as file:
        txt = file.read()
        new_dict = json.loads(txt)
        # pprint.pp(new_dict)
    for key, value in new_dict.items():
        if value == 1:
            list_of_all_main.append(key)
        else:
            for x in range(1,value+1):
                list_of_all_main.append(key[:-1]+f"{x}")
    path_final_links = os.path.join(os.path.abspath(''), "final_links.json")
    print(len(list_of_all_main))
    with open(path_final_links, "w") as file:
        json.dump(list_of_all_main, file)

generating_all_main_page_links()