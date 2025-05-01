#Mediante un menú de opciones el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción
#incorrecta, se debe informar del error. Volver a mostrar las tres opciones luego de ejecutada cada opción,
#permitiendo volver a elegir. Si elige las opciones 1 muestre un texto de Bienvenida, 2 mostrar el mayor de
#cinco valores numéricos ingresados. Si elige la opción 3, el programa finalizará.

print("MENU DE OPCIONES")
print("1.!Bienvenida¡")
print("2.El numero mas grande de 5 valores")
print("3.Salida")

while True:
    print("Ingresar uno de los siguientes tres numeros: 1, 2, 3")
    escojer_num = int(input("Ingresar uno de los 3 números: "))

    if escojer_num == 1:
        print("¡Bienvenida!")
        break
    elif escojer_num == 2:
        numeros = []
        for i in range(5):
            num = float(input(f"Ingresar número {i+1}: "))
            numeros.append(num)

        mayor = max(numeros)
        print("El mayor número de los ingresados es:", mayor)
    elif escojer_num == 3:
        break
    else:
        print("Ingrese un numero correcto")