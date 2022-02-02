# Challenge-Collecting-Data
# Web Scraping Data from Immovlan

![image](https://user-images.githubusercontent.com/96992159/151995717-99281793-72ae-48f0-b679-e000e25b4905.png)

## Scraping URLs of Immovlan

From class `Immovlan` , we collected URLs of houses and apartments based on their zipcodes using different libraries. Class `DataExtraction`, helps in extracting data from each URL collected from `Immovlan`. Finally, we stored all information extracted from the webpages in a csv file.

### Prerequisites

- Python 3.10
- Visual Studio Code (IDE)
- Third Party Libraries:
  - BeautifulSoup
  - Pandas
  - Requests
  - Maths

## Immovlan- URL extraction

In order to extract URLs from "Immovlan". We used the main link to generate different URLs to extract information about houses and appartments. We collected all zipcodes of Belgium in file name `zipcode.txt`and created unique URL for each postcode in Belgium.

---------------------------------------------------------------------------------------------------------------

```
for zip in belgian_postcodes:
            self.main_links_postcodes.append(f"https://immo.vlan.be/en/real-estate?transactiontypes=for-sale,in-public-sale&towns{zip}&propertytypes=house,flat&noindex=1&page=1"
```

-----------------------------------------------------------------------------------------------------------


With "BeautifulSoup" and "requests"  library, we are requesting website make us extract data from the website.We specified "user-agents" of the browser as header when url requests are being made (So that we won't be blocked from the website :))

We used "BeautifulSoup" for web scraping as it is more user-friendly, more readable and allows us to learn faster and begin web scraping easily.

--------------------------------------------------------------------------------------------------------------

```
headers_agent = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
        r = requests.get(url, headers=headers_agent)
        soup = BeautifulSoup(r.content, "lxml")
```

-----------------------------------------------------------------------------------------------------------------


Following that, we calculated the number of pages for each postcode (Each search on Immovlan is limited to 400 items with 20 per page). All the urls for all pages based on zipcodes are extracted and stored in a json file `dict_max_page.json`. 

For better understanding and easy extraction of data, we stored all URLs in a list `self.list_all_mains = []` in `all_mains_links.json`.


-----------------------------------------------------------------------------------------------






![Capture](https://user-images.githubusercontent.com/96992159/152135668-8c37620c-de48-4521-89f6-7417b5fa2fb6.PNG)


-------------------------------------------------------------------------------------------------------------------

With loop on each link stored in the all_mains_links.json, we extracted the soup to get the links of all advertisement on every webpage and stored it in a list `all_information`.



