#!/usr/bin/env python3

import requests

url_1 = 'http://web-09.challs.olicyber.it/login'
payload={"username":"admin","password": "admin"}


r = requests.post(url_1, json=payload)

print(r.text)

