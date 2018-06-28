course = "Curso"
my_string = 'Codigo Facilito!'

"""Metodos de formato""" #Otra forma de comentar
result = '{a} de {b}'.format(a=course, b=my_string)
result = result.lower()
#result = result.upper()
#result = result.title()


"""Metodos de busqueda"""
posicion = result.find("codigo") #Esto mostrará la posición por la que empieza la palabra "código" en nuestro string
count = result.count("c") #Cuantas veces se repite C

new_string = result.replace('c', 'x') #Reemplaza las C's por las X's
new_string = result.split(' ') #Me secciona mi string "result" en cada \space o el valor que indique entre parentesis


print(posicion)
print(result)
print(count)
print(new_string)
