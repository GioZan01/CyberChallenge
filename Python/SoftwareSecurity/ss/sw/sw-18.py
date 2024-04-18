#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *

def estrai_valori(data):
	#print(f"words-----{data}--------")
	#frasi=data.split("\n\n")
	#prima_frase=frasi[0]
	
	#p_f=prima_frase.split(" ")	
	p_f=data.split(" ")	
	
	codifica=p_f[8].split("-")[0]
	valore=p_f[5]
	
	return (codifica, valore)
	
	
def main():
    HOST = "software-18.challs.olicyber.it"
    PORT = 13001
    
    r = remote(HOST, PORT)
    
    data = r.recv()
    r.sendline(b"Ciao!")
    
    for _ in range(100):
        data = r.recv()
        print(f"ciaooooooo****{str(data)}****")
	    
        codifica, valore=estrai_valori(str(data))
        if codifica=="32":
            s=p32(int(valore, 16))
        else:
            s=p64(int(valore, 16))
        #print(f"parametri: {codifica} {valore}\n")
        #print(f"risultato: {s}\n")
	    
        r.send(s)

	    #print (r.recv())
	    #print("finestep1\n\n")
	    
    # chiude la socket
    # permette di interagire con la connessione direttamente dalla shell
    r.interactive()

    r.close()


if __name__ == "__main__":
    main()
