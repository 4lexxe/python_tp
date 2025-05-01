def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

#principal
frase = input('Ingrese una frase: ')
print(contar_palabras(frase))