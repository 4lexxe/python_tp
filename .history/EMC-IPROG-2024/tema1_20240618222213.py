"""
Es una tienda se venden dos tipos de articulos, de etiqueta amarilla o de etiqueta verde, ambos tipos de articulos tienen el mismo precio unitario. Cada cliente puede comprar un solo tipo
articulo (amarillo o verde) para ello debe indicar la cantidad a comprar. Los clientes se identifican por un numero correlativo automatico. Los articulos que tengan etiqueta verde tienen
un descuento del 20% si se compran en cantidades inferiores a 10. Se quiere saber cuanto debe pagar cada cliente. Al final de la jornada, se desea saber:

#Cuantos articulos de tipo amarrillo se vendieron
#El cliente que gasto mas dinero

Validar las entradas: el precio unitario es mayor a 100 y menoro igual a 200. Las cantidades deber mayores a cero. Utilice modulos para las validaciones
"""

#Etiqueta amarilla o verde

amarillo = 0
cliente = 1
continuar = "s"
logico_max = True
while True:
    precio_unitario = float(input("Ingresar precio unitario: "))
    if 100 < precio_unitario and precio_unitario <= 200:
        break
    else:
        print("El precio ingresado no se encuentra entre el rango de los precios")

while continuar == "s":
    print(f"Nro de cliente {cliente}")
    producto = input("Ingreasar el color de la etiqueta del producto (Verde o Amarillo): ").lower()
    cant_producto = int(input("Ingresar cantidades del producto a llevar: "))
    if cant_producto > 0:
        if producto == "verde":
            total_producto = precio_unitario*cant_producto
            if cant_producto < 10:
                total_condescuento = total_producto-(total_producto*0.20)
                print(f"El total de su compra es {total_condescuento}")
                total_producto = total_condescuento
            else:
                print(f"El total de su compra es {total_producto}")
        elif producto == "amarillo":
            total_producto = cant_producto*precio_unitario
            print(f"El total de su compra es {total_producto}")
            amarillo += 1
        else:
            print("Ingresar Verde o Amarrilo")
    else:
        print("El precio que usted ingreso no es mayor a 0")
    if logico_max:
        gasto_max = total_producto
        cliente_mayor_gasto = cliente
        logico_max = False
    if total_producto > gasto_max:
        gasto_max = total_producto
        cliente_mayor_gasto = cliente
    cliente+=1
    continuar=input("Desea continuar?: ")
print(f"La cantidad total de articulos amarillos vendidos fueron: {amarillo}")
print(f"El cliente que mas gasto fue {cliente_mayor_gasto} y su gasto fue de {gasto_max}")