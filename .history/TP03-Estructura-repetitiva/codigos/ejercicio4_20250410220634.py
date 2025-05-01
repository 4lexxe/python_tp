"""4. Escribir un algoritmo que calcule y muestre la división entera de dos números enteros ddo y dsor mediante
restas sucesivas.
"""

# PASO 1: Obtener los datos de entrada
# Solicitamos al usuario que ingrese los números para realizar la división
ddo = int(input("Ingrese el dividendo (ddo): "))  # El número que vamos a dividir
dsor = int(input("Ingrese el divisor (dsor): "))  # El número por el que dividimos

# PASO 2: Inicialización de variables
# El cociente representa cuántas veces hemos podido restar el divisor del dividendo
cociente = 0

# PASO 3: Implementación del algoritmo de división por restas sucesivas
# La idea fundamental es: "Dividir es determinar cuántas veces podemos restar el divisor del dividendo"
# Mientras el dividendo sea mayor o igual que el divisor, podemos seguir restando
while ddo >= dsor:
  # En cada iteración:
  # 1. Restamos el divisor del dividendo actual
  ddo -= dsor
  # 2. Aumentamos el contador de cuántas restas hemos realizado (cociente)
  cociente += 1
  # Este proceso continúa hasta que el dividendo sea menor que el divisor

# PASO 4: Al finalizar el bucle:
# - El valor de 'cociente' representa el resultado de la división entera
# - El valor final de 'ddo' representa el resto de la división

# PASO 5: Mostrar el resultado al usuario
print("La división entera de", ddo, "entre", dsor, "es:", cociente)
# Nota: Hay un error en la salida, debería mostrar el dividendo original, no el valor final de ddo (que es el resto)
