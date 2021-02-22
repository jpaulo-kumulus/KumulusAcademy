import requests
#from PIL import Image
#from StringIO import StringIO
#r = requests.get('https://github.com/timeline.json') ##Objeto do tipo response
#r = requests.post("http://httpbin.org/post") ##Requisição http post
##A seguir, será mostrado vários tipos de requisições HTTP:
#r = requests.put("http://httpbin.org/put")
#print(r)
#r = requests.delete("http://httpbin.org/delete")
#print(r)
#r = requests.head("http://httpbin.org/get")
#print(r)
#r = requests.options("http://httpbin.org/get")
#rint(r)

#é possível passar parâmetros para os requests

#payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.get("http://httpbin.org/get", params=payload)
#rint(r)
#rint(r.url) 

#nome = input('Users name: ')
#r = requests.get('https://api.github.com/users/repos')
#print(r.text)
#print(r.status_code)   
#print(r._content)
#print(r.encoding) ##Descobrir o tipo de decodificação
#print(r.content) ##Resposta binária
#print(r.json()) ##Pode retornar um erro! Irá apresentar o código 401
#print(r)

#r = requests.get('https://api.github.com/users/repos', stream=True)
#print(r.raw)
#print(r.raw.read(10))

#url = 'https://api.github.com/users/repos'
#payload = {'some': 'data'}
#headers = {'content-type': 'application/json'}
#r = requests.post(url, data=json.dumps(payload), headers=headers)

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.headers)

r = requests.get('https://api.github.com/users/repos')
print(r.status_code)
print(r.headers)
print(r.url)
