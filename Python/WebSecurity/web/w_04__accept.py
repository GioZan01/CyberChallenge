#!/usr/bin/env python3

import requests

param={"id":"flag"}

url = 'http://web-04.challs.olicyber.it/users'
header = {'Accept': 'application/xml'}

r=requests.get(url, headers=header)
print(r.text)
