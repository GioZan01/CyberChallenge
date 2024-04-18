from Crypto.Cipher import AES
import binascii, sys
import string

caratteri=string.printable

KEY = "yn9RB3Lr43xJK2"
IV  = ""
msg = "AES with CBC is very unbreakable"
p1=msg[0:16].encode()
p2=msg[16:32].encode()

#print(bytes.fromhex("78c670cb67a9e5773d696dc96b78c4e0"))
#print(p2.hex())

def xor(s1,s2):
    byte_string1 = binascii.unhexlify(s1)
    byte_string2 = binascii.unhexlify(s2)

    # Esegui l'operazione XOR bit a bit tra i byte corrispondenti
    result_bytes = bytes(a ^ b for a, b in zip(byte_string1, byte_string2))

    # Converti il risultato in una stringa esadecimale
    result_hex = binascii.hexlify(result_bytes).decode()

    return result_hex

chiave_vera=''
cip1=''
for c1 in caratteri:
    for c2 in caratteri:
        new_key=KEY+c1+c2
        cipher = AES.new(new_key.encode(), AES.MODE_ECB)
        cipher_text = cipher.decrypt(bytes.fromhex("78c670cb67a9e5773d696dc96b78c4e0"))
        res=xor(bytes.hex(cipher_text),p2.hex())
        #print(res)
        if res.startswith("c5") and res.endswith("d49e"):
            #print(res)
            cip1=res
            chiave_vera=new_key

#print(cip1)

cipher = AES.new(chiave_vera.encode(), AES.MODE_ECB)
cipher_text = cipher.decrypt(bytes.fromhex(cip1))
res=xor(bytes.hex(cipher_text),p1.hex())
print(bytes.fromhex(res).decode())
