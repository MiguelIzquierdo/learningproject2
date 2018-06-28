#Los diccionarios son estructuras de datos, que permiten almacenar strings, listas, etc.

diccionario = {'a': True, 'e': "Esto es un string", (1,2): False, 'a': "False"} #Las claves deben ser inmutables
#Siempre tomará el ultimo valor indicado (a: False)
diccionario['c'] = "nuevo string" #Esto sirve para añadir/modificar valores de una clave a un diccionario

valor = diccionario['a'] #Obtenemos los valores de 'a'
valor = diccionario.get('z', False) #Si no encuentra z en diccionario devuelveme False #Recomendado

del diccionario['e'] #del nos ayuda a eliminar sin perder el valor inicial
print(diccionario)
print(valor)

llaves = list( diccionario.keys()) #objeto iterable #podemos hacerlo lista poniendo list()
valores = list(diccionario.values()) #guarda todos los valores como lista
valores = tuple(diccionario.values()) #guarda los valores como tuple

diccionario_dos = {'z': 23, 'w': 88}
#diccionario['z'] = diccionario_dos['z'] #Hará crecer nuestro diccionario con la llave z del dos.

diccionario.update(diccionario_dos) #De esta forma añadimos el diccionario dos al uno

#print(llaves)
#print(valores)
print(diccionario)