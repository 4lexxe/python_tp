"""Escribir el código en python que permita el registro de la edad del cliente y la cantidad de fichas que compra
en una sala de juegos para niños. El programa debe mostrar el monto total de la fichas compradas teniendo en
cuenta que si la edad está en el intervalo [4,7) el precio de las fichas es un 20% más barata y además reciben 5
fichas gratis, si la edad está en el intervalo [7,10) el precio de las fichas es un 15% más cara. Para edades fuera
de esos rangos no se permite el ingreso a la sala de juegos. El precio unitario de las fichas no varía y es de 35
pesos."""

# PASO 1: Solicitar datos de entrada al usuario
edadCliente = int(input("ingrese la edad: "))  # Convertimos la entrada a número entero
cantidadFichas = int(input("ingrese la cantidad de fichas a comprar: "))  # Convertimos la entrada a número entero
precioFichas = 35  # Establecemos el precio base de cada ficha

# PASO 2: Evaluar la edad del cliente y calcular el monto según las condiciones
if 4 <= edadCliente < 7:
    # PASO 2.1: Para niños entre 4 y 6 años
    descuento = (precioFichas * 20) / 100  # Calculamos el 20% de descuento
    precioUnitario = precioFichas - descuento  # Restamos el descuento al precio original
    cantidadFichas += 5  # Sumamos las 5 fichas gratis
    montoTotal = precioUnitario * cantidadFichas  # Calculamos el monto total
    print(f"Monto total a pagar: {montoTotal} pesos por {cantidadFichas} fichas (incluye 5 fichas gratis)")
elif 7 <= edadCliente < 10:
    # PASO 2.2: Para niños entre 7 y 9 años
    aumento = (precioFichas * 15) / 100  # Calculamos el 15% de aumento
    precioUnitario = precioFichas + aumento  # Sumamos el aumento al precio original
    montoTotal = precioUnitario * cantidadFichas  # Calculamos el monto total
    print(f"Monto total a pagar: {montoTotal} pesos por {cantidadFichas} fichas")
else:
    # PASO 2.3: Para edades fuera del rango permitido
    print("No se permite el ingreso a la sala de juegos para esta edad")
