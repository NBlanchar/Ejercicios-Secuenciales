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

# Ejercicio 5
edad = int(input('Digite la edad: '))
NPulsaciones = (200 - edad) / 10
print(f'El numero de pulsaciones por cada 10 seg es: {NPulsaciones}')

# Ejercicio 6
Inversionista_1 = float(input('Digite aporte del inversionista 1: '))
Inversionista_2 = float(input('Digite aporte del inversionista 2: '))
Inversionista_3 = float(input('Digite aporte del inversionista 3: '))
Total = Inversionista_1 + Inversionista_2 + Inversionista_3
Porcentaje_1 = Inversionista_1 / Total * 100
Porcentaje_2 = Inversionista_2 / Total * 100
Porcentaje_3 = Inversionista_3 / Total * 100
print(f'El porcentaje del inversionista 1 es: {Porcentaje_1}%')
print(f'El porcentaje del inversionista 2 es: {Porcentaje_2}%')
print(f'El porcentaje del inversionista 3 es: {Porcentaje_3}%')

# Ejercicio 7
ahorro = float(input('Digite monto ahorrado: '))
interes = ahorro * 0.015
total = ahorro + interes
print(f'El saldo final del ahorrador es: {total}')

# Ejercicio 8
sueldo = float(input('Digite el sueldo: '))
ley_politica = sueldo * 0.01
SSocial = sueldo * 0.04
SForzoso = sueldo * 0.005
CAhorro = sueldo * 0.05
total = sueldo - ley_politica - SSocial - SForzoso - CAhorro
print(f'El descuento por ley de politica publica es: {ley_politica}')
print(f'El descuento por seguro social es: {SSocial}')
print(f'El descuento por seguro forzoso es: {SForzoso}')
print(f'El descuento por caja de ahorro es: {CAhorro}')
print(f'El Total a pagar al trabajador es: {total}')

# Ejercicio 9
NPalabras = int(input('Digite el numero de palabras: '))
tamano = float(input('Digite el tamaño en centímetros: '))
NColores = int(input('Digite el numero de colores: '))
total = (NPalabras * 20000) + (tamano * 15000) + (NColores * 25000)
print(f'El total a pagar por el aviso es: {total}')

# Ejercicio 10
antiguedad = int(input('Digite la antiguedad del trabajador: '))
total = ((antiguedad - 1) * 120000) + 100000
print(f'El monto a pagar por el bono es: {total}')

# Ejercicio 11
horas = int(input('Digite el numero de horas trabajadas: '))
PHoras = horas * 20000
descuento = PHoras * 0.05
total = PHoras - descuento
print(f'El descuento por caja de ahorro es: {descuento}')
print(f'El monto a pagar al profesor es: {total}')

# Ejercicio 12
MInicial = float(input('Digite el monto inicial de la tarjeta: '))
MFinal = float(input('Digite el monto final de la tarjeta: '))
Ctotal = MFinal - MInicial
Cllamada = 5 * Ctotal / 6
print(f'El costo de la llamada es:{Cllamada}')

# Ejercicio 13
NFotos = int(input('Digite el numero de fotos: '))
TFotos = NFotos * 1500
Total = TFotos + (TFotos * 0.16)
print(f'El moto a pagar por las fotos es: {Total}')

# Ejercicio 14
presupuesto = float(input('Digite el presupuesto del hospital: '))
Ginecologia = presupuesto * 0.4
Traumatologia = presupuesto * 0.3
Pediatria = presupuesto * 0.3
print(f'El presupuesto para el area de ginecología es : {Ginecologia}')
print(f'El presupuesto para el area de traumatología es : {Traumatologia}')
print(f'El presupuesto para el area de pediatría es : {Pediatria}')

# Ejercicio 15
NPeliculas = int(input("Digite el numero de peliculas: "))
Ndias = int(input("Digite el numero de dias: "))
Total = 15000 * (Ndias * (NPeliculas-1))
print(f'El monto a pagar es: {Total}')
