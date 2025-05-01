'''5. Realice dos algoritmos para calcular la siguiente fórmula:
'''
# a. Algoritmo para una cantidad n de términos de la suma
# Función para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Solicitar al usuario el valor de x y la cantidad de términos n
x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese la cantidad de términos n: "))

# Inicializar la suma
suma = 0.0

# Calcular la suma de n términos
for i in range(n):
    termino = (x ** i) / factorial(i)
    suma += termino

# Imprimir el resultado
print(f"El valor aproximado de e^{x} usando {n} términos es: {suma}")


#---------------------------------------------------------------------
#b. Algoritmo hasta que el término o error o aproximación sea menor a 0.001

# Función para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Solicitar al usuario el valor de x
x = float(input("Ingrese el valor de x: "))

# Inicializar variables
suma = 0.0
i = 0
termino = 1.0  # Inicializar con un valor mayor que el error deseado

# Calcular la suma hasta que el término sea menor a 0.001
while termino >= 0.001:
    termino = (x ** i) / factorial(i)
    suma += termino
    i += 1

# Imprimir el resultado
print(f"El valor aproximado de e^{x} con un término menor a 0.001 es: {suma}")
print(f"Se utilizaron {i} términos en la suma.")