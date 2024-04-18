#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *

	
def main():
	HOST = "piecewise.challs.cyberchallenge.it"
	PORT = 9110
	r = remote(HOST, PORT)
	
	while True:
		data = r.recv()
		data=str(data)
		data=data.split(" ")
		print(f"{data}\n")
		if data[4] == "empty":
			r.sendline()
			
			print(f"{data}\n")
		else:
			codifica=data[8].split("-")[0]
			valore= data[5]
			endianess=data[9].split("-")[0]
			context.endian=endianess
			if codifica=="32":
				print(f"codifica: {codifica}, valore: {valore}, endianess: {endianess},\n")
				s=p32(int(valore))
				print(f"risultato: {s}\n")
			else:
				print(f"codifica: {codifica}, valore: {valore}, endianess: {endianess}\n")
				s=p64(int(valore))
				#print(f"parametri: {codifica} {valore}\n")
				print(f"risultato: {s}\n")
			r.send(s)
	
		data=r.recv()
		print(data)
	r.interactive()
	# chiude la socket
	# permette di interagire con la connessione direttamente dalla shell


	r.close()

if __name__ == "__main__":
	main()
