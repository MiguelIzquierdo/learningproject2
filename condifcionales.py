fruta = 'kiwi'

#Estructura: if condicion : \Salto de línea\
#\tab\ código


if fruta == 'kiwis' : #Conds: >  <  >=  <=  !=(dif)  ==
    print("El valor es kiwi")

elif fruta == 'manzana': #Un else con condición que puede repetirse n veces.
    print('Es una manzana')

elif fruta == 'pera':
    print('Otra fruta')

elif fruta == 'platano':
    pass #Esto sirve cuando podemos tener una condicion que no sepamos que ejecutará, si no ponemos pass, petará el archivo.

else:
    print('No son iguales')

#True=1
#False=0

'''if True:
    print('Es verdad') ''' #Esto devolverá 'Es verdad' debido a que True siempre es 1

#Todas las variables que tengan valor seran 1 y las vacias seran 0
#Ejemplo:

valor = '' #Tambien podemos poner None (Significa que no es una lista, ni una strnig, etc...) Valor = None

if valor:
    print('Es verdad')
else:
    print('No es verdad')

valor2 = 21

if valor and valor2 > 20: #Si ponemos or and vez de and, con que 1 se cumpla, dará True
    print('Es verdad')
else:
    print('Es mentira') #En este caso se tendrán que cumplir las dos

#Otra forma de condicionar no recomendada:
#mensaje = 'El valor es kiwi' if fruta == 'kiwi' else 'No son iguales'
#print(mensaje)