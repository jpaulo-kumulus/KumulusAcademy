print('Você quer continuar?')
continuar = input()
if continuar == "n" or continuar == "não" or continuar == "N" or continuar == "Não" or continuar == "NÃO":
    print('Saindo')
elif continuar == "s" or continuar == "sim" or continuar == "S" or continuar == "Sim" or continuar == "SIM":
    print('Continuando...')
    import time
    time.sleep(3)
    print('Pronto!')
else:
    print('Por favor tente novamente e responda com sim ou não')