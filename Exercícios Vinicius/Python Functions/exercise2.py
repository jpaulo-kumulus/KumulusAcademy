#ESSA FUNÇÃO DEFINE UMA LISTA DE ARGUMENTOS COM O PARTÂMETRO (*args) QUE QUANDO PRECISAR DE INTERAÇÃO PODE SER CHAMADA COM args
#LISTAS DE ARGUMENTOS ARBITRÁRIOS NÃO PODEM SER EDITADAS COMO UMA (list)
# def print_args(*args):
#   for arg in args:
#     print(f'arg = {arg}')
#     print(args)
#     print(type(args))

# print_args('a')
# print_args('a', 'b')
# print_args('a', 'b', 'c')

#ARGUMENTOS DE PALAVRA CHAVE USA-SE (**kwargs)
#A FUNÇÃO ESTÁ SENDO CHAMADA TRÊS VEZES, A CADA CHAMADA ELE PERCORRE OS ARGUMENTOS
#A FUNÇÃO PROCURA UMA PALAVRA CHAVE COM (kwargs.get()) E CASO ELA NÃO ACHE NO ARGUMENTO ELA ESTÁ SETANDO PARA NONE (portanto ignorando a chamada e argumento)
#CASO ACHE ELA PRINTA
# def print_keyword_args(**kwargs):

#   third = kwargs.get('third', None)
#   if third != None:
#     print('third arg =', third)


# print_keyword_args(first='a')
# print_keyword_args(first='b', second='c')
# print_keyword_args(first='d', second='e', third='f')

#(ARGS) É UM DICIONARIO OU (dict) QUE É SEMELHANTE A UMA LISTA
#MAS CADA ITEM DA LISTA TEM 2 PARTES: NOME(palavra chave de argumento(first))
#E valor (valor do argumento 'a')..

# def print_keyword_args(**kwargs):

#   print('\n')

#   for key, value in kwargs.items():
#     print(f'{key} = {value}')

#   third = kwargs.get('third', None)
#   if third != None:
#     print('third arg =', third)


# print_keyword_args(first='a')
# print_keyword_args(first='b', second='c')
# print_keyword_args(first='d', second='e', third='f')

#MESMA COISA QUE ACIMA PORÉM MOSTRANDO O TIPO DE DADO DE kwargs
# def print_keyword_args(**kwargs):

#   print('\n')
#   print(kwargs)
#   print(type(kwargs))

#   for key, value in kwargs.items():
#     print(f'{key} = {value}')

#   third = kwargs.get('third', None)
#   if third != None:
#     print('third arg =', third)


# print_keyword_args(first='a')
# print_keyword_args(first='b', second='c')
# print_keyword_args(first='d', second='e', third='f')



