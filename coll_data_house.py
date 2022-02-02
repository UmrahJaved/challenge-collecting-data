from bs4 import BeautifulSoup
import requests
from typing import Dict
import time
import random

class DataExtraction:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    def extract_single_page(self, pagelink: str)-> Dict:
        """
        extract the detail data for each item
        """
        r = requests.get(pagelink, headers=self.headers)
        soup = BeautifulSoup(r.content, "lxml")
        house_features ={}
        for locality in soup.find_all("span", attrs={"class": "city-line pl-1"}):
            house_features['Locality'] = locality.text
        for titleblock in soup.find_all("nav", attrs={"class": "my-2 d-none d-md-flex"}):
            types_of_prop =  titleblock.find_all("a", attrs={})
            house_features['Type of property'] = types_of_prop[1].get("href").split("/")[5]
            house_features['Subtype of property'] = types_of_prop[3].get("href").split("/")[5]
        for price in soup.find_all("span", attrs={"class": "d-block price-label"}):
            house_features['Price'] = (price.text).encode('ascii', 'ignore').decode("utf-8").strip()
        for row in soup.find_all("div", attrs={"class": "section-row"}):
            value_right = row.find("div", attrs={"class": "col-4 text-right"})
            value_left = row.find("div", attrs={"class": "col-8"})
            if value_right is not None and value_left is not None:
                house_features[value_left.text] = value_right.text
        return house_features

    def loop_txt(self, txt_file_path: str):
        links= []
        with open(txt_file_path, 'r') as link_reader:
            links = link_reader.read().splitlines()
        dict_list = []
        for link in links:
            try:
                dict_list.append(self.extract_single_page(link))
            except:
                print(f"error in this link: {link}")
            time.sleep(random.randrange(1, 3))
        
        print(dict_list)

my_test = DataExtraction()
#my_test.extract_single_page('https://immo.vlan.be/en/detail/residence/for-sale/9090/melle/rbe04276')
my_test.loop_txt("/home/dilsad/BeCode_Projects/challenge-collecting-data/data_collected/example_output.txt")