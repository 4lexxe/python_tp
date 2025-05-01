# Una fábrica necesita un programa para calcular el salario y mostrar el detalle de sus empleados, los mismos
# tienen un sueldo básico común y se adiciona un 10% por cada aumento de categoría, un 5% por cada año de
# antigüedad. A todos los empleados se les descuenta un 11% por aportes jubilatorios y un 4% por obra social
# ambos del sueldo básico, y finalmente un aumento fijo de $200 en concepto de salario familiar por cada hijo
# menor de 18 años.

# Paso 1: Recolectar los datos generales que afectan a todos los empleados
cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))  # Convertimos la entrada a entero
sueldo_basico = float(input("Ingrese el sueldo básico común: "))  # Convertimos la entrada a decimal (float)

# Paso 2: Iterar sobre cada empleado para calcular su salario individual
for i in range(cantidad_empleados):  # El loop se ejecutará 'cantidad_empleados' veces
  print("\nEmpleado", i+1)  # Mostramos el número de empleado actual (i+1 porque i comienza en 0)
  
  # Paso 3: Recolectar datos específicos de cada empleado
  categoria = int(input("Ingrese la categoría del empleado: "))
  antiguedad = int(input("Ingrese la antigüedad en años del empleado: "))
  hijos = int(input("Ingrese la cantidad de hijos menores de 18 años del empleado: "))

  # Paso 4: Calcular el salario considerando categoría y antigüedad
  # - Cada categoría aumenta el sueldo en un 10% del sueldo básico
  # - Cada año de antigüedad aumenta el sueldo en un 5% del sueldo básico
  salario_categoriayantiguedad = sueldo_basico + (sueldo_basico * categoria * 0.1) + (sueldo_basico * antiguedad * 0.05)
  
  # Paso 5: Calcular los descuentos por jubilación y obra social
  descuento_jubilatorio = salario_categoriayantiguedad * 0.11  # 11% de descuento por jubilación
  descuento_obrasocial = salario_categoriayantiguedad * 0.04   # 4% de descuento por obra social
  
  # Paso 6: Calcular el salario final sumando los aumentos y restando los descuentos
  salario_final = salario_categoriayantiguedad - descuento_jubilatorio - descuento_obrasocial + (hijos * 200)

  # Paso 7: Mostrar el detalle completo del salario del empleado
  print("\nDetalle del empleado:")
  print("Sueldo básico: $", sueldo_basico)
  print("Categoría:", categoria)
  print("Antigüedad:", antiguedad, "años")
  print("Hijos menores de 18 años:", hijos)
  print("Aumento por categoría: $", sueldo_basico * categoria * 0.1)
  print("Aumento por antigüedad: $", sueldo_basico * antiguedad * 0.05)
  print("Descuento jubilatorio: $", descuento_jubilatorio)
  print("Descuento obra social: $", descuento_obrasocial)
  print("Aumento por salario familiar: $", hijos * 200)
  print("Salario final: $", salario_final)

# -------------------------------------------------------------------------
# ANÁLISIS DE DEPURACIÓN (DEBUG):
# -------------------------------------------------------------------------
# 1. Validación de entradas:
#    - El programa no valida que la cantidad_empleados sea un número positivo
#    - No se verifica que sueldo_basico, categoria, antiguedad o hijos sean valores positivos
#
# 2. Posibles errores:
#    - Si el usuario ingresa texto en vez de números, el programa fallará con ValueError
#    - Es posible que los descuentos jubilatorios y de obra social deban calcularse sobre 
#      el sueldo básico, no sobre salario_categoriayantiguedad (revisar los requisitos)
#
# 3. Mejoras posibles:
#    - Formatear la salida con dos decimales usando format(): print("Sueldo básico: ${:.2f}".format(sueldo_basico))
#    - Agregar validaciones para las entradas numéricas
#    - Implementar manejo de excepciones para entradas inválidas
#    - Preguntar al usuario si desea continuar calculando salarios después de finalizar