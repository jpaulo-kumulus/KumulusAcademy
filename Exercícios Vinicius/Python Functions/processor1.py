def process_numbers(nao_processado):
    lista_processada = []
    if isinstance(nao_processado, list) == False:
        return lista_processada
    
    for items in nao_processado:
        if isinstance(items, int):
            lista_processada.append(items)
        elif isinstance(items, str):
            if items.isnumeric():
                item_convertido = int(items)
                lista_processada.append(item_convertido)

    lista_processada.sort()        
    return lista_processada

def process_names(nao_processado):
    
    lista_processada = []
    
    if isinstance(nao_processado, list) == False:
        return lista_processada

    for items in nao_processado:
        if isinstance(items, str):
            if items.isnumeric() == False:
                lista_processada.append(items)
                
    lista_processada.sort()
    return lista_processada

