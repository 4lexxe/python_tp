# Ejercicio 14: Programa de registro de ventas para un supermercado
# Este algoritmo permite registrar múltiples productos por cliente y calcula descuentos y totales

# Inicialización de variables principales
recaudacion = 0       # Acumulador para el total recaudado por el supermercado
ejecucion = "S"       # Variable de control para el bucle principal (S: continuar, otro: terminar)
orden = 0             # Contador de clientes que será incrementado automáticamente
logico_max = True     # Bandera para identificar el primer cliente (inicialización del máximo)

# Bucle principal - Procesa cada cliente hasta terminar la jornada laboral
while ejecucion.upper() == "S":
  orden += 1                 # Incrementamos el contador para asignar número de orden al cliente
  total_cliente = 0          # Inicializamos el acumulador para este cliente particular
  
  # Bucle secundario - Procesa múltiples productos para el cliente actual
  while True:
    # Bucle de validación - Asegura datos correctos (valores positivos mayores a cero)
    while True:
      try:
        # Captura de datos con manejo de excepciones
        precioProducto = float(input("Ingrese el precio del producto: "))
        cantidadProducto = int(input("Ingrese la cantidad de producto: "))

        # Validación de valores positivos
        if precioProducto > 0 and cantidadProducto > 0:
          break  # Salimos del bucle de validación si los datos son correctos
        else:
          print("El precio y la cantidad deben ser mayores que cero.")
      except ValueError:
        # Captura de errores si el usuario ingresa texto u otros datos no numéricos
        print("Entrada no válida. Por favor, ingrese valores numéricos.")

    # Cálculo del precio total por producto
    precioTotal = precioProducto * cantidadProducto

    # Aplicación de descuento condicional (10% si compra 5 o más unidades)
    if cantidadProducto >= 5:
      descuento = precioTotal * 0.10
      precioTotal -= descuento
      print(f"El producto tiene un precio de {precioTotal:.2f} pesos (se aplicó descuento)")
    else:
      print(f"El producto tiene un precio de {precioTotal:.2f} pesos (no se aplicó descuento)")

    # Acumulación del total para el cliente actual
    total_cliente += precioTotal

    # Consulta si el cliente desea agregar otro producto
    continuar_productos = input('¿El cliente desea agregar otro producto? (s/n): ').upper()
    if continuar_productos != "S":
      break  # Salimos del bucle de productos si el cliente no desea agregar más

  # Muestra el total a pagar por el cliente actual
  print(f"El cliente del orden {orden} debe pagar un total de {total_cliente:.2f} pesos")
  
  # Acumulación de la recaudación total del supermercado
  recaudacion += total_cliente

  # Determina si este cliente tiene el importe máximo hasta ahora
  if logico_max:
    # Es el primer cliente, por lo que establecemos su importe como máximo inicial
    logico_max = False
    importe_max = total_cliente
    pos_importe_max = orden
  else:
    # Comparamos con el máximo anterior y actualizamos si es necesario
    if total_cliente > importe_max:
      importe_max = total_cliente
      pos_importe_max = orden
  
  # Consulta si se desea continuar con otro cliente
  ejecucion = input('¿Continuar con otro cliente (s/n)? ').upper()

# Muestra de resultados finales
print(f'El cliente {pos_importe_max} pagó el máximo importe: ${importe_max:.2f}')
print(f'El total recaudado por el supermercado es: ${recaudacion:.2f}')
