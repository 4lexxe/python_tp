import os
os.system('cls')

# ------ ALGORITMO -------

def agregarEmpleado(m_empleados):
    legajo_repetido = True
    while (legajo_repetido):
        legajo_repetido = False
        legajo = input("Ingrese el legajo: ")
        for i in range(len(m_empleados)):
            if legajo in m_empleados[i]:
                legajo_repetido = True
                print("No se puede repetir el legajo. Ingrese sus datos nuevamente, por favor.")
                break
        if not(legajo_repetido):
            antiguedad = int(input("Ingrese la antiguedad: "))
            factor = float(input("Ingrese el factor: "))
            m_empleados.append([legajo, antiguedad, factor])

def disminuirFactor(m_empleados, legajo):
    for i in range(len(m_empleados)):
        if (legajo==m_empleados[i][0]):
            cantidad_a_disminuir = float(input("¿Cuánto desea disminuir el factor?: "))
            m_empleados[i][2] -= cantidad_a_disminuir
            return
    print("No se encontró el empleado.")

def sumatoria(m_empleados):
    suma = 0
    for i in range(len(m_empleados)):
        antiguedad = m_empleados[i][1]
        factor = m_empleados[i][2]
        producto = antiguedad*factor
        suma+=producto
    print(f"La sumatoria resulta {suma}.")


m_empleados = [ ['123', 5, 1.5], ['124', 3, 1.2]
              , ['125', 2, 1.1], ['126', 4, 1.3]
              , ['126', 4, 1.3], ['127', 6, 1.6]
              , ['128', 1, 1.0], ['129', 7, 1.7]
              , ['130', 8, 1.8], ['131', 9, 1.9]
              ]

#Agregar empleados (Aquí yo puse para agregar 3 pero podría ser solo 1)
for i in range(3):
    agregarEmpleado(m_empleados)
print(m_empleados)

#Disminuir factor
legajo = input("Ingrese el legajo del empleado para buscarlo y disminuir su factor: ")
disminuirFactor(m_empleados, legajo)
print(m_empleados)

#Calcular y mostrar sumatoria de la antigüedad por el factor
sumatoria(m_empleados)


