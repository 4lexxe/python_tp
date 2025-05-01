codigos = ['123', '124', '125', '126', '127', '128', '129', '130', '131']
stocks = [5, 3, 2, 4, 4, 6, 1, 7, 8]
precios = [100, 200, 300, 400, 500, 600, 700, 800, 900]

def agregar_articulo(codigos, stocks, precios):
    codigo = input('Ingrese el código del artículo: ')
    if not validarCodigo(codigo):  # Usamos la función que devuelve True o False
        stock = int(input('Ingrese el stock del artículo: '))
        precio = float(input('Ingrese el precio del artículo: '))
        codigos.append(codigo)
        stocks.append(stock)
        precios.append(precio)
    else:
        print('Ya existe un artículo con ese código')
        return

def validarCodigo(codigo):
    encontrado = False
    for item in codigos:  # Solo usamos 'item', el valor
        if item == codigo:
            encontrado = True
            break
    return encontrado

def disminuir_stock(codigos, stocks):
    codigo = input('Ingrese el código del artículo: ')
    pos = -1  # Iniciamos posición como -1 por defecto
    for i, item in enumerate(codigos):
        if item == codigo:
            pos = i
            break

    if pos != -1:  # Si encontramos el código
        cantidad = int(input('Ingrese la cantidad a disminuir: '))
        if cantidad <= stocks[pos]:
            stocks[pos] -= cantidad
            print('Stock actualizado:', stocks[pos])
        else:
            print('No hay stock suficiente')
            return
    else:
        print('No existe un artículo con ese código')
        return

    
def sumatoria(codigos, stocks, precios):
    suma = 0
    for i in range(len(codigos)):
        suma += stocks[i] * precios[i]
    print('La sumatoria es:', suma)

#principal
agregar_articulo(codigos, stocks, precios)
disminuir_stock(codigos, stocks)
sumatoria(codigos, stocks, precios)
