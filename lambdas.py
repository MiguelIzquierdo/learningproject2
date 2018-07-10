mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos

resultado = mi_funcion(50, 40)
print(resultado)


formato = lambda sentencia : '¿{}?'.format(sentencia)

resultado = formato('Puedes hacer esto una pregunta')
print(resultado)

no_valor = lambda : 10

resultado = no_valor()
print(resultado)