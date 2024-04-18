import math

a = 170
b = 81

gcd = math.gcd(a, b)
print("Il GCD di", a, "e", b, "è", gcd)

x=0
y=0
prod=a*x+b*y

while (prod!=gcd):
	if prod>gcd:
		x-=1
		prod=a*x+b*y
		
	else:
		y+=1
		prod=a*x+b*y
print(f"x={x}, y={y}")

#inverso modulare
numero=104
modulo=183
j=0
for i in range(modulo):
	if (numero*i)%modulo==1:
		j=i
		print(f"i={i}")
if j==0:
	print("non trovato")

