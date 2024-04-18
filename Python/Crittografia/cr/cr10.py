#teorema cinese del resto 

#dati forniti 
m=[94,3,5,83,71]
a=[93,0,3,48,38]
m_inc=8309130

# inverso modulare
def inverso_modulare(numero, modulo):
	j=0
	for i in range(modulo):
		if (numero*i)%modulo==1:
			return i
	return 0

M=1
x=0
for e in m:
	M=M*e

for i in range(len(m)):
	Mi=M/m[i]
	Ni=inverso_modulare(Mi,m[i])
	x=x+a[i]*Mi*Ni
print (int(x))
print (int(x % M))

print (f"Risultato: {int(x % m_inc)}")
