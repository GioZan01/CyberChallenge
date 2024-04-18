#!/usr/bin/env python3

import signal
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long
import os

TIMEOUT = 300

assert("FLAG" in os.environ)
flag = os.environ["FLAG"]
assert(flag.startswith("CCIT{"))
assert(flag.endswith("}"))

otp = os.urandom(8)

def xor(a, b):
    return bytes([a[i % len(a)] ^ b[i % len(b)] for i in range(max(len(a), len(b)))])

def encrypt_des(text, key):
    try:
        key = bytes.fromhex(key)
        text = xor(bytes.fromhex(text), otp)
        cipher = DES.new(key, DES.MODE_ECB)
        ct = xor(cipher.encrypt(pad(text, 8)), otp)
        return ct.hex()
    except Exception as e:
        return f"Something went wrong: {e}"


def handle():
    while True:
        print("1. Encrypt text")
        print("2. Encrypt flag")
        print("0. Exit")
        choice = int(input("> "))
        if choice == 1:
            text = input("What do you want to encrypt (in hex)? ").strip()
            key = input("With what key (in hex)? ").strip()
            print(encrypt_des(text, key))
        elif choice == 2:
            key = input("What key do you want to use (in hex)? ").strip()
            print(encrypt_des(flag.encode().hex(), key))
        else:
            break


if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()
