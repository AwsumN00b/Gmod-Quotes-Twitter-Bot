#!/usr/bin/env python3

#I thought finding quotes would be faster if they were ordered based on youtuber
#This method wont overwrite the original just in case it fucks up (first iteration of this script did fuck up)

#the old file should be deleted or moved, and the new file that is made should be
#renamed to quotes.txt

import os
import sys

quotes = []
with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line = line.strip()
        splitline = line.split(" - ")
        try:
            quotes.append((splitline[0], splitline[1]))
        except IndexError:
            quotes.append(line)

with open("sorted_quotes.txt", "a") as f:
    for key in sorted(quotes, key=lambda x: x[1]):
        print(key)
        if type(key) == tuple:
            f.write(str(key[0]) + " - " + str(key[1]) + "\r\n")
        else:
            f.write(str(key) + "\r\n")
