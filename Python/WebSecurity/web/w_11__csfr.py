#!/usr/bin/env python3

import requests
import json

url_1 = 'http://web-11.challs.olicyber.it/flag_piece'
url_2='http://web-11.challs.olicyber.it/login'

payload={"username":"admin","password": "admin"}

s = requests.Session()

r = s.post(url_2, json=payload)
data=r.text
data= json.loads(data)


flag=""

for i in range(4):
	
	param1={"index":i, "csrf":data["csrf"]}
	cookie=r.cookies
		
	r=s.get(url_1, params=param1, cookies=cookie)
	
	print(r.text)
	
	data=r.text
	data= json.loads(data)
	
	flag += data["flag_piece"]
	
print (flag)

