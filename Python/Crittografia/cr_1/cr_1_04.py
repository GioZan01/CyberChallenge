#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *

	
	
def main():
    HOST = "padding.challs.cyberchallenge.it"
    PORT = 9030
    
    r = remote(HOST, PORT)
    fine=False
    caratteri=["C","I","T","r","m","3","b","t","h","e","_","{"]+list(string.punctuation)+list(string.digits)+list(string.ascii_letters)
    flag=""
    i=0
    while not fine:
    	data = r.recvuntil(b"encrypt")
    	#print(data)
    	s="1"*(31-i)

    	r.sendlineafter(b":", s.encode())
    	data = str(r.recvuntil(b"\n")).split(": ")[1]
    	#print(data)
    	
    	for car in caratteri:
    		#print(car)
    		st=s+flag+str(car)
	    	r.sendlineafter(b":", st.encode())
    		data_new = str(r.recvuntil(b"\n")).split(": ")[1]
    		
    		if data[32:64]==data_new[32:64]:
    			flag+=car
    			print("Flag:", flag)
    			if car=="}":
    				fine=True
    			break
    		#else:
    		#	print("No")
    	i+=1

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
