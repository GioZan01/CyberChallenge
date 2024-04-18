#!/usr/bin/env python3

import signal
from binascii import hexlify
from string import printable
from random import randint
from secret import FLAG
from Crypto.Cipher import AES

TIMEOUT = 300
BLOCK = 16

def pad(s):
  return s + (BLOCK - len(s) % BLOCK) * chr(BLOCK - len(s) % BLOCK)

def randkey():
  return "".join([printable[randint(0, len(printable)-8)] for _ in range(BLOCK)]).encode()

def handle():
  print("=====================================")
  print("=     Secure Password Encrypter     =")
  print("=     Now with secure padding!      =")
  print("=====================================")

  cipher = AES.new(randkey(), AES.MODE_ECB)

  while True:
    print("")
    try:
      password = input("Give me the password to encrypt:")
      password = pad(password + FLAG).encode()
      password = hexlify(cipher.encrypt(password)).decode()
      print("Here is you secure encrypted password:", password)
    except EOFError:
      break

if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()
