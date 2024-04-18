from Crypto.Cipher import DES
from Crypto.Util.Padding import pad


print("DES")
print()
# Parametri forniti
key_hex = '75bfa79818d1aafb'
plaintext = 'La lunghezza di questa frase non è divisibile per 8'
padding_scheme = 'x923'

# Converti la chiave esadecimale in byte
key = bytes.fromhex(key_hex)

# Inizializza l'oggetto DES con la chiave e la modalità CBC
cipher = DES.new(key, DES.MODE_CBC)

# Applica lo schema di padding al plaintext
padded_plaintext = pad(plaintext.encode(), DES.block_size, style=padding_scheme)

# Cifra il plaintext
ciphertext = cipher.encrypt(padded_plaintext)

print("Ciphertext:", bytes.hex(ciphertext))

#iv è un array di inizizzazione randomico
iv_hex = bytes.hex(cipher.iv)
print("IV utilizzato:", iv_hex)



print()
print()
print("AES")
print()

import secrets

# Genera una chiave esadecimale casuale di 32 byte
key_esad = secrets.token_hex(32)

print("Chiave esadecimale generata:", key_esad)


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Chiave AES-256
chiave = bytes.fromhex(key_esad)

# Testo in chiaro
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'

# Converte il testo in chiaro in formato byte e applica il padding PKCS#7
plaintext = plaintext.encode('utf-8')
plaintext_padded = pad(plaintext, AES.block_size)

# Inizializzazione del vettore di inizializzazione (IV)
#iv = get_random_bytes(AES.block_size)
#print("IV utilizzato:", bytes.hex(iv))

# Cifra il testo
cipher = AES.new(chiave, AES.MODE_CFB, segment_size=24)
ciphertext = cipher.encrypt(plaintext_padded)
print("Testo cifrato: ", bytes.hex(ciphertext))

#iv è un array di inizizzazione randomico
iv_hex = bytes.hex(cipher.iv)
print("IV utilizzato:", iv_hex)



print()
print()
print("CHACHA20")
print()


from Crypto.Cipher import ChaCha20

# Chiave e testo cifrato forniti
key_hex = '60d68bdb369b54c16e1eec08e78ce093c763472d4b650f5ae090155eeff29326'
ciphertext_hex = '080b62959d4646fcfc827816967a04d318fdefc328e0ebdf508ad0a0'
nonce_hex = 'b8c222ad151e2357'

# Decodifica chiave, testo cifrato e nonce da esadecimale
key = bytes.fromhex(key_hex)
ciphertext = bytes.fromhex(ciphertext_hex)
nonce = bytes.fromhex(nonce_hex)

# Decifra il testo cifrato utilizzando ChaCha20
cipher = ChaCha20.new(key=key, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)

# Stampa il testo decifrato
print("Testo decifrato (ASCII):", plaintext.decode('utf-8'))
