
msg="TCICmI_{_d343_m4}s!s"
flag=""

for i in range(len(msg)//4):
	m = msg[i*4:i*4+4]
	flag += m[3]
	flag += m[1]
	flag += m[2]
	flag += m[0]
	
	
print("flag: ", flag)
