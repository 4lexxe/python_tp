#-----------------
# ANÁLISIS DEL PROBLEMA: JUEGO DEL NIM SIMPLIFICADO
#-----------------
# Datos/Variables:
# - numero_fosforos: int - Cantidad de fósforos en la mesa
# - jugador_actual: str - Identificador del jugador en turno ("jugador 1" o "jugador 2")
# - resta_fosforos: int - Cantidad de fósforos que toma un jugador en su turno (1, 2 o 3)
#
# Estructuras de control:
# - Condicional (if-else): Para determinar quién comienza y para alternar turnos
# - Bucle principal (while): Para mantener el juego mientras queden fósforos
# - Bucle de validación (while): Para asegurar que la jugada sea válida (1-3 fósforos y no más de los disponibles)
#
# Pasos del algoritmo:
# 1. Inicializar el número de fósforos (entrada del usuario)
# 2. Determinar aleatoriamente qué jugador comienza
# 3. Mientras queden fósforos:
#    a. Mostrar fósforos restantes
#    b. Solicitar al jugador actual cuántos fósforos quiere tomar
#    c. Validar que la jugada sea legal (1-3 fósforos y no más de los disponibles)
#    d. Restar los fósforos tomados del total
#    e. Verificar si el juego ha terminado (no quedan fósforos)
#    f. Cambiar el turno al otro jugador
# 4. Declarar perdedor al jugador que tomó el último fósforo
#
# JUSTIFICACIÓN DE LA SOLUCIÓN:
# La consigna indica crear un algoritmo para el juego del NIM simplificado donde:
# - Hay una cantidad n de fósforos sobre una mesa
# - Dos jugadores, en turnos alternados, quitan 1, 2 o 3 fósforos
# - Pierde el jugador que debe tomar el último fósforo
#
# Por lo tanto, el algoritmo implementado:
# 1. Permite que el usuario defina la cantidad inicial de fósforos (n)
# 2. Implementa los turnos alternados entre dos jugadores
# 3. Limita la cantidad de fósforos a tomar entre 1 y 3
# 4. Verifica que no se puedan tomar más fósforos de los disponibles
# 5. Detecta cuando no quedan fósforos y declara perdedor al jugador en turno
#
# Esta implementación respeta totalmente las reglas del juego definidas en la consigna.
#-----------------

import random

# Inicializar la cantidad de fósforos
numero_fosforos = int(input("Ingrese el número de fosforos: "))

# Decidir quien comienza, mediante condiciones if
if random.randint(1, 2) == 1:
    jugador_actual = "jugador 1"
else:
    jugador_actual = "jugador 2"

print(f"El {jugador_actual} comienza el juego.")

# bucle del juego, donde la expresión tiene que ser mayor que 0
while numero_fosforos > 0:
    print(f"Fosforos restantes: {numero_fosforos}")
    
    resta_fosforos = int(input(f"{jugador_actual}, ingresa cuántos fósforos quieres tomar (1, 2 o 3): "))
    
    # validación para la entrada de tomas de fósforos
    while resta_fosforos < 1 or resta_fosforos > 3 or resta_fosforos > numero_fosforos:
        print("No se puede hacer ese movimiento.")
        resta_fosforos = int(input(f"{jugador_actual}, ingresa cuántos fósforos quieres tomar (1, 2 o 3): "))
    
    # restar los fósforos tomados
    numero_fosforos -= resta_fosforos
    
    # verificación si el juego ha terminado
    if numero_fosforos == 0:
        print(f"{jugador_actual} pierde, el otro jugador GANA!")
        break
    
    # cambiar el turno
    if jugador_actual == "jugador 1":
        jugador_actual = "jugador 2"
    else:
        jugador_actual = "jugador 1"
