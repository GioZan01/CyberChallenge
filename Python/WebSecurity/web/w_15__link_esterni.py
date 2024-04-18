#!/usr/bin/env python3

import requests

url_1 = 'http://web-15.challs.olicyber.it/'


r = requests.get(url_1)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
r=soup.find_all("link")
url = 'http://web-15.challs.olicyber.it'
s=list()
for tag in r:
	s.append(url+tag.get("href"))
r=soup.find_all("script")

stringa=""
for tag in r:
	s.append(url+tag.get("src"))
	
	
for l in s:
	r=requests.get(l)
	stringa +=r.text
	print(r.text)
	
import re
# Utilizzare un'espressione regolare per cercare parole che contengono la parte specificata
pattern = r'\b\w*' + re.escape("flag{") + r'\w*\b'
parole_trovate = re.findall(pattern, stringa)

print("Parole trovate:")
for parola in parole_trovate:
    print(parola)

