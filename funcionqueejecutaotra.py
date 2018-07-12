def crear_funcion(num_uno, num_dos): #Closure
    def validacion():
        print("se ejecuta validacion")
        return num_uno > 0 and num_dos > 0
    return validacion()

def aplicar_funcion(func):
    func

nueva_funcion = crear_funcion(10, 9)
aplicar_funcion(nueva_funcion)