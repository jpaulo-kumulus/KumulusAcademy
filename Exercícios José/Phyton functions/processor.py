def process_numbers(myListOfData):
    auxVector = []
    auxAnswerVector = []
    if type(myListOfData) == list:
        for i in myListOfData:
            auxVector.append(f'{i}')
        auxVector.sort()
        ##print(auxVector)
        for k in auxVector:
            #print(k)
            #print(type(k))
            if k.isnumeric() == True:
                auxAnswerVector.append(f'{k}')
                #print(auxAnswerVector)
        return auxAnswerVector
    else:
        return auxVector

def process_names(myListOfData):
    auxVector = []
    auxAnswerVector = []
    if type(myListOfData) == list:
        for i in myListOfData:
            auxVector.append(f'{i}')
        auxVector.sort()
        #print(auxVector)
        for k in auxVector:
            #print(k)
            #print(type(k))
            if k.isnumeric() == False:
                auxAnswerVector.append(f'{k}')
                #print(auxAnswerVector)
        return auxAnswerVector
    else:
        return auxVector

