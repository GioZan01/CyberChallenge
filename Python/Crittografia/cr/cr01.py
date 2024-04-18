interi=[102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125]


# chr() converte da intero a carattere
# ord() fa il contrario
s=""
for i in interi:
	s+=chr(i)
print(s)
