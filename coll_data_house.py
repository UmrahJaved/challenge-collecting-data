from http.client import ImproperConnectionState
from bs4 import BeautifulSoup
import requests
from typing import Dict
import time
import os
import random
from multiprocessing import Pool
from pathlib import Path


class DataExtraction:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    def extract_single_page(self, pagelink: str)-> Dict:
        """
        extract the detail data for each item
        """
        r = requests.get(pagelink, headers=self.headers)
        soup = BeautifulSoup(r.content, "lxml")
        house_features = {}
        for locality in soup.find_all("span", attrs={"class": "city-line pl-1"}):
            house_features['Locality'] = locality.text
        for titleblock in soup.find_all("nav", attrs={"class": "my-2 d-none d-md-flex"}):
            types_of_prop = titleblock.find_all("a", attrs={})
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
        print(f"start process {txt_file_path}")
        links = []
        with open(txt_file_path, 'r') as link_reader:
            links = link_reader.read().splitlines()
        for link in links:
            try:
                write_data = self.extract_single_page(link)
                with open(txt_file_path.replace(".txt", ".json"), "a") as filewriter:
                    filewriter.write(str(write_data))
                    filewriter.write("\n")
            except:
                print(f"error in this link: {link}")
            time.sleep(random.randrange(1, 2))
        print(f"end process {txt_file_path}")


my_test = DataExtraction()
# my_test.extract_single_page('https://immo.vlan.be/en/detail/residence/for-sale/9090/melle/rbe04276')
filepath = os.path.join(os.path.abspath(''), Path("ressources/divided_items"))
line_per_file = 2340
file_list = []
for i in range(1, 3):
    file_list.append(f"{filepath}{i*line_per_file}.txt")


if __name__ == "__main__":
    starttime = time.time()
    pool = Pool()
    pool.map(my_test.loop_txt, [file for file in file_list])
    pool.close()
    endtime = time.time()
    print(f"Time taken {endtime-starttime} seconds")
