#Diseñe un algoritmo que permita calcular las mediciones de temperaturas de una caldera, las mismas solo
#pueden ser mayores a 20 grados, si se ingresan valores inferiores a estos se debe volver a pedir el valor. Al final
#del proceso mostrar el promedio de todos los valores ingresados.

suma = 0
cant_mediciones = 0

while True:
    temp = float(input("Ingrese la temperatura de la medición: "))
    
    if temp <= 20:
        print("La temperatura debe ser mayor a 20 grados. Vuelva a ingresar el valor.")
        continue
    
    suma += temp
    cant_mediciones += 1
    
    respuesta = input("¿Desea continuar ingresando mediciones? (S/N): ")
    if respuesta.upper() != "S":
        break

if cant_mediciones > 0:
    promedio_temperaturas = suma / cant_mediciones
    print("El promedio de las temperaturas ingresadas es:", promedio_temperaturas)
else:
    print("No se ingresaron mediciones válidas.")