#!/usr/bin/env python3

##create a dictionary

switch = {"hostname": "sw1", "ip":"1.1.1.1", "version" : "2.0", "vendor" : "someone"}
print(switch)
print("Switch version is: ", switch["version"])

##fake key with get method

print(switch.get("lynx"))

##keys & values printed out

print(switch.keys())
print(switch.values())


