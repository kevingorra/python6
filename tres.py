contador=0
print("Enamorate De Antioquia")
print("Menu")
print("1. Agregar Pueblos")
print("2. Mostrar Rutas")
print("3. Salir")
pueblos=[]
while(contador!=3):
    pueblo={}
    contador=int(input("Digita una opcion"))
    if(contador==1):
        print("Agregando Pueblo")
        pueblo['nombre']=input("ingrese el nombre del pueblo")
        pueblo['distancia']=int(input("ingrese la distancia del pueblo"))
        pueblo['poblacion']=int(input("ingrese el numero de habitantes"))
        pueblos.append(pueblo)
    elif(contador==2):
        print("Distancia")
        print(pueblos)
    elif(contador==3):
        print("Saliendo")
        break
    else:
        print("Opcion no valida")

