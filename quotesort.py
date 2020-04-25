#!/usr/bin/env python3

#I thought finding quotes would be faster if they were ordered based on youtuber
#This method wont overwrite the original just in case it fucks up

#the old file should be deleted or moved, and the new file that is made should be
#renamed to quotes.txt

import os

dict = {}
with open("quotes.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        splitline = line.split(" - ")
        try:
            dict[splitline[1]] = line
        except IndexError:
            dict[line] = line

with open("sorted_quotes.txt", "a") as f:
    for key in sorted(dict):
        print(key)
        f.write(dict[key] + "\r\n")
