import time
import random
#Mäng
#Martin Pettai, Artjom Vinogradov, Jass Õunapuu
#IT21


def print_menuu():    
    print (30 * "-" , "MENÜÜ" , 30 * "-")
    print ("[1] Uus mäng")
    print ("[2] Lae mäng")
    print ("[3] Vaata mängijat")
    print ("[4] Credits")
    print ("[5] Exit")
    print (67 * "-")
  
loop=True      
  
while loop:   
    print_menuu()   
    valik = int(input("Enter your valik [1-5]: "))
     
    if valik==1:     
        print ("Tere tulemast uude mängu!")
        ## You can add your code or functions here
    
    
    elif valik==2:
        print ("menuu 2 has been selected")
        ## You can add your code or functions here
    
    
    elif valik==3:
        print ("menuu 3 has been selected")
        ## You can add your code or functions here
    elif valik==4:
        print ("menuu 4 has been selected")
        ## You can add your code or functions here
        
    elif valik==4:
        print ("menuu 4 has been selected")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Vale valik, oled kindel, et vajutasid õiget klahvi?")
    