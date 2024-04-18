#!/usr/bin/env python3
from pwn import *

exe = ELF("./sw-19")

if args.REMOTE:
	HOST = "nc software-19.challs.olicyber.it"
	PORT = 13002
    
	r = remote(HOST, PORT)
	
	p = remote(HOST, PORT)
else:
	p = process([exe.path])

# $ ./script.py REMOTE
# $ ./script.py

	
	
def main():

	data = p.recv()
	data = p.recv()
	p.send(b"C")
	print(data)
	for _ in range(20):
		
		data = p.recv()
		
		print(f"a****{str(data)}****\n")
		words=str(data).split()
		f=words[1].strip(":")
		print(f"b****{f}****")
		indirizzo=hex(exe.sym[f])
		print(f"c-indirizzo: {indirizzo}\n")
		p.sendline(indirizzo.encode())

		#print (r.recv())
		#print("finestep1\n\n")
	# chiude la socket
	# permette di interagire con la connessione direttamente dalla shell
	p.interactive()

	p.close()


if __name__ == "__main__":
    main()
