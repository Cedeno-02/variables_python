# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''
# Empezar aquí la resolución del ejercicio
import math
from traceback import print_tb

print('¡Nuestra primera calculadora!')
print('Ingrese el primer numero real:')
num1 = float(input())
print('Ingrese el segundo numero real:')
num2 = float(input())

print('El resultado de la suma de', num1, 'y', num2, 'es', num1 + num2)
print('El resultado de la resta de', num1, 'y', num2, 'es', num1 - num2)
print('El resultado de la multiplicación de',
      num1, 'y', num2, 'es', num1 * num2)
print('El resultado de la división de', num1, 'entre', num2, 'es', num1 / num2)
print('El resultado de la potencia de', num1,
      'elevado al', num2, 'es', num1 ** num2)

# Por Fabián Cedeño Rojas
