# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

print("Los divisores de", numero, "son:")

# Iterar desde 1 hasta el número ingresado
for i in range(1, numero+1):
    # Verificar si i es un divisor del número ingresado
    if numero % i == 0:
        # Si i es divisor, imprimirlo
        print(i)
