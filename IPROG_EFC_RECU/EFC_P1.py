m_empleados = [ ['123', 5, 1.5], ['124', 3, 1.2]
              , ['125', 2, 1.1], ['126', 4, 1.3]
              , ['126', 4, 1.3], ['127', 6, 1.6]
              , ['128', 1, 1.0], ['129', 7, 1.7]
              , ['130', 8, 1.8], ['131', 9, 1.9]]

def agregar_empleado(m_empleados):
  legajo = input("Ingrese el legajo para agregar empleado: ")
  pos = validarLegajo(legajo, m_empleados)
  if pos == -1:
    antiguedad = int(input("Ingrese la antiguedad del empleado: "))
    factor = float(input("Ingrese el factor del empleado: "))
    m_empleados.append([legajo,antiguedad,factor])
  else:
    print("Ya existe un empleado con ese legajo.")
    return agregar_empleado(m_empleados)

def validarLegajo(legajo, m_empleados):
  pos = -1
  for i, item in enumerate(m_empleados):
    if item[0] == legajo:
      pos = i
      break
  return pos

def disminuir_factor(m_empleados):
  legajo = input("Ingrese el legajo del empleado a disminuir el factor: ")
  pos = validarLegajo(legajo, m_empleados)
  if pos != -1:
    cantidad = float(input("Ingrese la cantidad a disminuir del factor: "))
    if cantidad <= m_empleados[pos][2]:
      m_empleados[pos][2] -= cantidad
      print("Factor actualizado"+ str(m_empleados))
    else:
      print("No hay factor suficiente.")
      return disminuir_factor(m_empleados)
  else:
    print("No existe un empleado con ese legajo.")
    return disminuir_factor(m_empleados)
  
def sumatoria(m_empleados):
  suma = 0
  for item in m_empleados: 
    suma += item[1] * item[2]
  print("la sumatoria es:", suma)
  
#principal
agregar_empleado(m_empleados)
disminuir_factor(m_empleados)
sumatoria(m_empleados)
