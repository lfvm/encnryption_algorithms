from vigenere import *

def decryptFileVigenere() -> str:

    # Leer archivo
    with open('../documents/cipher2.txt', 'r') as file:
        data = file.read().rstrip()

    # Crear una lista de listas con grupos de 4 letras
    groupsOf4Letters = []
    n = 4
    for index in range(0, len(data), n):
        groupsOf4Letters.append(data[index : index + n])

    # Crear 4 diccionarios para contar la repetición de letras en cada índice
    counters = [{}, {}, {}, {}]

    # Por cada grupo de 4 letras
    for group in groupsOf4Letters:

        # Por cada índice del 0 al 3
        for i in range(len(group)):

            # Contar la repetición de caracteres en cada índice
            if group[i] in counters[i]:
                counters[i][group[i]] += 1
            else:
                counters[i][group[i]] = 1


    # Obtener las letras que más se repitieron en los 4 índices
    mostRepeatedEncryptedLetters = []
    for i in range(4):
        maxValue = max(counters[i].values())

        for letter, amount in counters[i].items():
            if amount == maxValue:
                mostRepeatedEncryptedLetters.append(letter)


    '''
    Tenemos la letra que más se repite de cada índice. Sabemos que las letras que más se repiten en
    el Inglés son: " ", e, t y a. Por lo tanto podemos intuír que las letras que más se repitieron 
    en cada índice deben de representar algúna de esas letras.
    '''


    print(mostRepeatedEncryptedLetters)


decryptFileVigenere()