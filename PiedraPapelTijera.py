import random


def juega():
    usuario = input("Juguemos piedra, papel y tijera: Escribe 'pi' si tu opcion es piedra, si es papel escribe 'pa' "
                    "si es tijera escribe 'ti'\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    print(f'Tu eleccion fue: {usuario} y el de la computadora fue: {computadora}')

    if usuario == computadora:
        return 'Empate'
    if gano_el_jugador(computadora, usuario):
        return 'Ganastes'
    return 'Perdistes'


def gano_el_jugador(oponente, jugador):
    if ((oponente == 'pi' and jugador == 'ti') or (oponente == 'pa' and jugador == 'pi')
            or (oponente == 'ti' and jugador == 'pa')):
        return True
    else:
        return False

print(juega())
