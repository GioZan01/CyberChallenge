#!/usr/bin/env python3

import requests

url_1 = 'http://web-06.challs.olicyber.it/token'
url_2='http://web-06.challs.olicyber.it/flag'

s = requests.Session()

s.get(url_1)
r = s.get(url_2)

print(r.text)

