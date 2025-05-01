def cambiar_vocal(cad, letra):
    nueva_cad = ''
    for caracter in cad:
        if caracter in letra:
            nueva_cad += caracter.upper()
        else:
            nueva_cad += caracter
    return nueva_cad

#principal
cad = input('Ingrese una frase: ')
letra = input('Ingrese una vocal: ')
print(cambiar_vocal(cad, letra))
#Roses arE
