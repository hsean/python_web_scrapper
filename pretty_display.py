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


# TODO: find longest title in list
# TODO: sum all prices
# read data from a text file
with open('output.txt', 'r') as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        if line.startswith('$'):
            prices.append(line)
        elif line == "\n":
            pass
        else:
            titles.append(line)
            count = count + 1

    # display data
    print("lines array")
    print(lines)
    print("The list of titles is:")
    print(titles)
    print("The list of prices is:")
    print(prices)

    # display each item
    for x in count:
        print(x)
