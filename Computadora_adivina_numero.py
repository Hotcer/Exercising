import random


def adivina_computadora(x):
    global prediccion
    print('========================')
    print('Bienvenido (@) al Juego ')
    print('========================')
    print(f'Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo...')

    limite_inferior = 1
    limite_superior = x
    respuesta = ''
    while respuesta != 'c':
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior

        respuesta = input(f'Mi prediccion es {prediccion}. Si es muy alta ingresa (A). Si es muy baja ingresa (B).'
                          f' Si es la correcta ingresa (C): Cual es tu Respuesta?:  ').lower()
        if respuesta == 'a':
            limite_superior = prediccion - 1
        elif respuesta == 'b':
            limite_inferior = prediccion + 1

    print(f'Siiii!!! La computadora adivino, el numero era {prediccion}')


adivina_computadora(5)
