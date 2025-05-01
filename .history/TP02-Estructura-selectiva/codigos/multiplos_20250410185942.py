"""11. Hacer dos programas que utilicen la sentencia selectiva compuesta (anidada) y la sentencia if…elif…else…, el
programa debe pedir un número y mostrará:
● si es múltiplo de dos,
● si es múltiplo de cuatro (y de dos)
● si no es múltiplo de dos
Nota: El valor 0 se considerará múltiplo de 4 y de 2."""

# PRIMER PROGRAMA: Usando sentencias selectivas anidadas (if dentro de otro if)
numero = int(input("Ingrese un número para el primer programa: "))

# El operador % (módulo) devuelve el resto de la división entre dos números
# Si numero % 2 == 0, significa que el número es divisible por 2 sin dejar resto, es decir, es múltiplo de 2
if numero % 2 == 0:
    # Si ya sabemos que es múltiplo de 2, ahora verificamos si también es múltiplo de 4
    if numero % 4 == 0 or numero == 0:  # El 0 es considerado múltiplo de 4
        print("Es múltiplo de 4 y de 2")
    else:
        print("Es múltiplo de 2 pero no es múltiplo de 4")
else:
    print("No es múltiplo de 2")

# SEGUNDO PROGRAMA: Usando sentencias if...elif...else
numero = int(input("Ingrese un número para el segundo programa: "))

# Aquí evaluamos las condiciones de forma secuencial con if-elif-else
if numero % 4 == 0 or numero == 0:  # Primero verificamos si es múltiplo de 4 o es cero
    print("Es múltiplo de 4 y de 2")
elif numero % 2 == 0:  # Si no es múltiplo de 4, verificamos si es múltiplo de 2
    print("Es múltiplo de 2")
else:  # Si no es múltiplo ni de 4 ni de 2
    print("No es múltiplo de 2")

"""
EXPLICACIÓN:
- El operador % (módulo) calcula el resto de dividir un número entre otro.
- Por ejemplo: 10 % 2 = 0 porque 10 dividido por 2 da 5 sin resto.
- Por otro lado: 5 % 2 = 1 porque 5 dividido por 2 da 2 con resto 1.

- La condición "numero % 2 == 0" verifica si el número es divisible por 2 sin resto (es decir, es par).
- La condición "numero % 4 == 0" verifica si el número es divisible por 4 sin resto.
- "4 == 0" era un error en el código original, ya que siempre será falso.
- Se corrigió a "numero % 4 == 0" para verificar correctamente si el número es múltiplo de 4.
- Se agregó la condición "numero == 0" para tratar el caso especial donde el número es 0.
"""
