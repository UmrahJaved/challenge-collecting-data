from main import Generating_links

generating_en_links = Generating_links()
generating_en_links.generating_main_links_postcode()

print(len(generating_en_links.main_links_postcodes))

# generating_en_links.generating_max_page_each_postcodes()

generating_en_links.generating_all_main_page_links()
generating_en_links.generating_all_items_links()