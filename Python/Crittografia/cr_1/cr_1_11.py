#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


BLOCK_SIZE = 16
	
HOST = "padding.challs.cyberchallenge.it"
PORT = 9033
    
r = remote(HOST, PORT)

def xor(a,b):
	return bytes([x ^ y for x,y in zip(a,b)])
def main():
	data = r.recvuntil(b"What").decode()
	print(data)
	data=data.split("\n")[-2]
	print("dati iniziali: ", data)
	'''
 	IV = data[:32]
	IV = bytes.fromhex(IV)
	
	#Primo blocco
	print(data[32:64])
	a = single_block_attack(bytes.fromhex(data[32:64]))
	a = bytes(a)
	print(xor(a,IV))
    	
	
	#Secondo blocco
	print(data[64:96])
	a = single_block_attack(bytes.fromhex(data[64:96]))
	a = bytes(a)
	print(xor(a,bytes.fromhex(data[32:64])))
    '''
    #Terzo blocco
	print(data[96:128])
	a = single_block_attack(bytes.fromhex(data[96:128]))
	a = bytes(a)
	print(xor(a,bytes.fromhex(data[64:96])))				

#verifico 
def oracle(iv, blocco_da_decrypt):
	'''#print(blocco_da_decrypt)
	send=""
	for i in range(len(iv)):
		send += hex(iv[i])[2:].zfill(2)
	send+=blocco_da_decrypt
	'''
	#print("send", iv.hex()+blocco_da_decrypt.hex())
	r.sendlineafter(b"? ", iv.hex()+blocco_da_decrypt.hex())
	#print("send", (iv.hex()+blocco_da_decrypt.encode().hex()))
	data=str(r.recvline())
	#print("data", data)
	if "incorrect" in data:
		return False
	else:
		return True

def single_block_attack(blocco_da_decrypt):
    
	#creo un vettore di zeri della dimenzione del blocco
	zeroing_iv = [0] * BLOCK_SIZE
    
	#per ogni valore di padding
	for pad_val in range(1, BLOCK_SIZE+1):
    	
		padding_iv = [pad_val ^ b for b in zeroing_iv]
		
		for candidate in range(256):
			#inserisco il candidato 
			padding_iv[-pad_val] = candidate
			
			iv = bytes(padding_iv)
			#print(padding_iv)
			#print(candidate)
			if oracle(iv, blocco_da_decrypt):
				#verifico correttezza primo byte
				if pad_val == 1:
					padding_iv[-2] ^= 1
					
					iv = bytes(padding_iv)
					if not oracle(iv, blocco_da_decrypt):
						continue  # false positive; keep searching
				#print(hex(candidate^pad_val))
				break
		else:
			raise Exception("no valid padding byte found (is the oracle working correctly?)")

		zeroing_iv[-pad_val] = candidate ^ pad_val
		print(zeroing_iv)


	return zeroing_iv



if __name__ == "__main__":
	main()

