import random as r 

ALPHABET_TO_INDEX = {
    "a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7,
    "i": 8,"j": 9,"k": 10,"l": 11,"m": 12,"n": 13,"o": 14,"p": 15,"q": 16,"r": 17,
    "s": 18,"t": 19,"u": 20,"v": 21,"w": 22,"x": 23,"y": 24,"z": 25, " ": 26
}

INDEX_TO_ALPHABET = { 
    0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h",
    8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r",
    18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z", 26: " "
}

def encryptMessageWithCeasarMethod( key: str, message: str  ) -> str:
    # Variable a regresar
    result = ""
    keyIndex = ALPHABET_TO_INDEX[key] # Índice de la llave

    for letter in message:

        originalIndex = ALPHABET_TO_INDEX[letter] # Obtenemos el índice de la letra actual
        newIndex = keyIndex + originalIndex # Sumamos el indice de la llave para encriptar

        # Si la el nuevo indice se sale del abecedario
        if newIndex > 26:
          newIndex = newIndex - 27 # Se resta el tamaño del abecedario para iterar
          
        encryptedLetter = INDEX_TO_ALPHABET[newIndex]
        result = result + encryptedLetter

    return result

    
def decryptMessageWithCeasarMethod( key: str, encryptedMessage: str  ) -> str:
    # Variable a regresar
    result = ""
    keyIndex = ALPHABET_TO_INDEX[key] # Índice de la llave

    for letter in encryptedMessage: 
         
        encryptedIndex = ALPHABET_TO_INDEX[letter] # Obtenemos el índice de la letra actual encriptada
        orginalIndex = encryptedIndex - keyIndex # Restamos el índice de la llave para obtener letra indice original
        
        # Si la el nuevo indice se sale del abecedario
        if orginalIndex < 0:
          orginalIndex += 27 # Se suma el tamaño del abecedario para iterar
          
        originalLetter = INDEX_TO_ALPHABET[orginalIndex]
        result = result + originalLetter

    return result

def cesar_main():

    print("\n--- Cesar Cipher ---")

    message = "hola mundo"
    key = "k"

    print(f"Message: {message}")
    print(f"Key: {key}")

    encryptedCode = encryptMessageWithCeasarMethod(key, message)
    print(f"Encrypted: {encryptedCode}")

    decryptedMessage = decryptMessageWithCeasarMethod(key, encryptedCode)
    print(f"Decrypted: {decryptedMessage}")