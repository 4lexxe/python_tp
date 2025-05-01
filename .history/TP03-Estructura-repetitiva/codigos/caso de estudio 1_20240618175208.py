'''CE01TP03: Realice la prueba de escritorio o traza del algoritmo de Euclides utilizando el debugger de VSC.'''

a = int(55) #2366, 55
b = int(89) #273, 89

while b != 0:
    r = a % b
    a = b
    b = r
print('mcd:', a)
