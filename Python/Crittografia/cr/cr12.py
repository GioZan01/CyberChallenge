 #Diffie-Hellman. e logaritmi discreti 
''' oppure

from Crypto.Util.number import inverse

base = 2
modulo = 13
target = 5

result = inverse(base, modulo)
logarithm = (target * result) % modulo
print("Logaritmo discreto:", logarithm)
'''

from sympy.ntheory import discrete_log

def log_disc(base, modulo, target):
	result = discrete_log(modulo, target, base)
	return result

print(log_disc(2,53,39))


#Diffie-Hellman.
p=107
g=2
#send_A=g^numero_scelto_da_A mod p
send_A=29
 
#send_B=g^numero_scelto_da_B mod p
numero_scelto_da_B=71
#quindi send_B 
send_B=pow(g,numero_scelto_da_B,p)
print(f"La mia chiave pubblica è: {send_B}")
 
# chiave condivisa sarà send_A^numero_scelto_da_B 
# ovvero anche chiave condivisa sarà send_B^numero_scelto_da_A
#ovvero anche chiave condivisa sarà g^(numero_scelto_da_A*numero_scelto_da_B) mod p
#hanno una chiave condivisa senza aversela scambiata

key_shared=pow(send_A,numero_scelto_da_B,p)
print(f"Chiave condivisa: {key_shared}")
 
 
