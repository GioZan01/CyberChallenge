#!/usr/bin/env python3

import signal
import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

TIMEOUT = 300
BLOCK_SIZE = 16

assert("FLAG" in os.environ)
flag = os.environ["FLAG"]
assert(flag.startswith("CCIT{"))
assert(flag.endswith("}"))

key = os.urandom(BLOCK_SIZE)
iv = os.urandom(BLOCK_SIZE)

print("Hello! Here's an encrypted flag")
cipher = AES.new(key, AES.MODE_CBC, iv)
print(iv.hex()+cipher.encrypt(pad(flag.encode(), BLOCK_SIZE)).hex())


def handle():
    while True:
        try:
            dec = bytes.fromhex(
                input("What do you want to decrypt (in hex)? ").strip())
            cipher = AES.new(key, AES.MODE_CBC, dec[:BLOCK_SIZE])
            decrypted = cipher.decrypt(dec[BLOCK_SIZE:])
            decrypted_and_unpadded = unpad(decrypted, BLOCK_SIZE)
            print("Wow you are so strong at decrypting!")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()
