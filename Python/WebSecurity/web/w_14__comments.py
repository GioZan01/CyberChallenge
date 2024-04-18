#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from bs4 import Comment

url_1 = 'http://web-14.challs.olicyber.it/'


r = requests.get(url_1)

soup = BeautifulSoup(r.text, 'html.parser')

# Trovare tutti i commenti HTML
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

# Stampare i commenti trovati
for comment in comments:
    print(comment)
