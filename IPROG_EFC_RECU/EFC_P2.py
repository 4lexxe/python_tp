lista_codigos = ['123', '124', '125', '126', '127', '128', '129', '130', '131']
lista_stocks = [5, 3, 2, 4, 4, 6, 1, 7, 8]
lista_precios = [100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0]

def agregar_articulo(lista_codigos, lista_stocks, lista_precios):
  codigo = input("Ingrese el codigo para agregar: ")
  if not validar(codigo, lista_codigos):
    stock = int(input("Ingrese el stock: "))
    precio = float(input("Ingrese el precio: "))
    lista_codigos.append(codigo)
    lista_stocks.append(stock)
    lista_precios.append(precio)
  else:
    print("Ya existe articulo con ese codigo.")
    return
  
def validar(codigo, lista_codigos):
  encontrado = False
  for item in lista_codigos:
    if item == codigo:
      encontrado = True
      break
  return encontrado

def aumentar_stock(lista_codigos, lista_stocks):
  codigo = input("INgrese el codigo del articulo: ")
  pos = validarCodigo(codigo, lista_codigos)
  if pos != -1:
    cantidad = int(input("Ingrese la cantidad para aumentar el stock: "))
    if cantidad <= lista_stocks[pos]:
      lista_stocks[pos] += cantidad
      print("Lista actualizada: ", lista_stocks[pos])
    else:
      print("No hay stock suficiente")
  else:
    print("No existe el articulo.")
    return

def validarCodigo(codigo, lista_codigos):
  pos = -1
  for i, item in enumerate(lista_codigos):
    if item == codigo:
      pos = i #2
      break
  return pos

def sumatoria(lista_codigos, lista_stocks, lista_precios):
  suma = 0
  for i in range(len(lista_codigos)):
    suma += lista_stocks[i] * lista_precios[i]
  print("la sumatoria es: ", suma)

#principal
agregar_articulo(lista_codigos, lista_stocks, lista_precios)
aumentar_stock(lista_codigos, lista_stocks)
sumatoria(lista_codigos, lista_stocks, lista_precios)



