"""4. Escribir un algoritmo que calcule y muestre la división entera de dos números enteros ddo y dsor mediante
restas sucesivas.
"""

# Solicitar al usuario que ingrese los números ddo (dividendo) y dsor (divisor)
ddo = int(input("Ingrese el dividendo (ddo): "))
dsor = int(input("Ingrese el divisor (dsor): "))

# Inicializar el cociente en 0
cociente = 0

# Mientras el dividendo sea mayor o igual que el divisor
while ddo >= dsor:
    # Restar el divisor del dividendo y aumentar el cociente en 1
    ddo -= dsor
    cociente += 1

# Mostrar el cociente (resultado de la división entera)
print("La división entera de", ddo, "entre", dsor, "es:", cociente)
