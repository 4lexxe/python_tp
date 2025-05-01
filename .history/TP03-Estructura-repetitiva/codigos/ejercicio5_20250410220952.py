"""5. Muestre todos los números primos que hay en un intervalo [inicial, final]
"""
# Solicitamos al usuario ingresar los límites del intervalo
vi = int(input("Ingrese el valor inicial del intervalo: "))
vf = int(input("Ingrese el valor final del intervalo: "))

# Iteramos sobre todos los números en el intervalo [vi, vf]
for num in range(vi, vf + 1):
  # Asumimos inicialmente que el número es primo
  es_primo = True
  
  # Un número primo es mayor que 1
  if num > 1:
    # Verificamos si es divisible por algún número entre 2 y (num-1)
    for i in range(2, num):
      # Si encontramos un divisor, entonces no es primo
      if num % i == 0:
        es_primo = False
        # Salimos del bucle, ya no es necesario seguir verificando
        break
  else:
    # Los números menores o iguales a 1 no son primos
    es_primo = False
    
  # Si después de todas las verificaciones el número sigue siendo primo, lo imprimimos
  if es_primo:
    print(num)