


def decryptFileCeasars() -> str:

    groupsOfwords = []
    with open('../documents/cipher2.txt', 'r') as file:
        data = file.read().rstrip()

    #crear una lista de listas con grupos de 4 letras
    counter = 0 
    group = ""
    for letter in data:

        if counter == 4:
            groupsOfwords.append(group)
            counter = 0
            group = ""
        else :
            counter +=1 
            group += letter

            


    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}

    for group in groupsOfwords:
        
        if group[0] in dict1:

            dict1[group[0]] += 1  
        else:
            dict1[group[0]] = 1


        if group[1] in dict2:

            dict2[group[1]] += 1  
        else:
            dict2[group[1]] = 1   

            
        if group[2] in dict3:

            dict3[group[2]] += 1  
        else:
            dict3[group[2]] = 1


        if group[3] in dict4:

            dict4[group[3]] += 1  
        else:
            dict4[group[3]] = 1

    


decryptFileCeasars()