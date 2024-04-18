#!/usr/bin/env python3

import requests

url_1 = 'http://web-13.challs.olicyber.it/'


r = requests.get(url_1)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

r=soup.find_all(class_="red")
s=""
for tag in r:
	s+=tag.string
print(s)

