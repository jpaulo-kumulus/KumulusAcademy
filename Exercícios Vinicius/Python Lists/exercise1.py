colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

#MOSTRAR O TIPO DAS LISTAS
# print(colors)
# print(type(colors))

#MOSTRANDO QUE O DADO DENTRO DA LISTA NÃO SE ALTERA AO MOSTRAR
# sundry = ['John', 3.14, 7, False]
# print(sundry)
# print(type(sundry))

#PRINTAR OU MANUSEAR DADO COM BASE EM [X:Y] SENDO X ONDE COMEÇA E Y ONDE TERMINA 
#(CASO X ESTEJA EM BRANCO, COMEÇA DO COMEÇO. CASO Y ESTEJA EM BRANCO, VAI ATÉ O FINAL)
#ALÉM DISSO VOCÊ PODE PERCORRER A LISTA AO CONTRÁRIO USANDO (-) ANTES DO INDEX
# print(f'0-based indexing into the list ... second item: {colors[1]}')
# print(f'Last item of the list: {colors[-1]}')
# print(f'Next to last item in the list: {colors[-2]}')
# print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
# print(colors[2:5])
# print(type(colors[2:5]))
# print('\nPrint a slice, starting at index 0 to index 3:')
# print(colors[:3])
# print('\nPrint a slice, starting a index 4 to the end of the list:')
# print(colors[4:])
# print('\nPrint a slice, from the 4th from the end (but not the last item):')
# print(colors[-4:-1])

#INVERTE A ORDEM DA LISTA E ORGANIZA (ORDEM ALFANUMERICA)
# colors.reverse()
# print(colors)
# colors.sort()
# print(colors)

#COMANDO POP QUE RETIRA UM ITEM DA LISTA
# print(colors)
# color = colors.pop(0)
# print('popped', color)
# print(colors)

#COMANDOS PARA ADICIONAR AO FIM DA LISTA OU REMOVER DA LISTA (REMOVE DE QUALQUER POSIÇÃO)
# print(colors)
# colors.append('black')
# colors.append('white')
# colors.remove('yellow')
# colors.remove('orange')
# print(colors)

#ADICIONA OUTRA LISTA AO FINAL DA ESCOLHIDA
# new_colors = ['lime', 'gray']
# colors.extend(new_colors)
# print(colors)

#LIMPA A LISTA
# print(colors)
# colors.clear()
# print(colors)