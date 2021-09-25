#!/usr/bin/python3

###############################################################################
# Author: Sean Hendrickson
# File: anime_collection_scraper.py
# Desc: This file is used to find the name and price for bluray/dvd box sets
#       from rightstufanime.com
#
#       All links will be passed through a text file called 
#       anime_series_hyperlinks and printed to standard output
###############################################################################

import requests
from bs4 import BeautifulSoup

# read data from a text file
with open('hyperlinks.txt', 'r') as f:
    URL_list = f.readlines()

# open each URL
for URL in URL_list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # find page elements
    title_element = soup.find(class_="product-details-full-content-header-title")
    price_element = soup.find(class_="product-views-price-lead")

    # Display results
    print(title_element.text.strip())
    print(price_element.text.strip())
    print()
