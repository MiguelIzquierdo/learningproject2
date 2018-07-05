def palindromo():
    nuevo_valor = frase.replace(' ','') #Variables locales: Solo existen dentro de la función
    return nuevo_valor == nuevo_valor[::-1] #Esto nos regresa la cadena de carácteres al revés (Frase = Frase al revés)

frase = "anita lava la tina" #Variables Globales #A esto si puede acceder una función (Da igual si está antes o después)
resultado = palindromo()
print(resultado)

def valor_global():
    global variable_global
    variable_global = 'Cambiar valor'

variable_global = 'Esto es una variable global'
print(variable_global)

valor_global()
print(variable_global)