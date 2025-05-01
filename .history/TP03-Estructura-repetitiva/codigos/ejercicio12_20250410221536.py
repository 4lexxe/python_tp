# Ejercicio 12: Clasificación de puntos en cuadrantes del plano cartesiano
# Descripción: Este programa solicita al usuario una cantidad N de puntos,
# lee las coordenadas (x,y) de cada punto y determina en qué cuadrante se encuentra.
# Al final muestra la cantidad de puntos en cada cuadrante.

# Inicialización de contadores para cada cuadrante
cuadrante_1 = 0  # Contador para puntos en cuadrante 1 (x > 0, y > 0)
cuadrante_2 = 0  # Contador para puntos en cuadrante 2 (x < 0, y > 0)
cuadrante_3 = 0  # Contador para puntos en cuadrante 3 (x < 0, y < 0)
cuadrante_4 = 0  # Contador para puntos en cuadrante 4 (x > 0, y < 0)

# Solicitud al usuario de la cantidad de puntos a ingresar
N = int(input("Ingrese la cantidad de puntos a representar: "))

# Ciclo para leer las coordenadas de cada punto
for i in range(N):  # Iteramos desde 0 hasta N-1
  # Solicitamos las coordenadas x e y para el punto actual
  x = float(input(f"Ingrese la coordenada x del punto {i+1}: "))
  y = float(input(f"Ingrese la coordenada y del punto {i+1}: "))
  
  # Determinamos el cuadrante según las coordenadas e incrementamos el contador correspondiente
  if x > 0 and y > 0:  # Primer cuadrante: ambas coordenadas positivas
    cuadrante_1 += 1
  elif x < 0 and y > 0:  # Segundo cuadrante: x negativa, y positiva
    cuadrante_2 += 1
  elif x < 0 and y < 0:  # Tercer cuadrante: ambas coordenadas negativas
    cuadrante_3 += 1
  elif x > 0 and y < 0:  # Cuarto cuadrante: x positiva, y negativa
    cuadrante_4 += 1
  # Nota: Si x=0 o y=0, el punto está en un eje, no en un cuadrante específico

# Presentación de resultados: mostramos la cantidad de puntos en cada cuadrante
print("Cantidad de puntos en el cuadrante 1:", cuadrante_1)
print("Cantidad de puntos en el cuadrante 2:", cuadrante_2)
print("Cantidad de puntos en el cuadrante 3:", cuadrante_3)
print("Cantidad de puntos en el cuadrante 4:", cuadrante_4)

# ---------- DEBUG Y ANÁLISIS ADICIONAL ----------
# Para depurar este código podríamos:
# 1. Verificar casos especiales: puntos que caen sobre los ejes no se están contabilizando
# 2. Podríamos agregar contadores para estos casos:
#    - eje_x = 0 (para puntos donde y = 0)
#    - eje_y = 0 (para puntos donde x = 0)
#    - origen = 0 (para el punto (0,0))
# 3. Para probar el programa correctamente, deberíamos ingresar puntos en diferentes cuadrantes:
#    - Cuadrante 1: por ejemplo (2,3)
#    - Cuadrante 2: por ejemplo (-2,3)
#    - Cuadrante 3: por ejemplo (-2,-3)
#    - Cuadrante 4: por ejemplo (2,-3)
#    - Sobre ejes: por ejemplo (0,5) o (5,0)
#    - En el origen: (0,0)