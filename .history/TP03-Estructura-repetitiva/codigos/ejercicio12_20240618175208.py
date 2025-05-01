#Pida al usuario una cantidad N de puntos a representar en el plano cartesiano. Lea el par de valores que
#representan las coordenadas (x,y), para cada punto indique en qué cuadrante se encuentra. Muestre al final la
#cantidad de puntos ingresados para cada cuadrante. La figura muestra un caso ejemplo, con el ingreso de
#valores (x,y) para 3 puntos.

cuadrante_1 = 0
cuadrante_2 = 0
cuadrante_3 = 0
cuadrante_4 = 0

N = int(input("Ingrese la cantidad de puntos a representar: "))

for i in range(N):
    x = float(input(f"Ingrese la coordenada x del punto {i+1}: "))
    y = float(input(f"Ingrese la coordenada y del punto {i+1}: "))
    
    if x > 0 and y > 0:
        cuadrante_1 += 1
    elif x < 0 and y > 0:
        cuadrante_2 += 1
    elif x < 0 and y < 0:
        cuadrante_3 += 1
    elif x > 0 and y < 0:
        cuadrante_4 += 1

print("Cantidad de puntos en el cuadrante 1:", cuadrante_1)
print("Cantidad de puntos en el cuadrante 2:", cuadrante_2)
print("Cantidad de puntos en el cuadrante 3:", cuadrante_3)
print("Cantidad de puntos en el cuadrante 4:", cuadrante_4)