"""
tabla = int(input('Ingrese número:'))
print(f"Tabla de multiplicar del {tabla}")
for i in range(1, 10):
    print(f"{tabla} x {i} = {i*tabla}")
"""

i=0
tabla = int(input("Ingresa numero: "))
print("La tabla de multiplicar del",tabla)
while i < 10:
    i += 1
    print(f"{tabla}x{i}={i*tabla}")

"""
vi = int(input('vi:'))
vf = int(input('vf:'))
for ddo in range (vi, vf):
    divisores = 0
    print('')
    print(ddo,': ', end='')
    for dsor in range (2,ddo):
        if ddo % dsor == 0:
            print(dsor, ',', end='')
            divisores += 1
    if divisores == 0:
        print('es un número primo!', end='')
        print('\n')
"""

vi = int(input('vi:'))
vf = int(input('vf:'))
ddo = vi

while ddo < vf:
    divisores = 0
    print('')
    print(ddo,': ', end='')
    dsor = 2

    while dsor < ddo:
        if ddo % dsor == 0:
            print(dsor, ',', end='')
            divisores += 1
        dsor += 1
    
    if divisores == 0:
        print('es un número primo!', end='')
        print('\n')

    ddo += 1
