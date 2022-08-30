"""
Actividad Criptología
29/08/2022

Marco Torres 
Fernando Valdeón 

"""
from ceasar_cypher.ceasar import *
from vigenere.vigenere import *
from one_time_pad.one_time_pad import *
from ceasar_cypher.decrypt_file import decryptFileCeasars 


# Menú
option = -1
while option != 0:

  print("\n\n--- ENCRYPTIONS --- ")
  print("Choose an option: ")
  print("1. Cesar")
  print("2. Vigenere")
  print("3. One Time Pad")
  print("4. Cesar Decrypt File")
  print("5. Cifrado del Cesar")
  print("0. End")
  option = int(input("Option: "))

    
  if option == 1:
    cesar_main()
  elif option == 2:
    vigenere_main()
  elif option == 3:
    one_time_pad_main()
  elif option == 4:
    decryptFileCeasars()
  elif option == 5:
    print("Cifrado del Cesar")
  elif option == 0:
    continue
  else:
    print("\nOpción incorrecta")
    continue

  input("\nEnter to continue")

# print("VIGENERE CYPHER")
# key = 'abct lpety'
# print(f"Orginal message: {message}")
# encryptedCode = encryptMessageWithVigenereMethod(key, message)
# print(f"Encripted message: {encryptedCode}")
# decryptedMessage = decryptMessageWithVigenereMethod(key, encryptedCode)
# print(f"Decrypted message: {decryptedMessage}")
# print("__________________________________________________________________________")

# print("\n")
# print("Plain text of encrypted file 1: ")
# decryptFileCeasars()
# print("__________________________________________________________________________")


# print("\n")
# print("One time Pad ")
# print(oneTimePad("hola mundo"))