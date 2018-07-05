def suma(valor_uno, valor_dos, valor_tres):
    return valor_uno + valor_dos + valor_tres

def division(valor_uno, valor_dos):
    return valor_uno / valor_dos

def multiplicacion(valor_uno, valor_dos = 10): #Podemos indicar 1 valor fijo #Solo si no viene el valor
    return valor_uno * valor_dos

def multiples_valores():
    return "String", 1, True, 25.6 #******

resultado = suma(10, 20, 30)
resultado = multiplicacion(valor_uno = 6, valor_dos = 15)
resultado2 = division(100, 10)
resultado3 = multiplicacion(10)
resultado4 = multiples_valores()

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)

"""def multiples_valores():
    return "String", 1, True, 25.6"""

"""resultado = multiples_valores() #Con esto declaramos que resultado será la funcion multiples multiples_valores

string = resultado[0]
entero = resultado[1]
boolean = resultado[2]
float = resultado[3]""" #podemos hacerlo de dos formas

string, entero, boolean, float = multiples_valores()

print(string)
print(entero)
print(boolean)
print(float)

def mostrar_resultado(funcion):
    print(funcion(6,8))

mi_variable = multiplicacion
mostrar_resultado(mi_variable)
