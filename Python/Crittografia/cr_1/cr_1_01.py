'''
import codecs

# Testo da trasformare
testo_originale = "Hello, World!"

# Applica ROT13 al testo
testo_rot13 = codecs.encode(testo_originale, 'rot_13')

print("Testo originale:", testo_originale)
print("Testo dopo ROT13:", testo_rot13)
'''



def rot(testo, key):
    risultato = ""
    for char in testo:
        # Controllo se il carattere è una lettera minuscola
        if 'a' <= char <= 'z':
            # Applica la trasformazione ROT13 alle lettere minuscole
            risultato += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        # Controllo se il carattere è una lettera maiuscola
        elif 'A' <= char <= 'Z':
            # Applica la trasformazione ROT13 alle lettere maiuscole
            risultato += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            # Se non è una lettera, aggiungi il carattere originale
            risultato += char
    return risultato

# Test dell'implementazione ROT13
testo_originale = "TTZK{Xrzlj_Alczlj_Trvjri}"
testo_rot = rot(testo_originale,0)
i=0
while testo_rot[0]!="C":
	i+=1
	testo_rot=rot(testo_originale,i)
	print("Testo dopo ROT13:", testo_rot)

