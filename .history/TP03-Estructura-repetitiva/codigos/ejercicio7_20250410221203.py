# Solicitamos al usuario que ingrese una edad y la convertimos a entero
edad = int(input("Ingresar Edad: "))

# Utilizamos un bucle for para iterar desde 1 hasta la edad ingresada (inclusive)
for i in range(1, edad+1):
  # Verificamos si la edad es negativa
  if edad < 0:
    print("Error")
  # Mostramos cada año desde 1 hasta la edad ingresada
  print(i, "Años")