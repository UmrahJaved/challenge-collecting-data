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
    # path_final_links = os.path.join(os.path.abspath(''), "final_links.json")
    # print(len(list_of_all_main))
    # with open(path_final_links, "w") as file:
    #     json.dump(list_of_all_main, file
    return list_of_all_main


def item_links():
    """
    extracting all links from all pages
    """
    head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    list_of_all_main = generating_all_main_page_links()
    all_information = []
    for element in list_of_all_main:
        r = requests.get(element, headers=head) 
        soup = BeautifulSoup(r.content,"lxml")
        sub_soup = soup.find_all("div", attrs= {"class":"col-lg-5 card-image"})
        for elem in sub_soup:
            all_information.append(elem.find("a"))
        for links in all_information:
            href = links.get("href")
            with open("item_links.txt","a") as file:
                file.write(f"{href}\n")
        all_information = []
        time.sleep(random.randint(1,4))

item_links()