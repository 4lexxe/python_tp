#Hacer un algoritmo que sea Idem Caso de Estudio 2 pero un cliente puede comparar más de un tipo de producto.
 
#Caso de estudio 2: En un supermercado se ingresa repetidamente el precio de un producto y el número de unidades a comprar por
#cliente (un cliente solo puede comprar un tipo de producto). Validar que el precio del producto y el número de
#unidades no debe ser negativo ni cero. A partir de 5 unidades se realiza un descuento del 10% sobre el total de
#la compra. Los clientes se identifican por un número de orden consecutivo automático. Muestre el importe de
#dinero que debe pagar el cliente. El proceso finaliza al terminar la jornada laboral. Mostrar el número de
#orden del cliente que pagó el máximo importe y el total recaudado por el supermercado.

recaudacion = 0
ejecucion = "S"
orden = 0
logico_max = True

while ejecucion.upper() == "S":
    orden += 1
    total_cliente = 0
    while True:
        while True:
            try:
                precioProducto = float(input("Ingrese el precio del producto: "))
                cantidadProducto = int(input("Ingrese la cantidad de producto: "))

                if precioProducto > 0 and cantidadProducto > 0:
                    break
                else:
                    print("El precio y la cantidad deben ser mayores que cero.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese valores numéricos.")

        precioTotal = precioProducto * cantidadProducto

        if cantidadProducto >= 5:  # Descuento a partir de 5 unidades
            descuento = precioTotal * 0.10
            precioTotal -= descuento
            print(f"El producto tiene un precio de {precioTotal:.2f} pesos (se aplicó descuento)")
        else:
            print(f"El producto tiene un precio de {precioTotal:.2f} pesos (no se aplicó descuento)")

        total_cliente += precioTotal

        continuar_productos = input('¿El cliente desea agregar otro producto? (s/n): ').upper()
        if continuar_productos != "S":
            break

    print(f"El cliente del orden {orden} debe pagar un total de {total_cliente:.2f} pesos")
    recaudacion += total_cliente

    if logico_max:
        logico_max = False
        importe_max = total_cliente
        pos_importe_max = orden
    else:
        if total_cliente > importe_max:
            importe_max = total_cliente
            pos_importe_max = orden
    
    ejecucion = input('¿Continuar con otro cliente (s/n)? ').upper()

print(f'El cliente {pos_importe_max} pagó el máximo importe: ${importe_max:.2f}')
print(f'El total recaudado por el supermercado es: ${recaudacion:.2f}')
