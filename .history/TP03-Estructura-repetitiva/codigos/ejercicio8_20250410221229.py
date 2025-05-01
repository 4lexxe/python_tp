#Realizar el código de un programa que solicite al usuario un número entero positivo (debe validar que cumpla
#ésta condición) y muestre por pantalla todos los números impares desde 1 hasta ese número. Resuelto lo
#anterior, comente las líneas de código y agregue otras que muestre los impares en forma decreciente desde el
#número ingresado hasta 1.

# Solicitamos al usuario un número entero positivo
# TO-DO: Falta validar que el número sea positivo según el enunciado
num = int(input("Ingrese un número entero positivo: "))

# Mostramos un mensaje indicando que vamos a mostrar los números impares en forma descendente
print("Números impares desde", num, "hasta 1 en forma descendente:")

# Si el número ingresado es par, lo convertimos a impar restándole 1
# Esto es necesario porque queremos mostrar solo números impares
if num % 2 == 0:
  num -= 1

# Utilizamos un ciclo for con range que:
# - Comienza desde el número (ya ajustado si era par)
# - Termina en 0 (sin incluirlo, por lo que el último será 1)
# - Decrementa de 2 en 2 para obtener solo los impares
for i in range(num, 0, -2):
  print(i)