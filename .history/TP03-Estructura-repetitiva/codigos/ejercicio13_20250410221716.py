# Mediante un menú de opciones el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción
# incorrecta, se debe informar del error. Volver a mostrar las tres opciones luego de ejecutada cada opción,
# permitiendo volver a elegir. Si elige las opciones 1 muestre un texto de Bienvenida, 2 mostrar el mayor de
# cinco valores numéricos ingresados. Si elige la opción 3, el programa finalizará.

# Mostramos el menú de opciones al usuario
print("MENU DE OPCIONES")
print("1.!Bienvenida¡")
print("2.El numero mas grande de 5 valores")
print("3.Salida")

# Comenzamos un ciclo infinito que solo se interrumpirá con la opción 3
while True:
  print("Ingresar uno de los siguientes tres numeros: 1, 2, 3")
  # Solicitamos al usuario que ingrese su elección y la convertimos a entero
  escojer_num = int(input("Ingresar uno de los 3 números: "))

  # Opción 1: Mostrar mensaje de bienvenida
  if escojer_num == 1:
    print("¡Bienvenida!")
    # Nota: No debemos usar break aquí si queremos volver al menú
    # Eliminamos el break para permitir volver al menú
    
  # Opción 2: Encontrar el mayor de 5 números
  elif escojer_num == 2:
    # En lugar de usar una lista, usaremos variables independientes
    # Inicializamos la variable que guardará el número mayor
    mayor = float('-inf')  # Comenzamos con el menor valor posible
    
    # Solicitamos 5 números y encontramos el mayor
    for i in range(5):
      # Pedimos cada número
      num = float(input(f"Ingresar número {i+1}: "))
      
      # Comparamos con el mayor actual y actualizamos si es necesario
      if num > mayor:
        mayor = num
    
    # Mostramos el resultado
    print("El mayor número de los ingresados es:", mayor)
    
  # Opción 3: Salir del programa
  elif escojer_num == 3:
    print("Finalizando programa...")
    break  # Rompemos el ciclo infinito para terminar
    
  # Cualquier otra opción: Mostrar error
  else:
    print("Ingrese un numero correcto")
    
  # Agregamos una separación visual entre iteraciones
  print("\n" + "-"*40 + "\n")