#!/usr/bin/python3

import urllib.request
import re

while True:
    try:
        print("where should we search?")
        url = input()
        print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
        searchFor = input()
        searchMe = urllib.request.urlopen(url).read().decode("utf-8")
        if re.search(searchFor, searchMe):
            print("Found a match!")
            # re.findall expects two args, a pattern, then a place to search
            #num_results =len(re.findall(re.search(searchFor, searchMe)))
            num_results =len(re.findall(searchFor, searchMe))
            print(num_results)
        else:
            print("No Match!")
    except KeyboardInterrupt:        
        print('Have a good day')
        break


