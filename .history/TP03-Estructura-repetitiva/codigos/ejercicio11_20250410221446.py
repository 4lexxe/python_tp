# Diseñe un algoritmo que permita calcular las mediciones de temperaturas de una caldera, las mismas solo
# pueden ser mayores a 20 grados, si se ingresan valores inferiores a estos se debe volver a pedir el valor. Al final
# del proceso mostrar el promedio de todos los valores ingresados.

# Inicializamos variables para acumular la suma de temperaturas y contar mediciones
suma = 0
cant_mediciones = 0

# Iniciamos un bucle infinito que solo terminará cuando el usuario decida no ingresar más mediciones
while True:
  # Solicitamos al usuario que ingrese una temperatura y la convertimos a float
  temp = float(input("Ingrese la temperatura de la medición: "))
  
  # Verificamos si la temperatura es menor o igual a 20 grados
  if temp <= 20:
    # Si la temperatura es inválida, informamos al usuario y continuamos con la siguiente iteración
    print("La temperatura debe ser mayor a 20 grados. Vuelva a ingresar el valor.")
    continue  # Volvemos al inicio del bucle sin procesar esta medición
  
  # Si llegamos aquí, la temperatura es válida. La agregamos a la suma
  suma += temp
  # Incrementamos el contador de mediciones válidas
  cant_mediciones += 1
  
  # Preguntamos al usuario si desea continuar ingresando datos
  respuesta = input("¿Desea continuar ingresando mediciones? (S/N): ")
  # Si la respuesta no es "S" o "s", salimos del bucle
  if respuesta.upper() != "S":
    break  # Termina el bucle infinito

# Una vez fuera del bucle, verificamos si se ingresó al menos una medición válida
if cant_mediciones > 0:
  # Calculamos el promedio dividiendo la suma entre la cantidad de mediciones
  promedio_temperaturas = suma / cant_mediciones
  # Mostramos el resultado
  print("El promedio de las temperaturas ingresadas es:", promedio_temperaturas)
else:
  # Si no se ingresaron mediciones válidas, mostramos un mensaje adecuado
  print("No se ingresaron mediciones válidas.")