list="54 00 00 00 c3 00 00 00 22 01 00 00 8b 01 00 00 df 01 00 00 44 02 00 00 b6 02 00 00 ea 02 00 00 5e 03 00 00 c3 03 00 00 22 04 00 00 8b 04 00 00 c0 04 00 00 1f 05 00 00 87 05 00 00 dc 05 00 00 49 06 00 00 aa 06 00 00 f8 06 00 00 57 07 00 00 cb 07 00 00 fb 07 00 00 5a 08 00 00 cc 08 00 00 ff 08 00 00 42 09 00 00 b7 09 00 00 09 0a 00 00 7c 0a 00 00 e1 0a 00 00 40 0b 00 00 a4 0b 00 00 d5 0b 00 00 4b 0c 00 00 b4 0c 00 00 22 0d 00 00 87 0d 00 00 ff ff ff ff"

valori=list.split(" ")

i=0
inp=""
param_3=0
while len(valori)>i:
	mem=int(valori[i],16)
	new_char=mem-param_3
	param_3+=new_char
	inp+=chr(new_char%256)
	i+=4
print(inp)
