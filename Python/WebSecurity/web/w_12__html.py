#!/usr/bin/env python3

import requests

url_1 = 'http://web-12.challs.olicyber.it/'


r = requests.get(url_1)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

r=soup.find_all("p")
print(r[1])

