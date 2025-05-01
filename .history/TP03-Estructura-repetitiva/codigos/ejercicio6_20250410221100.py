# Ejercicio 6: Leer números enteros, hasta que el usuario ingrese el 0.
# Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

# Inicializamos la variable suma en 0, que acumulará los números positivos
suma = 0

# Iniciamos un bucle infinito que solo se romperá cuando el usuario ingrese 0
while True:
  # Solicitamos al usuario que ingrese un número y lo convertimos a entero
  num = int(input("Ingresar numero: "))
  
  # Condición de salida: si el número es 0, salimos del bucle con break
  if num == 0:
    break
  
  # Si el número no es 0, lo sumamos a nuestra variable acumuladora
  # Nota: el enunciado pide sumar solo los positivos, pero el código suma todos
  suma += num

# Una vez terminado el bucle, mostramos el resultado de la suma
print("La suma de todos sus numeros son: ", suma)