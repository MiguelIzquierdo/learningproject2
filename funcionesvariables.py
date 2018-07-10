def palindromo():
    nuevo_valor = frase.replace(' ','') #Variables locales: Solo existen dentro de la función
    return nuevo_valor == nuevo_valor[::-1] #Esto nos regresa la cadena de carácteres al revés (Frase = Frase al revés)

frase = "anita lava la tina" #Variables Globales #A esto si puede acceder una función (Da igual si está antes o después)
resultado = palindromo()
print(resultado)

def valor_global(): #Tiene que quedar claro que est crea una función, pero aún no la ejecutas *
    global variable_global
    variable_global = 'Cambiar valor'

variable_global = 'Esto es una variable global'
print(variable_global)

valor_global() #* Aquí es cuando se ejcuta la funcion antes creada.
print(variable_global)


def crear_globalU(): #Crea una variable
    global nueva_variable
    nueva_variable = 'Esto es una variable global'

crear_globalU()
print(nueva_variable)

def mostrar_global():
    print(variable_global)

mostrar_global()