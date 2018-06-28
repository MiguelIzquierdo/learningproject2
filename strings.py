my_string = "Hola Mundo!"
my_string = """Este string contiene saltos de línea
como puedes ver"""

course ="Python3"
name = "Miguel"

final_message = "Nuevo curso de "+ course + " por " + name #Forma 1 de juntar strings
final_message = "Nuevo curso de %s por %s" %(course, name) #Forma 2
final_message = "Nuevo curso de {} por {}".format(course, name) #Forma3

print(my_string)
print(final_message)