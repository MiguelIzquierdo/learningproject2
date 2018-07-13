def crear_funcion(num_uno, num_dos):
    def validacion():
        return num_uno > 0 and num_dos > 0

    return validacion()


prueba = crear_funcion(10,9)
print(prueba)