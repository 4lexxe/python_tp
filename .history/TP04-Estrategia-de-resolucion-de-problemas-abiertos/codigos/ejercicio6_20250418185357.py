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
