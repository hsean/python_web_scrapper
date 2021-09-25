#!/usr/bin/python3

###############################################################################
# Author: Sean Hendrickson
# File: pretty_display.py
# Desc: This file displays a list of titles and prices in two columns and
#       displays the total sum at the end of the list
###############################################################################

# store text file
lines = []

# read data from a text file
with open('output.txt', 'r') as f:
    lines = f.readlines()

    count = 0
    for line in lines:
        count += 1
        print(f'line {count}: {line}')
