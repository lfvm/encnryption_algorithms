import random as r 

ALPHABET_TO_INDEX = {
    "a": 0,"b": 1,"c": 2,"d": 3,"e": 4,"f": 5,"g": 6,"h": 7,
    "i": 8,"j": 9,"k": 10,"l": 11,"m": 12,"n": 13,"o": 14,"p": 15,"q": 16,"r": 17,
    "s": 18,"t": 19,"u": 20,"v": 21,"w": 22,"x": 23,"y": 24,"z": 25, " ": 26
}

# Guardar en un diccionario el indice junto con su respectiva letra
INDEX_TO_ALPHABET = { 
    0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h",
    8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r",
    18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z", 26: " "
}

def encryptMessageWithCeasarMethod( key: str, message: str  ) -> str:


  
    #Variable a regresar
    result = ""
    keyIndex = ALPHABET_TO_INDEX[key]

    for letter in message:  
        
        

        originalIndex = ALPHABET_TO_INDEX[letter]
        newIndex = keyIndex + originalIndex
        if newIndex > 26:
          newIndex = newIndex - 27
          
        encryptedLetter = INDEX_TO_ALPHABET[newIndex]
        result = result + encryptedLetter


    return result

    
def decryptMessageWithCeasarMethod( key: str, encryptedMessage: str  ) -> str:

    #Variable a regresar
    result = ""
    keyIndex = ALPHABET_TO_INDEX[key]

    for letter in encryptedMessage:  

   

        encryptedIndex = ALPHABET_TO_INDEX[letter]
        orginalIndex = encryptedIndex - keyIndex
        if orginalIndex < 0:
          orginalIndex += 27
          
        originalLetter = INDEX_TO_ALPHABET[orginalIndex]
        result = result + originalLetter


    return result

