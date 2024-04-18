import hashlib
 
# Definisci il messaggio
msg = 'hash_me_pls'
 
# Calcola l'hash SHA3-384 del messaggio
hash_value = hashlib.sha3_384(msg.encode()).hexdigest()
 
# Stampa l'hash SHA3-384 in formato esadecimale
print("SHA3-384(msg):", hash_value)
print()
 
import hashlib
import hmac
import binascii
 
# Definizione dei parametri
key_hex = '3270da2a288ed7474dd4432f9fdc4e481501a20fc26a33bd15fd4b11bbc3d04c'
msg = 'La mia integrità è importante!'
 
# Converti la chiave da esadecimale a binario
key = binascii.unhexlify(key_hex)
 
# Calcola l'HMAC utilizzando SHA-224
hmac_value = hmac.new(key, msg.encode(), hashlib.sha224).hexdigest()
 
# Stampa l'HMAC in formato esadecimale
print("HMAC(msg):", hmac_value)
print()
 
from asn1crypto import keys
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import binascii
 
# Chiave DSA in formato esadecimale
key_hex = '3082025d0201003082023606072a8648ce380401308202290282010100989437450bb9c1019ff5d07fc24ae45158b5e058a8d3b0ee4d17cef20868f3ce9eceea050f718cdfa1afb1339386a5dcce23dd3e2a824c5aa76f940b60ed054006443ee041216f848c9e5d9669d28ef7d4c8a84a54d98cb06a8149490f173d81e496b0e5ce7d720406307fef925e0257c35c774496be3c340d3297a816aaffb2ded7cfdbaf3edca460764d0cc6861876eeaf2fa70abcd4299de2f7537f1e95743269d1097b512b1ff736e5cf07abcb36e5dfb340c7e46272188d8d788eee766b311b2033845c7bcfb5e417369a5fc4338c30b143ade3d76abec4f02b5d4d98ed89254c8c1328b165ebc1a3cb7e9e9a58a8934bdb77673b28deee2404e1cc03f1021d00b25753ecbc199a77b41d6052810c1d05e45f81c8a57194e3bd770899028201010081819742ca56a234ed837a609c2e5fbc191ecc12abd037232eb255fd63fab9149a06bea0f504d4a5e1112ec8ef74dbaad749ec01ca0b552b7b4904ce65fe4b0283e9ea6fd3bc60351b6d9921e08bf82543a8622e3cdce25fcd28365f3009d1b8ead001f9183db88ac58b153cf271d8a69dfd42c681a29d09865e505cc7a3d796426bd9912adc2ef96b5d1df7bb82cbff2c5ee81f21bb1e515319c592bae3473d28e12f599784dcd8456befd993cb621e6ebfadba47000befd4e5a34a49d8ee54590a21ad3071ee120ebe27ef89003fc33f91c658fd7a4e7053fd0c175abc7c754cefbe9eb2855e9d49be52ca73609a96196a94dfd8a76ec76f6f06eb816d265b041e021c01ead3fdcfae911f7ab109763bafc019c9d1fd991e6ca211c14c49ff'
 
# Converti la chiave esadecimale in un oggetto di tipo bytes
key_bytes = binascii.unhexlify(key_hex)
 
# Converti la chiave esadecimale in un oggetto di tipo chiave ASN.1
key = keys.PrivateKeyInfo.load(binascii.unhexlify(key_hex))
 
# Estrai il parametro "p"
p = key['private_key_algorithm']['parameters']['p'].native
 
# Stampa il valore di "p"
print("p =", p)
 
# Carica la chiave DSA
private_key = serialization.load_der_private_key(
    key_bytes,
    password=None,
    backend=default_backend()
)
 
# Estrai il parametro "y"
y = private_key.public_key().public_numbers().y
 
# Stampa il valore di "y"
print("y =", y)
 
# Estrai il parametro "q"
q = private_key.private_numbers().public_numbers.parameter_numbers.q
 
# Stampa il valore di "q"
print("q =", q)
 
# Estrai il parametro "g"
g = private_key.private_numbers().public_numbers.parameter_numbers.g
 
# Stampa il valore di "g"
print("g =", g)

 
 
from sympy import randprime
 
# Genera un numero primo con esattamente 1497 bit
prime_number = randprime(2**(1852-1), 2**1852 - 1)
 
print("Numero primo con 1852 bit:", prime_number)
 
 
from sympy import isprime
 
def is_prime(n):
    return isprime(n)
 
print(is_prime(170593468423416674779785861226437189487008093996451569854098773928197635811254871512293256248333356726109287947543114206265008718682128027809385814966619669750660815143713437522644777089195259280288105109110453635165564205922287146175895800001505608494184703422086357549373911613586229637018176252275932534445))
