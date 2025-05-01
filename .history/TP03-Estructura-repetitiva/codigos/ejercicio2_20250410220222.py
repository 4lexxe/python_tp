"""
tabla = int(input('Ingrese número:'))
print(f"Tabla de multiplicar del {tabla}")
for i in range(1, 10):
    print(f"{tabla} x {i} = {i*tabla}")
"""

# Implementación de tabla de multiplicar con WHILE
# Inicialización del contador antes del bucle
i=0
tabla = int(input("Ingresa numero: "))
print("La tabla de multiplicar del",tabla)
while i < 10:
    i += 1  # Incremento del contador dentro del bucle
    print(f"{tabla}x{i}={i*tabla}")

# Código comentado para la búsqueda de primos con FOR
"""
vi = int(input('vi:'))
vf = int(input('vf:'))
for ddo in range (vi, vf):
    divisores = 0
    print('')
    print(ddo,': ', end='')
    for dsor in range (2,ddo):
        if ddo % dsor == 0:
            print(dsor, ',', end='')
            divisores += 1
    if divisores == 0:
        print('es un número primo!', end='')
        print('\n')
"""

# Implementación de búsqueda de primos con WHILE
vi = int(input('vi:'))  # Valor inicial del rango
vf = int(input('vf:'))  # Valor final del rango
ddo = vi  # Inicializamos el dividendo con el valor inicial

while ddo < vf:  # Bucle externo: itera sobre cada número del rango
    divisores = 0  # Contador de divisores encontrados
    print('')
    print(ddo,': ', end='')
    dsor = 2  # Comenzamos a probar desde el divisor 2

    while dsor < ddo:  # Bucle interno: prueba todos los posibles divisores
        if ddo % dsor == 0:  # Si es divisible
            print(dsor, ',', end='')
            divisores += 1
        dsor += 1  # Incremento del divisor
    
    if divisores == 0:  # Si no encontramos divisores, es primo
        print('es un número primo!', end='')
        print('\n')

    ddo += 1  # Avanzamos al siguiente número del rango
