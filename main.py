"""
Actividad Criptología
29/08/2022

Marco Torres 
Fernando Valdeón 

"""
from ceasar_cypher.ceasar import *
from vigenere.vigenere import *
from one_time_pad.one_time_pad import *
from ceasar_cypher.decrypt_file import * 
from vigenere.decrypt_file import * 


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
    decryptFileVigenere()
  elif option == 0:
    continue
  else:
    print("\nOpción incorrecta")
    continue

  input("\nEnter to continue")
