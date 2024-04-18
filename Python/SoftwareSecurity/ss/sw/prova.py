
from pwn import *

def estrai_valori(data):

	#print(f"words-----{data}--------")
	frasi=data.split(" ")
	
	codifica=frasi[8].split("-")[0]
	valore=frasi[5]
	
	return (int(codifica), valore)
	
	
def res(n, valore):
	if n==32:
		return p32(int(valore, 16))
	return p64(int(valore, 16))
	
	
def main():
	codifica=
	valore=
	s=res(codifica, valore)
	print(f"parametri: {codifica} {valore}\n")
	print(f"risultato: {s}\n")


if __name__ == "__main__":
    main()
