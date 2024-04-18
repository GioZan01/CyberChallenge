#RSA

# inverso modulare
def inverso_modulare(numero, modulo):
	j=0
	for i in range(modulo):
		if (numero*i)%modulo==1:
			return i
	return 0

#seleziono due numeri primi 
p=7
q=17

#calcolo prodotto 
n=p*q
print(f"n: {n}")

#calcolo funzione di eulero phi(n)=(p-1)*(q-1)
phi_n=(p-1)*(q-1)
print(f"phi(n): {phi_n}")

#scelgo e: affinchè 1<e< phi(n) con e e phi(n) coprimi (ovvero  GCD(e,phi(n)=1))
e=13	#esso farà parte assieme ad n della chiave pubblica

#scelgo d: e*d mod phi(n) =1 con  0<=d<=n (d = e^−1 mod phi(n)
# quindi Determino d<n affinchè (e*d) mod phi(n) =1
#ovvero inverso modulare
d=inverso_modulare(e,phi_n) #farà parte della chiave privata
print(f"d: {d}")

#messaggio da cifrare
M=118

#chiave pubblica key={e,n}
#messaggio cifrato 
C=pow(M,e,n)
print(f"Messaggio cifrato: {C}")


#chiave privata key={d,n}
# messaggio decifrato 
M=pow(C,d,n)
print(f"Messaggio decifrato: {M}")

