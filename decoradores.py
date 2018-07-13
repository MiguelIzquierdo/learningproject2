def decorador(is_valid):

    def _decorador(funcion): #A (B)

        def before_action():
            print('Se ejecutará la función')

        def after_action():
            print('La funcioón se ha ejecutado')

        def nueva_funcion(*args, **kwargs):
            if is_valid:
                before_action()#Agregue código (X ejemplo abrir conex. base de datos)

            resultado = funcion(*args, **kwargs) #Funcion a ejecutar

            after_action()
            return resultado
        return nueva_funcion #C
    return _decorador

@decorador(is_valid=True)
def suma(num_uno, num_dos):
    return num_uno + num_dos

resultado = suma(10, 20)
print(resultado)


#A B y C son funciones
#A recibec omo parametro B para poder crear C
#Funcional final=C