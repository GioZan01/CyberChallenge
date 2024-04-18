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
db = {'admin': os.urandom(16).hex()}


def handle():
    while True:
        print("1. Register")
        print("2. Generate command tokens")
        print("3. Execute commands with token")
        print("4. See database")
        print("0. Exit")
        choice = int(input("> "))
        if choice == 1:
            name = input("Insert your username: ")
            if ":" in name:
                continue
            if name not in db:
                cookie = f"login_token:{name}".encode()
                iv = os.urandom(16)
                db[name] = iv.hex()
                cipher = AES.new(key, AES.MODE_CBC, iv)
                encrypted = cipher.encrypt(pad(cookie, 16))
                print(f"Your login token: {iv.hex()+encrypted.hex()}")
            else:
                print("Username already registered")
        elif choice == 2:
            token = input("Please give me your login token ")
            try:
                cookie = bytes.fromhex(token[32:])
                iv = bytes.fromhex(token[:32])
                cipher = AES.new(key, AES.MODE_CBC, iv)
                pt = unpad(cipher.decrypt(cookie), 16).decode()
                values = pt.split(":")
                if values[0] == "login_token":
                    print("Welcome back {}".format(values[1]))
                    command = bytes.fromhex(input(
                        "What command do you want to execute? "))
                    iv = bytes.fromhex(db[values[1]])
                    cipher = AES.new(key, AES.MODE_CBC, iv)
                    encrypted = cipher.encrypt(pad(command, 16))
                    print(f"Your command token: {iv.hex()+encrypted.hex()}")
                else:
                    print("It seems that this is not a login token.")
            except:
                print("Something went wrong")
        elif choice == 3:
            token = input("What do you want to do? ")
            try:
                cmd = bytes.fromhex(token[32:])
                iv = bytes.fromhex(token[:32])
                cipher = AES.new(key, AES.MODE_CBC, iv)
                pt = unpad(cipher.decrypt(cmd), 16)
                if pt == b"get_flag":
                    if iv == bytes.fromhex(db['admin']):
                        print(f"Here is your flag: {flag}")
                    else:
                        print("Only admin can see the flag.")
                else:
                    print("Nice command! But it seems useless...")
            except:
                print("Something went wrong")
        elif choice == 4:
            print(db)
        else:
            break


if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()
