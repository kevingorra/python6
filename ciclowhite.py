# ciclo mientras
# variable de control

import math


i=0
numero1=0
numero2=0
#Menu
print("***MENU***")
print("1.Sumar")
print("2. Restar")
print("3. Raiz cuadrada")
print("4. Multiplicar")
print("Salir")

#programar la estructura  del ciclo mientras 


while(i!=5):
    i=int(input("digite una opcion del menu: "))
    if(i==1):
       numero1=int(input("digite el primer numero"))
       numero2=int(input("digite el primer numero"))
       resultado=numero1+numero2
       print("Su resultado es :",resultado)
    elif(i==2):
        numero1=int(input("digite el primer numero"))
        numero2=int(input("digite el primer numero"))
        resultado=numero1-numero2
        print("Su resultado es :",resultado)
    elif(i==3):
        numero1=int(input("digite el primer numero"))
        resultado= math.sqrt(numero1)
        print("Su resultado es :",resultado)
    elif(i==4):
        numero1=int(input("digite el primer numero"))
        numero2=int(input("digite el primer numero"))
        resultado=numero1*numero2
        print("Su resultado es :",resultado)
       
    elif(i==5):
        break
    else:
        print("salimos del ciclo")
  
