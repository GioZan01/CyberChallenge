#!/usr/bin/env python3

import requests

url_1 = 'http://web-10.challs.olicyber.it/'


r = requests.put(url_1)

print(r.headers)

