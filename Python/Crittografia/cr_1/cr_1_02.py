def trova_indice(lista, elemento):
    for i, sublist in enumerate(lista):
        try:
            # Cerca l'elemento nella sottolista
            index = sublist.index(elemento)
            # Se trovato, restituisce l'indice della sottolista e l'indice dell'elemento all'interno della sottolista
            return i, index
        except ValueError:
            # Se l'elemento non è presente nella sottolista corrente, continua con la successiva
            continue
    # Se l'elemento non è stato trovato in nessuna sottolista, restituisce None
    return None, None



matrix=[["P","L","A","N","E"],["T","C","B","D","F"],["G","H","I","K","M"],["O","Q","R","S","U"],["V","W","X","Y","Z"]]

msg="CGKRKRLANXBERXBHLGAUVSZMQODKGB"
flag=""

for i in range(len(msg)//2):
	coppia = msg[i*2:i*2+2]
	riga1, colonna1=trova_indice(matrix, coppia[0])
	riga2, colonna2=trova_indice(matrix, coppia[1])

	#prima regola in questo caso non serve (se lettere nella coppia uguali)
	
	if riga1==riga2:#prendo carattere successivo
	
		flag+=matrix[riga1][(colonna1-1)%5]
		flag+=matrix[riga2][(colonna2-1)%5]
	
	elif colonna1==colonna2:#prendo carattere subito in basso
		flag+=matrix[(riga1-1)%5][colonna1]
		flag+=matrix[(riga2-1)%5][colonna1]
	
	else: #prendo incrociate 
		flag+=matrix[riga1][colonna2]
		flag+=matrix[riga2][colonna1]
		
		
	
	
	
print("flag: ", flag)
