# Escribir un programa que solicite ingresar la cantidad de alumnos de un curso y cada nota de los mismos.
# Finalmente deberá mostrar cuántos tienen notas mayores o iguales a 7 y cuántos menores a 7. También calcule
# y muestre el promedio de todos los valores ingresados.

# Inicialización de variables para contar y acumular
notas_mayores_iguales_7 = 0  # Contador para notas >= 7
notas_menores_7 = 0          # Contador para notas < 7
suma = 0                     # Acumulador para calcular el promedio

# Entrada de datos: solicitamos la cantidad total de alumnos
cant_alumnos = int(input("Ingresar cantidad de alumnos total en el curso: "))

# Utilizamos un bucle for para iterar sobre cada alumno
for i in range(cant_alumnos):
  # Solicitamos la nota de cada alumno (i+1 para mostrar números de alumno desde 1)
  nota = float(input(f"Ingresar la nota de alumno {i+1}: "))
  
  # Acumulamos la nota para calcular el promedio posteriormente
  suma += nota
  
  # Estructura condicional para clasificar las notas
  if 7 <= nota:  # Si la nota es mayor o igual a 7
    notas_mayores_iguales_7 += 1  # Incrementamos el contador correspondiente
  else:  # Si la nota es menor a 7
    notas_menores_7 += 1  # Incrementamos el otro contador
    
# Cálculo del promedio: suma total dividida por la cantidad de alumnos
promedio = suma/cant_alumnos

# Mostrar resultados
print("Cantidad de alumnos con una nota mayor o igual a 7 es: ", notas_mayores_iguales_7)
print("Cantidad de alumnos con una nota menor a 7 es: ", notas_menores_7)
print(f"El promedio de las notas es: {promedio:.2f}")  # Agregamos el promedio formateado a 2 decimales

# ----- DEBUG Y EXPLICACIÓN ADICIONAL -----
# 
# SEGUIMIENTO DE EJECUCIÓN (ejemplo con 3 alumnos):
# 1. Inicializamos: notas_mayores_iguales_7 = 0, notas_menores_7 = 0, suma = 0
# 2. Ingresamos cant_alumnos = 3
# 3. Iteración 1: 
#    - Se pide nota alumno 1, supongamos nota = 8
#    - suma = 0 + 8 = 8
#    - 7 <= 8? Sí, entonces notas_mayores_iguales_7 = 1
# 4. Iteración 2:
#    - Se pide nota alumno 2, supongamos nota = 5
#    - suma = 8 + 5 = 13
#    - 7 <= 5? No, entonces notas_menores_7 = 1
# 5. Iteración 3:
#    - Se pide nota alumno 3, supongamos nota = 9
#    - suma = 13 + 9 = 22
#    - 7 <= 9? Sí, entonces notas_mayores_iguales_7 = 2
# 6. Cálculo del promedio: promedio = 22/3 = 7.33
# 7. Se muestra: 2 alumnos con nota >= 7, 1 alumno con nota < 7, promedio = 7.33
#
# COMPLEJIDAD:
# - Tiempo: O(n) donde n es la cantidad de alumnos
# - Espacio: O(1) ya que solo usamos variables simples