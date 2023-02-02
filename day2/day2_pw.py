
from collections import Counter

def checkIfValid(password, letter, min_range, max_range):
    counter = Counter(password)
    return min_range <= counter[letter] <= max_range 

def checkIfValid2(password, letter, index1, index2):
    return (password[index1] == letter) != (password[index2] == letter)



valid_pw = 0 

with open("passwords.txt", 'r') as file:
    for line in file.readlines():
        line = line.strip()
        policy,_ , password  = line.partition(":")  
        password = password.strip()     
        minRange,_ ,maxRange = policy.partition("-")       
        indx2 = int(maxRange.split(' ')[0])-1
        indx1 = int(minRange)-1 
        letter = policy[-1]
                
        if checkIfValid2(password,letter,indx1,indx2):
            print(f'letter = {letter} pw[{indx1}]={password[indx1]} pw[{indx2}]={password[indx2]} password={password}')
            valid_pw += 1 
    print(valid_pw)        