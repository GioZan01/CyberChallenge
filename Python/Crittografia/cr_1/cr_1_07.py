#!/usr/bin/python3

import string
import base64

#from secret import KEY

def encrypt(clear, key):
  enc = []
  for i in range(len(clear)):
    key_c = key[i % len(key)]
    enc_c = chr((ord(clear[i]) + ord(key_c)) % 128)
    enc.append(enc_c)
  return str(base64.urlsafe_b64encode("".join(enc).encode('ascii')), 'ascii')


# For debug purpose
def decrypt(enc, key):
    dec = []
    enc = str(base64.urlsafe_b64decode(enc.encode('ascii')), 'ascii')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((128 + ord(enc[i]) - ord(key_c)) % 128)
        dec.append(dec_c)
    return "".join(dec)
    '''
assert(len(KEY) == 8)
assert(all(c in string.ascii_lowercase for c in KEY))


print("flag: CCIT{%s}" % KEY)

k1 = KEY[0:4]
k2 = KEY[4:8]

m = "See you later in the city center"
d = encrypt(m, k1)
c = encrypt(d, k2)

print("Message:", m)
print("Ciphertext:", c)


'''
m = "See you later in the city center"
c = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="

cifrari=dict()
caratteri=string.ascii_lowercase

def get_keys_by_value(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]



for car in caratteri:
	for car1 in caratteri:
		for car2 in caratteri:
			for car3 in caratteri:
				key=car+car1+car2+car3
				st=encrypt(m, key)
				cifrari[key]=st
for car in caratteri:
	for car1 in caratteri:
		for car2 in caratteri:
			for car3 in caratteri:
				key=car+car1+car2+car3
				st=decrypt(c, key)
				if st in cifrari.values():
					flag=get_keys_by_value(cifrari, st)+key 
					print(flag)
					print("flag: CCIT{%s}" % flag)
