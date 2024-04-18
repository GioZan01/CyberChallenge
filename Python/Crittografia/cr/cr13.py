import sympy
'''
def find_safe_prime(bits):
    while True:
        # Genera un numero primo casuale con il numero desiderato di bit
        prime = sympy.randprime(2**(bits-1), 2**bits - 1)
        
        # Controlla se (prime - 1) / 2 è anche un numero primo
        candidate = (prime - 1) // 2
        if sympy.isprime(candidate):
            return prime, candidate

# Esempio di utilizzo: trovare un numero primo p e un numero q tale che (p-1)/2 sia primo
bits = 1024
p, q = find_safe_prime(bits)
print("Numero primo p con", bits, "bit:", p)
'''
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decifra_AES128_CBC(chiave, iv, ciphertext):
    # Crea un oggetto cipher per AES in modalità CBC
    cipher = AES.new(chiave, AES.MODE_CBC, iv)
    
    # Decifra il testo cifrato
    decrypted_text = cipher.decrypt(ciphertext)
    
    # Rimuovi il padding PKCS#7
    #decrypted_text_unpadded = unpad(decrypted_text, AES.block_size, segment_size=24)
    
    # Ritorna il testo decifrato come una stringa
    return decrypted_text


p=159049645727759363658402649709287195907649384194247689427061007849813898671705301535787398792493529346546286905512228283745301281778699916779079802422650673293039075283700019700312905338201780024198510224156808449944858080463339896427470389208253880706376987337227842618150446598821453827683436308719223274239

g=1111111111
public_key=pow(g,2,p)
print(public_key)
    
chiave_A="3072566229f54d4a61890f9663af256abd256e01947cd0e5065f3b041d1b9e68653e9907cbbe79a9177fb223fd6bd02087ee1f90aec67301a2b5d2373101af86423610fd24d3c8c7f8b9f19b810fa8f10af305874233a5d9f268b179317b83c262d1415a71e137ffa448510f29cd30cb342562e63edd8a3d38f7f6ed40814616"
key_shared=pow(int(chiave_A,16),2,p)
print(f"Chiave condivisa: {key_shared}")


#chiave=str(key_shared)[:32].encode()
chiave = str(hex(key_shared))[2:34]
iv=bytes.fromhex("053c597d2f985b4f8c39d5255ff25817")
msg=bytes.fromhex("8d409353ccc6e6336e850262f9a8bbb680fff081a343435ea800b3f90156b10800744fb3c596984b8f81d0cb5a8f44c0085c735f8ca35ff9da40ebd4c1ccf3a7")

testo_decifrato = decifra_AES128_CBC(bytes.fromhex(chiave), iv, msg)
print("Testo decifrato:", testo_decifrato)


