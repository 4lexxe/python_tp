#En una tienda de ropa se realiza una venta especial durante una semana. Cada cliente realiza una compra y, en función de su grupo (niños, adultos, seniors), se aplican ciertos descuentos o aumentos en el precio final. Además, al final de la semana, la tienda quiere saber cuál fue el grupo que más dinero gastó en total y cuánto gastó.

# Definición de precios base para los productos
camisa = 100    # Precio base de una camisa
pantalon = 150  # Precio base de un pantalón
zapatos = 200   # Precio base de un par de zapatos

# Inicialización de contadores para almacenar el gasto acumulado de cada grupo
gasto_niño = 0    # Almacena el gasto total del grupo niños
gasto_adulto = 0  # Almacena el gasto total del grupo adultos
gasto_senior = 0  # Almacena el gasto total del grupo seniors

# Inicia la interacción con el usuario, preguntando si desea comenzar con las ventas
sino = input("¿Desea empezar con la venta? (Si/No): ").lower()

# Bucle principal que se ejecuta mientras el usuario quiera continuar con las ventas
while sino == "si":
    
    # Solicita información sobre el grupo al que pertenece el cliente
    grupo = input("¿A que grupo pertenece?: (Niño/Adulto/Senior): ").lower()
    # Validación para asegurar que se ingrese un grupo válido
    while grupo not in ["niño", "adulto", "senior"]:
        grupo = input("Error. ¿A que grupo pertenece?: (Niño/Adulto/Senior): ").lower()
    
    # Solicita cantidad de camisas a comprar    
    camisetas = int(input("¿Cuantas camisas desea llevar?: "))
    # Validación para evitar valores negativos
    while camisetas < 0:
        camisetas = int(input("Error. Valores Negativos. ¿Cuantas camisas desea llevar?: "))
    
    # Solicita cantidad de pantalones a comprar
    pantalones = int(input("¿Cuantas pantalones desea llevar?: "))
    # Validación para evitar valores negativos
    while pantalones < 0:
        pantalones = int(input("Error. Valores Negativos. ¿Cuantos pantalones desea llevar?: "))
    
    # Solicita cantidad de zapatos a comprar
    calzados = int(input("¿Cuantos zapatos desea llevar?: "))
    # Validación para evitar valores negativos
    while calzados < 0:
        calzados = int(input("Error. Valores Negativos. ¿Cuantos zapatos desea llevar?: "))
    
    # Cálculo del total a pagar según el grupo del cliente
    if grupo == "niño":
        # Para el grupo niños se aplica un 10% de descuento
        totalsindesc = camisetas * camisa + pantalon * pantalones + calzados * zapatos
        total = totalsindesc - totalsindesc * 0.1
        gasto_niño += total  # Acumula el gasto en el contador específico
    
    elif grupo == "adulto":
        # Para el grupo adultos se aplica un 5% de aumento
        totalsinaumento = camisetas * camisa + pantalon * pantalones + calzados * zapatos
        total = totalsinaumento + totalsinaumento * 0.05
        gasto_adulto += total  # Acumula el gasto en el contador específico
    
    elif grupo == "senior":
        # Para el grupo seniors se aplica un 15% de descuento
        totalsindesc = camisetas * camisa + pantalon * pantalones + calzados * zapatos
        total = totalsindesc - totalsindesc * 0.15
        gasto_senior += total  # Acumula el gasto en el contador específico
    
    # Pregunta si desea continuar con otra venta
    sino = input("¿Desea continuar con la venta? (Si/No): ").lower()

# EXPLICACIÓN DEL USO DE BANDERAS (FLAGS):
# En esta parte del código se utilizan variables como banderas para determinar
# cuál de los tres grupos de clientes gastó más dinero.

# Inicialización de variables para rastrear qué grupo gastó más
# max_gasto es una bandera que almacenará el valor del gasto máximo
# Se inicializa en -1 para asegurar que cualquier gasto positivo sea mayor
max_gasto = -1
# max_grupo es una bandera que almacenará el nombre del grupo con mayor gasto
max_grupo = ""

# Sistema de comparación para encontrar el grupo con mayor gasto
# A continuación se utilizan condicionales para comparar los gastos de cada grupo
# Si el gasto actual es mayor que el máximo registrado hasta ahora,
# actualizamos las banderas max_gasto y max_grupo

# Verificamos si el gasto de los niños es el máximo hasta ahora
if gasto_niño > max_gasto:
    max_gasto = gasto_niño   # Actualizamos la bandera de gasto máximo
    max_grupo = "Niño"       # Actualizamos la bandera del grupo con más gasto

# Verificamos si el gasto de los adultos es mayor que el máximo actual
if gasto_adulto > max_gasto:
    max_gasto = gasto_adulto  # Actualizamos la bandera de gasto máximo
    max_grupo = "Adulto"      # Actualizamos la bandera del grupo con más gasto

# Verificamos si el gasto de los seniors es mayor que el máximo actual
if gasto_senior > max_gasto:
    max_gasto = gasto_senior  # Actualizamos la bandera de gasto máximo
    max_grupo = "Senior"      # Actualizamos la bandera del grupo con más gasto

# Salida de resultados
# Verificamos que haya habido al menos una venta (max_gasto > 0)
if max_gasto > 0:
    # Mostramos el grupo que más gastó usando las banderas que encontramos
    print(f"El grupo que mas gasto fue el grupo {max_grupo} con un gasto de ${max_gasto}.")
    # Mostramos el gasto total de cada grupo
    print(f"El grupo Niño gastó ${gasto_niño}")
    print(f"El grupo Adulto gastó ${gasto_adulto}")
    print(f"El grupo Senior gastó ${gasto_senior}")
else:
    # Si no hubo ventas, mostramos un mensaje correspondiente
    print("No se realizaron ventas durante la semana.")