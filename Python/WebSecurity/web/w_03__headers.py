#!/usr/bin/env python3

import requests

param={"id":"flag"}

url = 'http://web-03.challs.olicyber.it/flag'
header = {'X-Password': 'admin'}

r=requests.get(url, headers=header)
print(r.text)
