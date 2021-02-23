usuario = input("Nome do usuário: ", )

import requests

url = 'https://api.github.com/users/' + usuario + '/repos'

r = requests.get(url)


all_text = r.text

list_text = all_text.replace('"name":', 'xxxxxx ').replace('"full_name":', 'xxxxxx')
list_text = list_text.split('xxxxxx')

count = 0
repos = []
numer = 0
for peces in list_text:
    count += 1
    if peces.count('"') > 2 or peces.count(",") > 1:
        count = count
    else:   
        numer += 1 
        peces = str(numer) + '°- ' + peces[2:-2] 
        repos.append(peces)

for i in repos:
    print(i)

