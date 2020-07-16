#!/usr/bin/python3

def devicereboot(IPs):
    IPs = ['12.3.4.5', '32.45.6.5',' 3.6.6.6']
    for IP in[IPs]:
        print(f'Connecting to..{IP}')
        print('REBOOTING NOW')

IPs = ['12.3.4.5', '32.45.6.5',' 3.6.6.6']
print(devicereboot(IPs))

