#SET DE UMA FUNÇÃO QUE FALA OI MUNDO
# def say_hello():
#   print('Hello World!')
# say_hello()

#SET DE UMA FUNÇÃO QUE ESPERA UM INPUT NA CHAMADA E COLOCA O INPUT
# def say_hello(name):
#   print(f'Hello {name}!')
# say_hello(input())

#SET DE UMA FUNÇÃO QUE JÁ TEM DEFINIDO O PARÂMETRO, E CASO VOCÊ COLOQUE PARÂMETROS NA CHAMADA ELA SUBSTITUI A DEFAULT
# def say_hello(name='World'):
#   print(f'Hello {name}!')

# say_hello()
# say_hello(input())
# say_hello('Bob')

##SET DE UMA FUNÇÃO COM PARÂMETROS DEFINIDOS, NO SEGUNDO PARÂMETRO CASO NÃO HAJA NADA, ELE MANTÉM O PRINT DO IF
#CASO NA CHAMADA DA FUNÇÃO SE USE O PARÂMETRO GREETING = QUALQUERCOISA, ELE PRINTA O QUALQUER COISA
# def say_hello(name='World', greeting=None):
#   if greeting == None:
#     print(f'Hello {name}!')
#   else:
#     print(f'{greeting} {name}!')

#say_hello(input())
# say_hello()
# say_hello('Bob')
# say_hello(greeting='Howdy')
# say_hello('Bob', 'Howdy')

#MOSTRA QUE CASO HAJA RETORNO DE OPERAÇÕES ENTRE VARIÁVEIS, ELA É IGNORADA SE NÃO FOR CAPTURADA EM UMA VARIÁVEL
# def add_two_numbers(x, y):
#     return x + y

# add_two_numbers(4, 6)
# result = add_two_numbers(5, 7)
# print(result)

#CAPTURA TODA A FUNÇÃO EM UMA VARIÁVEL (deck = []), ASSIM QUANDO A FUNÇÃO É CHAMADA ELE MOSTRA O CONTEÚDO DA VARIAVEL (deck = []) QUE É PARA ONDE O RETORNO APONTA
# def create_deck():
#   suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
#   ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#   deck = []

#   for  suit in suits:
#     for rank in ranks:
#       deck.append(f'{rank} of {suit}')

#   return deck

# my_deck = create_deck()
# print(len(my_deck))

#MOSTRA QUE UMA CHAMADA DE VARIAVEL NÃO PUXA A VARIAVEL DE DENTRO DE UMA FUNÇÃO, UMA NOVA VARIAVEL TEM DE SER CRIADA ATRIBUINDO A FUNÇÃO
#ESSA NOVA VARIAVEL PODE SER USADA PARA CHAMAR A FUNÇÃO
# value = 1
# def some_function():
#     value = 10
#     return value
# print(value)
# some_function()
# print(value)
# new_value = some_function()
# print(new_value)