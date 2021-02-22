import requests
import json

def git_user():
    site_r = 0
    site_r_convertido = '0'
    while site_r_convertido != True:
        username = input('Digite seu usuário do GitHub: \n')
        site_r = requests.get(f'https://api.github.com/users/{username}/repos')
        site_r_convertido = json.loads(site_r.text)
        if site_r.status_code != 404:
            for value in site_r_convertido:
                print('repo: '+value['html_url'] +' ID: ' +str(value['id']))
            break

git_user()