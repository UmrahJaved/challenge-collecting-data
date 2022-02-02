# challenge-collecting-data
#Web Scraping Data from Immovlan
---------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/96992159/151995717-99281793-72ae-48f0-b679-e000e25b4905.png)

## Scraping URLs of Immovlan
---------------------------------------------------------------------------------------------------------
From class `Immovlan` , we collected URLs of houses and apartments based on their zipcodes using different libraries. Class `DataExtraction`, helps in extracting data from each URL collected from `Immovlan`. Finally, storing all information in csv file.

#### Third party Packages:
- BeautifulSoup
- Pandas
- Numpy

## Immovlan- URL extraction
-----------------------------------------------------------------------------------------------------------
Using all zipcodes of Belgium from `zipcode.txt`, we are creating URL for each postcode in Belgium.

"""

for zip in belgian_postcodes:
            self.main_links_postcodes.append(f"https://immo.vlan.be/en/real-estate?transactiontypes=for-sale,in-public-sale&towns={zip}&propertytypes=house,flat&noindex=1&page=1"

"""


