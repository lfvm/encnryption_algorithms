from vigenere.vigenere import *

ALPHABET_TO_INDEX = {
    "a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7,
    "i": 8,"j": 9,"k": 10,"l": 11,"m": 12,"n": 13,"o": 14,"p": 15,"q": 16,"r": 17,
    "s": 18,"t": 19,"u": 20,"v": 21,"w": 22,"x": 23,"y": 24,"z": 25, " ":  26
}

INDEX_TO_ALPHABET = { 
    0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h",
    8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r",
    18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z", 26 : " "
}

def decryptFileVigenere():

    print("\n--- Vigenere Decrypt File ---")

    # Leer archivo
    with open('./documents/cipher2.txt', 'r') as file:
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

    print(f"Most repeated letters: {mostRepeatedEncryptedLetters}")


    '''
    Tenemos la letra que más se repite de cada índice. Sabemos que el caractér que más se repite es
    el espacio, por lo que podemos decir que la letra más repetida de cada índice corresponde al espacio.
    y usamos eso para obtener las verdaderas letras de la llave
    '''
        
    keyLetters = []
    for encryptedLetter in mostRepeatedEncryptedLetters:
        # La letra más repetida corresponde al espacio
        encryptedLetterIndex = ALPHABET_TO_INDEX[encryptedLetter]
        keyLetterIndex = encryptedLetterIndex - 26 # El espacio es la última letram restamos su indice
        
        # Si la el nuevo indice se sale del abecedario
        if keyLetterIndex < 0:
          keyLetterIndex += 27 # Se suma el tamaño del abecedario para iterar
          
        keyLetter = INDEX_TO_ALPHABET[keyLetterIndex]
        keyLetters.append(keyLetter)

    print(f"Key letters: {keyLetters}")

    
    message = data[0:100] 
    key = ""

    # Creamos llave de misma longitud repitiendo las letras de la llave
    for i in range(len(message)):
        key += keyLetters[i % len(keyLetters)]

    # Desencriptamos
    result = decryptMessageWithVigenereMethod(key, message)
    print(f"Message: {result}")