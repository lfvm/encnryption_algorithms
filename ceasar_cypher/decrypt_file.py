from ceasar_cypher.ceasar import decryptMessageWithCeasarMethod

def decryptFileCeasars():

    # Leer archivo
    with open('documents/cipher1.txt', 'r') as file:
        data = file.read().rstrip()

    # Por fuerza bruta obtener las combinaciones
    results = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        message = decryptMessageWithCeasarMethod(letter , data)
        results.append(message)

    # Mostrar una parte de los resultados
    print("\n--- Cesar Decrypt File ---")
    print("Results:")
    for i in range(len(alphabet)):
        print(f"{alphabet[i]}. {results[i][0:100]}")

    print("\nWe can see the correct key is 'k'")

