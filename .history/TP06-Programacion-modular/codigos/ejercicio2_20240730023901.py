'''2. Analizar, ejecutar, realizar la prueba de escritorio en forma manual y con el debugger del VSC.'''

#Pruebe para s = 1

def dos(s):
  s = s + 5
  print('Dos:', s)
def uno(s):
  s = s + 10
  dos(s)
  print('Uno:', s)
  return s

#principal
s = int(input('Inicial:'))#1
s = s + uno(s)
print('Global:',s)


#----------------------------------------------------

'''Pruebe para v = 10, luego elimine el # de la última línea,
debe mostrar el tiempo. ¿Cómo evita utilizar global v?
'''
def acelerar():
    global v
    tiempo = 1
    v += 5
    return

# Programa principal
v = float(input('Velocidad?: '))
print(f'Velocidad: {v} km/h')
print('Aumento la velocidad!')
acelerar()
print(f'Velocidad: {v} km/h')
#print('Tiempo:', tiempo)

#sin usar v global: 
def acelerar(velocidad):
    tiempo = 1
    nueva_velocidad = velocidad + 5
    return nueva_velocidad

# Programa principal
velocidad_inicial = float(input('Velocidad?: '))
print(f'Velocidad: {velocidad_inicial} km/h')
print('Aumento la velocidad!')
nueva_velocidad = acelerar(velocidad_inicial)
print(f'Velocidad: {nueva_velocidad} km/h')
