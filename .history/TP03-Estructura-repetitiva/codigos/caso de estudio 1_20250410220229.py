'''CE01TP03: Realice la prueba de escritorio o traza del algoritmo de Euclides utilizando el debugger de VSC.'''

# Aquí inicializamos nuestras variables con valores enteros
# El comentario muestra valores alternativos que podríamos probar (2366/273 o 55/89)
a = int(55) #2366, 55
b = int(89) #273, 89

# Este bucle es el corazón del algoritmo de Euclides
# Se ejecuta hasta que b llegue a cero
while b != 0:
    # Calculamos el resto de dividir a entre b
    r = a % b
    # Movemos b a la posición de a
    a = b
    # El resto pasa a ser nuestro nuevo b
    b = r
# Al finalizar, a contiene el MCD
print('mcd:', a)
