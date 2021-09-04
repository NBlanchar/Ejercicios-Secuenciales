# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 03:48:40 2021

@author: nefer
"""

# Ejercicio 1
y = ((5 + 2 - 5) ** 2 * 5 + 8 / 2 - 30) / 2 * 5 - 3
print(y)

# Ejercicio 2
z = 5
n = 3
m = z - n
y = (((z + 2 - n) ** 2 * m + 8 / 2 - 30) / 2 * 5 - 3) ** 5 + 15 * 3 - 9 / 3
print(y)

# Ejercicio 3
z = 5
n = ((8 + 2 - 4) ** 2 * 5 + 8 + 7 / 2 - 30 * 5) / 2 * 5 - 3
m = z ** 2 * 3 + n
a = (z + 2 - n) ** 2 * m + 8 / 2 - 30
y = (((a) / 2 * 5 - 3) ** 5 + 15 * 3 - 9 / 3) ** 2 - 5 / 4
print(y)

# Ejercicio 4
presion = float(input('Digite valor de la presión: '))
volumen = float(input('Digite valor de la volúmen: '))
temperatura = float(input('Digite valor de la temperatura: '))
masa = (presion * volumen) / (0.37 * (temperatura + 460))
print(f'La masa es: {masa}')
