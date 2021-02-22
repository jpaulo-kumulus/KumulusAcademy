import requests
import json


print('Escolha um nome que voce deseja procurar: ')
userName = input()
requestGet = requests.get('https://api.github.com/users/'+ userName + '/repos')
print(requestGet)
if requestGet.status_code == 200:
    print('User has been found on their server')
    justString = requestGet._content
    response_json = json.loads(justString)
    for repository in response_json:
        print(repository['name'])
    exit()
else:
    print('Errooorr! User could be found on their server!')
    exit()


