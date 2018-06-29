lista = (1,2,3,4,5,6,7,8,9,10,11,12,13,16)

for valor in lista: #Ciclo básico
    print(valor)



nuevo_rango = range(0,20,4) #Del 0 al 20 de 4 en 4
for valor in nuevo_rango:
    print(valor)

for valor in range(0,15,3): #Forma mas simple de hacerlo
    print(valor)





indice = 0
for valor in lista:
    print(valor, "tiene el indice", indice) #Nos muestra el indice (pos.) de cada valor
    indice +=1

for indice, valor in enumerate(lista): #Forma mas simple de hacerlo
    print(valor, "contiene el indice", indice)


for valor in range(0, len(lista)): #Me muestra la cantidad de elementos que tengo en la lista
    print(valor)

for valor in "Curso de código facilito":
    print(valor)

""" for valor in 123
        print(valor)""" #No funcionaria porque los números no son iterables
diccionario = {'a': 10, 'b': 20, 'c': 500}
for llave, valor in diccionario.items():
    print("la llave", llave, "tiene el valor de", valor)

#Añadir valores a una lista

lista = [] #False
for valor in range(0, 101):
    lista.append(valor)
print(lista)