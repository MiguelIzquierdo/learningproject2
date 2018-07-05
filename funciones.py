def factorial_numero(): #Crear una función en python #No usar espacios
    numero = 5
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    print(factorial)

factorial_numero() #Esto sería el print de una función (se puede repetir)


def factorial_cualquiern(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
   #print(factorial)
   return factorial

resultado = factorial_numer(4)
print(resultado)