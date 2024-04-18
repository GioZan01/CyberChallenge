
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

if __name__ == "__main__":

	ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"

	for i in range (2**8):
		flag=""
		i_byte=i.to_bytes(1, "big")
		for j in range(len(ciphertext)//2):
			#print(ciphertext[j*2:j*2+2])
			a = bytes.fromhex(ciphertext[j*2:j*2+2])
			flag+=bytes.hex(xor(a,i_byte))
		print(f"{i} --> {bytes.fromhex(flag)}")
