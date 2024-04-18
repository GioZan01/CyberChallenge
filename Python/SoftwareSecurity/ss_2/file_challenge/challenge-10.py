#!/usr/bin/env python3

import signal
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

TIMEOUT = 300

assert("FLAG" in os.environ)
flag = os.environ["FLAG"]
assert(flag.startswith("CCIT{"))
assert(flag.endswith("}"))

key = os.urandom(16)

def handle():
    while True:
        print("1. Register")
        print("2. Login")
        print("0. Exit")
        choice = int(input("> "))
        if choice == 1:
            name = input("Insert your username: ")
            if ";" in name:
                continue
            cookie = f"usr={name};is_admin=0".encode()
            iv = os.urandom(16)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            encrypted = cipher.encrypt(pad(cookie, 16))
            print(f"Your login token: {iv.hex()+encrypted.hex()}")
        elif choice == 2:
            token = input("Insert your token: ")
            try:
                cookie = bytes.fromhex(token[32:])
                iv = bytes.fromhex(token[:32])
                cipher = AES.new(key, AES.MODE_CBC, iv)
                pt = unpad(cipher.decrypt(cookie),16)
                values = pt.split(b";")
                user = values[0].split(b"=")[-1].decode()
                print(f"Welcome back {user} {values[1].decode()}")
                if b"is_admin=1" in values:
                    print(f"Here is your flag {flag}")
            except:
                print("Something is wrong with your token.")


if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()