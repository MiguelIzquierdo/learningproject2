
"""
while condicion:
    codigo
else:
    codigo
"""
contador = 0
bandera = [1, True]

while bandera:
    print(contador)
    contador +=1 #Aumentar el contador en 1
    """Podemos incluir conditions en medio de un while"""
    if contador == 5:
        print('Estamos en el numero 5')
    if contador == 6:
        continue #Continua con el contador
    if contador == 8:
        #break #Para el contador #No recomendado
        bandera = False #break  #Siempre que bandera sea true sigue el ciclo,
else:
    print("El while ha terminado")