contador=0
empanadas=[]

print("1. Agregando Empanadas")
print("2. Mostrar Empanadas")
print("3. Salir")

while(contador!=3):
    ingredientes=[]
    empanada={}
    contador=int(input("Digite la opcion : "))
    if(contador==1):
        empanada['Nombre']=input("ingrese el nombre de la empanada : ")
        for i in range(3):
            ingredientes.append(input(f"digite el ingrediente {i+1} : "))
       
        empanada['ingredientes']=ingredientes
        empanada['precio']=int(input("ingrese el precio : $ "))
        empanadas.append(empanada) 
    elif(contador==2):
        print("mostrar Empanadas")
        print(empanadas)
    elif(contador==3):
        print("Salir")
        break
    else:
        print("opcion Valida")