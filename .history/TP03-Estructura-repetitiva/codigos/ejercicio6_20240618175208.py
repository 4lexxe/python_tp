#Leer números enteros, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

suma = 0
while True:
    num = int(input("Ingresar numero: "))
    if num == 0:
        break
    suma += num
print("La suma de todos sus numeros son: ", suma)