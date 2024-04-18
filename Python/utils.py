#Per importare tale modulo in sottocartelle
# Importa il modulo dalla cartella superiore
'''
import sys
sys.path.append("..")  # Aggiunge il percorso della cartella superiore al percorso di ricerca di Python
'''


def xor_hex(hex_0, hex_1):
	int_0=int(hex_0, 16)
	int_1=int(hex_1, 16)
	result_xor=int_0^int_1
	return hex(result_xor)[2:]
