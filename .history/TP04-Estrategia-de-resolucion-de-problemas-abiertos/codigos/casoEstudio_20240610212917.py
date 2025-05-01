#CASOS DE ESTUDIO
'''Diseñar un algoritmo que ordene tres números a, b, c en forma ascendente utilizando
un módulo denominado menorMayor que tiene dos parámetros y que devuelve en el primer
parámetro el valor menor y en el segundo el valor mayor de los parámetros respectivamente.'''

def menor_mayor(a, b):
    if a < b:
        menor = a
        mayor = b
    else:
        menor = b
        mayor = a
    return menor, mayor

def leer():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    return a, b, c

#principal
a, b, c = leer()
a, b = menor_mayor(a, b)
b, c = menor_mayor(b, c)
a, b = menor_mayor(a, b)
print(f'{a}, {b}, {c}')

#OTRA FORMA SIN USAR 2 FUNCIONES
def menorMayor(a, b):
    if a < b:
        menor = a
        mayor = b
    else:
        menor = b
        mayor = a
    return menor, mayor

#ORIGINAL
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
a, b = menorMayor(a, b)
b, c = menorMayor(b, c)
a, b = menorMayor(a, b)
print(f"{a}, {b}, {c}")

#CASO DE ESTUDIO
def modulo_uno():
    global a  #2
    a = 7     #3
    print(a)  #4
    return #-> no es necesario el return

a = 2
modulo_uno()
print(a)