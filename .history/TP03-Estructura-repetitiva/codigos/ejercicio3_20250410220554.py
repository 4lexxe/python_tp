# Solicitar al usuario que ingrese un número entero
# Usamos int() para convertir la entrada del usuario (que es un string) a un entero
numero = int(input("Ingrese un número entero: "))

# Mostramos un mensaje indicando que vamos a mostrar los divisores del número ingresado
print("Los divisores de", numero, "son:")

# Utilizamos un bucle for para iterar desde 1 hasta el número ingresado (inclusive)
# La función range(1, numero+1) genera una secuencia de números desde 1 hasta numero
# Es necesario usar numero+1 como segundo parámetro porque range excluye el valor final
for i in range(1, numero+1):
  # Verificamos si i es un divisor del número ingresado
  # Un número es divisor de otro si el residuo de la división es cero
  # Usamos el operador módulo (%) que devuelve el residuo de la división
  if numero % i == 0:
    # Si i es divisor (el residuo es cero), lo imprimimos
    # Esto nos permite mostrar todos los divisores uno por uno
    print(i)
