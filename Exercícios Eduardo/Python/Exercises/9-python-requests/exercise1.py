import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)


print(r.url)

# *************************************************************************************
import requests
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)

# *************************************************************************************

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

# ambos 'x-test' e 'x-test2' são enviados
s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})

# *************************************************************************************
import requests
r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')

r.headers

# *************************************************************************************

#from requests import Request, Session

#s = Session()
#prepped = Request('GET',  # ou qualquer outro método, 'POST', 'PUT', etc.
#                  url,
#                  data=data
#                  headers=headers
#                  # ...
#                  ).prepare()
# faça algo com prepped.body
# faça algo com prepped.headers
#resp = s.send(prepped,
#              stream=stream,
#              verify=verify,
#              proxies=proxies,
#              cert=cert,
#              timeout=timeout,
#              # etc.
#              )
#print(resp.status_code)

# ************************************************************************************

