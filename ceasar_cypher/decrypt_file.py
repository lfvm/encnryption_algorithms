from ceasar_cypher.ceasar import decryptMessageWithCeasarMethod

def decryptFileCeasars() -> str:

    with open('documents/cipher1.txt', 'r') as file:
        data = file.read().rstrip()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message = decryptMessageWithCeasarMethod("k" , data)
    print(f"{message}")
    print("\n")
    print("_______________________________________________________________")



decryptFileCeasars()