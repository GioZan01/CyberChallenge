#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re

url_1 = 'http://web-16.challs.olicyber.it/'

r = requests.get(url_1)

i=0
page_da_visitare=[""]
tutte_le_page=list()
h1=list()

while not page_da_visitare or i == 0:
	i==1
	
	url=url_1+page_da_visitare.pop()
	
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	
	tag_h1=soup.find_all("h1")
	for tag in tag_h1:
		print(tag.string)
		h1.append(tag.string)


	tag_a=soup.find_all("a")
	for tag in tag_a:
		new=tag.get("href")
		if new not in tutte_le_page:
			page_da_visitare.append(new)
			tutte_le_page.append(new)
	#print("s")
	#print(len(page_da_visitare))
	
print(h1)
	
