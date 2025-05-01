'''Se cuenta con una lista A cargada con la información de las materias de una carrera universitaria
privada donde, para cada una de ellas. se registra el código, nombre, año de cursada (1 a 5),
precios, cupo (valor entero que representa la cantidad máxima de alumnos a inscribir), y cantidad de inscriptos actuales. Diseñar los módulos necesarios para resolver lo siguiente:

(30 PUNTOS) Realizar la inscripción de un alumno en una materia. Para ello, se debe
solicitar y guardar el código de materia, DNI y nombre de alumno en la lista B. Para hacer
la inscripción se debe validar que el código de materia exista en la lista A y que el cupo
máximo de la misma no se haya superado; en caso contrario en caso contrario informar con
el mensaje correspondiente. A medida que se realiza una nueva inscripción es necesario
actualizar la cantidad de inscriptos de la materia en la lista A.

(15 PUNTOS) A partir de la información de la lista A, Mostrar el importe total recaudado por
una materia Dando su código. Para el cálculo se debe considerar la cantidad total de
alumnos que se inscribieron en la misma.

(20 PUNTOS) crear una lista C que contenga la información de las materias cuyo precio sea
menor al precio promedio de todas las materias.

(15 PUNTOS) Informar la cantidad de alumnos cuyo nombre contenga las subcadena
“María”

(20 PUNTOS) Disminuir el precio de todas las materias de primer año en un 5%

importante solo debe diseñar los módulos necesarios e incluir las llamadas con el mismo desde el
programa principal coma no debe diseñar el menú de opciones debe trabajar con lista anidadas y
considere la siguiente guía para el análisis de problemas
'''

listaA = [['1', 'Matematica', 1, 1000, 50, 10], ['2', 'Fisica', 2, 1500, 40, 20], ['3', 'Quimica', 3, 2000, 30, 30], ['4', 'Programacion', 4, 2500, 20, 40], ['5', 'Ingles', 5, 3000, 10, 50]]
listaB = []


def inscripcion(listaA, listaB):
  codigo = input("Ingrese el codigo de la materia: ")
  dni = input("Ingrese el dni del alumnos: ")
  nombre = input("Ingrese el nombre: ")
  pos = validar(listaA, codigo)
  if pos != -1:
    if listaA[pos][5] < listaA[pos][4]:
      listaA[pos][5] += 1
      listaB.append([codigo, dni, nombre])
    else:
      print("Cupo completo")
      return
  else:
    print("No existe la materia con ese codigo.")
    return
  

def validar(listaA, codigo):
  pos = -1
  for i, item in enumerate(listaA):
    if item[0] == codigo:
      pos = i
      break
  return pos

def importe_total(listaA):
  codigo = input("Ingrese el codigo de la materia para el importe total: ")
  pos = validar(listaA, codigo)
  if pos != -1:
    total = listaA[pos][3] * listaA[pos][5]
    print("importe total: ", total)
  else:
    print("No existe la materia")
    return
  
def listaC(listaA):
  precio = []
  for item in listaA:
    precio.append(item[3])

  promedio = sum(precio) / len(precio)

  listaC = []
  for item in listaA:
    if item[3] < promedio:
      listaC.append(item)
  print(listaC)

def cantidad_alumnos(listaB):
  cantidad = 0
  for item in listaB:
    if 'María' in item[2]:
      cantidad += 1
  print("cantidad de marias: ", cantidad)

def disminuir_precio(listaA):
  print("ANTIGUA LISTA: ", listaA)
  for item in listaA:
    if item[2] == 1:
      item[3] -= item[3] * 0.05
  print("NUEVA LISTA MATERIA: ", listaA)

#principal
inscripcion(listaA, listaB)
importe_total(listaA)
listaC(listaA)
cantidad_alumnos(listaB)
disminuir_precio(listaA)




