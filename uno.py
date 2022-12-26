numero=0
contador=0
numerosPares=[]
while(contador<10):
    numero=int(input("Digite un numero par :"))
    if(numero % 2==0):
        numerosPares.append(numero)
        contador=contador+1

for observador in numerosPares:
    print(observador)
    