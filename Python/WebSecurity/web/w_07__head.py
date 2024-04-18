#!/usr/bin/env python3

import requests

url_1 = 'http://web-07.challs.olicyber.it/'

r = requests.head(url_1)

print(r.headers)

