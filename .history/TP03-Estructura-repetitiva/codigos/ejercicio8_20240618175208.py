#Realizar el código de un programa que solicite al usuario un número entero positivo (debe validar que cumpla
#ésta condición) y muestre por pantalla todos los números impares desde 1 hasta ese número. Resuelto lo
#anterior, comente las líneas de código y agregue otras que muestre los impares en forma decreciente desde el
#número ingresado hasta 1.

num = int(input("Ingrese un número entero positivo: "))

print("Números impares desde", num, "hasta 1 en forma descendente:")

if num % 2 == 0:
    num -= 1

for i in range(num, 0, -2):
    print(i)