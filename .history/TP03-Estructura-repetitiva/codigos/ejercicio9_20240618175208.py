#Escribir un programa que solicite ingresar la cantidad de alumnos de un curso y cada nota de los mismos.
#Finalmente deberá mostrar cuántos tienen notas mayores o iguales a 7 y cuántos menores a 7. También calcule
#y muestre el promedio de todos los valores ingresados.

notas_mayores_iguales_7 = 0
notas_menores_7 = 0
suma = 0

cant_alumnos = int(input("Ingresar cantidad de alumnos total en el curso: "))

for i in range(cant_alumnos):
    nota = float(input(f"Ingresar la nota de alumno {i+1}: "))
    suma += nota
    if 7 <= nota:
        notas_mayores_iguales_7 += 1
    else:
        notas_menores_7 += 1
promedio = suma/cant_alumnos
print("Cantidad de alumnos con una nota mayor o igual a 7 es: ", notas_mayores_iguales_7)
print("Cantidad de alumnos con una nota menor a 7 es: ", notas_menores_7)