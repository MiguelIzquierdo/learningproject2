my_list = [9, 20, 25, 6, 8, 8.5, True]

my_list.append(6) #Añade el valor que viene entre parentesis
my_list.insert(1, "insert") #Añade el valor entre comillas en la posición indicada al principio.

my_list.remove(8) #Remueve los números indicados entre parentesi

print(my_list)
last_value = my_list.pop() #.pop Extra el ultimo valor, en este caso 6

print(my_list)
print(last_value)#Antes y despues
print(my_list[1]) #Me muestra la posición 1 de mi lista.

print("\n\n\n Lista 2") #Separo lista 1 de lista 2 para probar otros metodos y busquedas
list_one = [1,9,22,6,8,65]

list_one.sort(reverse = True) #Sort ordena, reverse revierte el orden

list_two = [25,26]
list_one.extend(list_two) #Añade la lista 2 al final de la lista 1
list_one.append(list_two) #Añade la lista 2 dentro a la lista 1 como nueva lista

print(list_one)

