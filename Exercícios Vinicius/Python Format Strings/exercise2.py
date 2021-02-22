#PRIMEIRA LETRA MAIUSCULA (MÉTODOS)
# message = str.capitalize('first message')
# print(message)
# message = 'second message'.capitalize()
# print(message)
# message = 'third message'
# print(message.capitalize())

#TUDO MINÚSCULO OU MAIÚSCULO
# message = 'hello world'
# print(message.lower())
# print(message.upper())

#TODA PRIMEIRA LETRA DE PALAVRA MAIÚSCULA
# message = message.title()
# print(message)

#TROCAR O CASE DAS LETRAS
# print(message.swapcase())

#CONTAR QUANTIDADE DE LETRAS EM UMA STRING
# location = 'Mississippi'
# print(location.count('s'))

#CONTAR QUANTAS LETRAS TEM NA STRING E DEVOLVE EM NUMEROS
# print(len('how many letters in this string?'))

#CHECAR SE A STRING TERMINA OU COMEÇA COM LETRA(S) 
# message = 'racecar'
# print(message.startswith('r'))
# print(message.startswith('a'))
# print(message.startswith('ra'))

# print(message.endswith('r'))
# print(message.endswith('a'))
# print(message.endswith('ar'))

#MOSTRA QUAL POSIÇÃO A LETRA ESTÁ NA STRING (COMEÇANDO DO 0)
# message = 'The quick brown fox jumps over the lazy dog'
# print(message.find('q'))
# print(message.find('t'))
# print(message.find('T'))

#RETIRA ESPAÇÕS EM BRANCO DA ESQUERDA, DIREITA OU AMBOS
# message = '    middle     '
# print('.' + message.lstrip() + '.')
# print('.' + message.rstrip() + '.')
# print('.' + message.strip() + '.')

#SUBSTITUI STRING POR OUTRA ESCOLHIDA
# message = 'brevity is the essence of wit'
# message = message.replace('essence', 'soul')
# print(message)

#ESPAÇAMENTO À DIREITA OU ESQUERDA (PODE ADICIONAR ALGO PARA PREENCHER)
# message = 'howdy'
# print(message.rjust(20))
# print(message.rjust(20, '-'))
# print(message.ljust(20))
# print(message.ljust(20, '-'))