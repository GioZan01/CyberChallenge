#!/usr/bin/env python3

import sys
sys.path.append("../..")  # Aggiunge il percorso della cartella superiore al percorso di ricerca di Python

import utils

cifrato="d6346c5b5889b3a1feb0e556055a5d718ba874ac416141eee3e2bdc03eb3af5c"
iv=cifrato[:32]
user=cifrato[32:]
print(iv)
print(user)

print()
print(iv[-4:-2])
print(user[-4:-2])

#faccio xor tra byte contenente lo zero cifrato e l'iv ottenendo lo zero 
modifica_bytes=utils.xor_hex(iv[-4:-2], hex(0))

#trovo valore iv tale che il valore sopra xorato con 1 mi restituisce il valore da mettere nell'iv
modifica=utils.xor_hex(modifica_bytes, hex(1))


new_token=iv[:-4]+modifica+iv[-2:]+user
print(new_token)
