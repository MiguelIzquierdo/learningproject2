def suma(*args):
    resultado = 0
    for valor in args:
        resultado = resultado + valor
    return resultado

resultado = suma(10, 50, 60,2,3,4,5,6)
print(resultado)

def diccionario(**kwargs):
    valor = kwargs.get('nombre1', 'No contiene valor')
    print(valor)

result = diccionario(nombre = 'Miguel', edad = 21)


* -> n valores -> tuplas
** -> n valores -> diccionarios

