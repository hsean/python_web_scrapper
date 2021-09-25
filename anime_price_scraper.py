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

# create lists to handle data
titles = []
prices = []
#total_cost = 0.0;
#print(total_cost)

# open each URL
for URL in URL_list:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    # find page elements
    title_element = soup.find(class_="product-details-full-content-header-title")
    price_element = soup.find(class_="product-views-price-lead")

    # add new data to the arrays
    titles.append(title_element.text.strip())
    prices.append(price_element.text.strip())

    # sum total cost
    #base_price = (price_element.text.strip()).replace('$',''))
    #stripped_price = price_element.text.strip().replace('$',' ')
    #print(stripped_price)
    #total_cost = total_cost + float(stripped_price)
    #print(total_cost)


# print arrays
# TODO: adjust title array padding to be [length + 1] of longest title
for t, p in zip(titles, prices):
    print('{:80} {:20}'.format(t, p))

