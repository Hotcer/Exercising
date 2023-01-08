import random


def adivina_el_numero(x):
    print('===============================')
    print('     Bienvenido al Juego!      ')
    print('===============================')
    print('Tu mision es adivinar el numero random generado por la computadora.')
    numero_aleatorio = random.randint(1, x)  # numero aleatorio generado por la pc

    prediccion = 0
    while prediccion != numero_aleatorio:
        prediccion = int(input(f'Adivina un numero entre 1 y {x}: '))  # f-sting

    if prediccion < numero_aleatorio:
        print('Este numero es muy pequeño')
    elif prediccion > numero_aleatorio:
        print('Este numero es muy grande')

    print(f' Felicidades adivinaste correctamente,  el numero era {numero_aleatorio} eres sortario!!')


adivina_el_numero(3)
