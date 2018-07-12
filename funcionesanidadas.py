"""def validacion(num_uno, num_dos):
    return num_uno > 0 and num_dos > 0 #Valida si ambos numeros son mayor a 0

def division(num_uno, num_dos):
    if validacion(num_uno, num_dos): #Llama a la otra funcion
        return num_uno / num_dos #Divide si la primera funcion se cumple

resultado = division(10,0)
print(resultado)"""


def division(num_uno, num_dos):
    def validacion():
        return num_uno > 0 and num_dos > 0

    if validacion():
        return num_uno / num_dos

resultado = division(10,5)
#print(resultado)

def crear_funcion(num_uno, num_dos): #Closure
    def validacion():
        print("se ejecuta validacion")
        return num_uno > 0 and num_dos > 0
    return validacion()

def aplicar_funcion(func):
    func

nueva_funcion = crear_funcion(10, -5)
aplicar_funcion(nueva_funcion)