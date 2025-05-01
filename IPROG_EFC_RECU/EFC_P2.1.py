def contar_palabras(frase):
  palabras = frase.split()
  return len(palabras)

#principal 
frase = input("Ingrese la frase: ")
print(contar_palabras(frase))