#!/usr/bin/env python3

import signal
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

def xor(a, b):
    return bytes([a[i % len(a)] ^ b[i % len(b)] for i in range(max(len(a), len(b)))])


def decrypt_des(text, key):
    try:
        key = bytes.fromhex(key)
        text = bytes.fromhex(text)
        cipher = DES.new(key, DES.MODE_ECB)
        ct = cipher.decrypt(text)
        return ct.hex()
    except Exception as e:
        return f"Something went wrong: {e}"
    
if __name__ == "__main__":
    print(decrypt_des("0adbb129b7ddc5fc44fd483c40e02d2d9435c5ff53d51013721b098e2c506043", "0101010101010101"))
    