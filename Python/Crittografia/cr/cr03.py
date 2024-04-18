'''
Possibili alternative possono essere l'esadecimale (come visto nella challenge precedente) o la base 64.

Un esempio di snippet in Python che decodifica una stringa in base 64:

#!/usr/bin/env python3
from base64 import b64decode
s = 'aGVubG8gOik='
print(b64decode(s))

In Python per convertire un oggetto bytes in un oggetto int è conveniente utilizzare la funzione int.from_bytes(b, endianness), ove b è il nostro oggetto bytes, mentre endianness è una stringa 'big' oppure 'little' che sta ad indicare in che ordine devono essere letti i byte di b: rispettivamente da sinistra verso destra e viceversa.

Per convertire un intero z in bytes puoi usare invece la funzione (z).to_bytes(n, endianness): n indica il numero di bytes da utilizzare per la conversione, seguendo l'ordine dato da endianness.
'''


'''
import math

numero_intero = 664813035583918006462745898431981286737635929725
byte_necessari = math.ceil(numero_intero.bit_length() / 8)
print("Numero di byte necessari:", byte_necessari)
'''


#!/usr/bin/env python3
from base64 import b64decode
str_da_base64="ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
flag=b64decode(str_da_base64)


str_da_intero=664813035583918006462745898431981286737635929725
flag+=(str_da_intero).to_bytes(20,"big")

#flag=bytes.fromhex(s)
print(flag)

