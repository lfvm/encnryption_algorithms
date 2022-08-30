"""

Activad cripologia
29/08/2022

Marco Torres 
Fernando Valdeon 


1. Implementa el cifrado y descifrado del cesar. Se recomienda que tu programa pueda recibir una letra a usar como llave y un mensaje a encriptar/descrifrar.


2. Implementa el cifrado y descifrado de Vigenere.
Implementa un "one time pad". La función debe de generar la llave automaticamente cuando encripca y regresar la llave y el texto cifrado.


"""
from ceasar_cypher.ceasar import *
from ceasar_cypher.decrypt_file import decryptFileCeasars 
from vigenere.vigenere import *
from one_time_pad.one_time_pad import oneTimePad

print("CESARS CYPHER")

message = "hola mundo"
key = "z"
print(F"Orginal message: {message}")

encryptedCode = encryptMessageWithCeasarMethod(key, message)
print(f"Encripted message: {encryptedCode}")

decryptedMessage = decryptMessageWithCeasarMethod(key, encryptedCode)
print(f"Decrypted message: {decryptedMessage}")
print("__________________________________________________________________________")
print("\n")

print("VIGENERE CYPHER")
key = 'abct lpety'
print(f"Orginal message: {message}")
encryptedCode = encryptMessageWithVigenereMethod(key, message)
print(f"Encripted message: {encryptedCode}")
decryptedMessage = decryptMessageWithVigenereMethod(key, encryptedCode)
print(f"Decrypted message: {decryptedMessage}")
print("__________________________________________________________________________")

print("\n")
print("Plain text of encrypted file 1: ")
decryptFileCeasars()
print("__________________________________________________________________________")


print("\n")
print("One time Pad ")
print(oneTimePad("hola mundo"))