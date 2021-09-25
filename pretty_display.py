#!/usr/bin/python3

###############################################################################
# Author: Sean Hendrickson
# File: pretty_display.py
# Desc: This file displays a list of titles and prices in two columns and
#       displays the total sum at the end of the list
###############################################################################

# store text file
lines = []
titles = []
prices = []
totalCost = 0
max_title_length = 0
max_price_length = 0

# read data from a text file
with open('output.txt', 'r') as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        if line.startswith('$'):
            #prices.append(line)
            simplifiedPrice = line.replace('$','')     
            simplifiedPrice = simplifiedPrice.replace('\n','')
            prices.append(simplifiedPrice)
            totalCost += float(simplifiedPrice)    # sum prices for later use
        elif line == "\n":
            pass
        else:
            titles.append(line)
            count = count + 1
            if len(line) > max_title_length:    # find largest string
                max_title_length = len(line)

    # find maximum price length
    max_price_length = len(str(round(totalCost, 2)))

    # display each item
    for x in range(count):
        print("{:{x}} ${:>{y}}".format(titles[x].strip(), prices[x].strip(), x=max_title_length, y=max_price_length))

    print("{:>{x}} ${:{y}.2f}".format("Total Cost:", round(totalCost, 2), x=max_title_length, y=max_price_length))
    print("Max string length =", max_title_length)
