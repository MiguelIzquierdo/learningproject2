lista = [valor for valor in range(0, 101)] #Añadirá el valor a la lista
pass

# Añadira el valor ("x cosa") a la lista
lista = [valor for valor in range(0, 101) if valor % 2 == 0] #< Sacar los numeros pares (% = residuo)
#1-valor a agregar a lista
#2- un ciclo, for

tupla =tuple(valor for valor in range(0, 101) if valor % 2 != 0) #Tupla con numeros impares
print(tupla)

diccionario = { indice:valor for indice, valor in enumerate(lista)}
print(diccionario)