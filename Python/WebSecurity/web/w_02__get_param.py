#!/usr/bin/env python3

import requests

param={"id":"flag"}
r=requests.get("http://web-02.challs.olicyber.it/server-records", params=param)
print(r.text)
