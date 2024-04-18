#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *

def somma(data):

	#print(f"words-----{data}--------")
	frasi=data.split("\\n")

	numb=[int(word.strip("[]")) for word in frasi[1].split(",")]
	#print(f"numb-----{numb}--------")
	return sum(numb)
	
def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)
    
    # .recv() riceve e ritorna al massimo 1024 bytes dalla socket
    data = r.recv()
    # .sendline() è identico a .send(), però appende un newline dopo i dati
    r.sendline(b"Ciao!")
    for _ in range(10):

	    data = r.recv()
	    '''
	    
	    print(f"ciaooooooo --{str(data)} --")
	    '''
	    s=somma(str(data))
	    #print(f"\n\n {data}\n\n")
	    print(f"sommaaaaa: {s}\n")

	    # .sendline() è identico a .send(), però appende un newline dopo i dati
	    r.sendline(str(s).encode())
	    
    # chiude la socket
    # permette di interagire con la connessione direttamente dalla shell
    r.interactive()

    r.close()


if __name__ == "__main__":
    main()
