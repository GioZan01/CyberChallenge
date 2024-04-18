
#bytes serve per gestire byte
#.hex() permette di ottenere una stringa esadecimale
#.fromhex() permette di ottenere da un esadecimale una stringa

s="666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
flag=bytes.fromhex(s)
print(flag)
