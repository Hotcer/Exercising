from _datetime import datetime

minutos_magicos = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22,
                   24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
                   44, 46, 48, 50, 52, 54, 56, 58]
minuto_actual = datetime.today().minute
if minuto_actual in minutos_magicos:
    print('MINUTO MAGICO!!!!')
else:
    print('Espera el minuto magico, faltan segundos')

