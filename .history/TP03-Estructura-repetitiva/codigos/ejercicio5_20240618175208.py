"""5. Muestre todos los números primos que hay en un intervalo [inicial, final]
"""
vi = int(input("Ingrese el valor inicial del intervalo: "))
vf = int(input("Ingrese el valor final del intervalo: "))

for num in range(vi, vf + 1):
    es_primo = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
    if es_primo:
        print(num)