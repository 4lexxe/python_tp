def convertir(listaExterna):
    # Paso [1]: Inicializar una lista vacía para almacenar los movimientos procesados.
    lst = list()

    # Paso [2]: Recorrer cada elemento (string) de la lista externa.
    for item in listaExterna: 
        # Paso [3]: Dividir el string en partes separadas por comas, creando una lista con los atributos de la cuenta.
        movimiento = item.split(',')

        # Paso [4]: Extraer el importe y convertirlo en un número flotante.
        # Modificar los últimos dos dígitos para convertirlos en centavos.
        importe = movimiento[2]
        importe = float(importe[:-2] + '.' + importe[-2:])
        movimiento[2] = importe  # Paso [5]: Reemplazar el importe en la lista de movimiento.

        # Paso [6]: Agregar el movimiento procesado a la lista final.
        lst.append(movimiento) 

    # Paso [7]: Retornar la lista con todos los movimientos procesados.
    return lst    

def movimientos(lst):
    # Paso [8]: Imprimir la lista de todos los movimientos.
    print('Lista de todos los movimientos')
    
    # Paso [9]: Recorrer la lista de movimientos e imprimir cada uno junto a su índice.
    for item, mov in enumerate(lst): 
        print(item, mov)

def sumar_depositos(lst):
    # Paso [10]: Imprimir el título para la lista de depósitos.
    print('Lista de depósitos')

    # Paso [11]: Inicializar una variable para acumular el total de los depósitos.
    suma = 0.
    
    # Paso [12]: Recorrer la lista de movimientos, buscando aquellos de tipo depósito (D).
    for item, mov in enumerate(lst): 
        if mov[4] == 'D':
            # Paso [13]: Imprimir el movimiento de depósito y sumarlo al total.
            print(item, mov)
            suma += mov[2]
    
    # Paso [14]: Imprimir el total acumulado de depósitos.
    print('Total Acumulado: ', suma)        

def movimiento_cuenta(lst):
    # Paso [15]: Solicitar al usuario que ingrese un número de cuenta.
    numeroCuenta = input('Ingrese Nro de Cuenta: ')
    existe = False  # Inicializar una bandera para verificar la existencia de la cuenta.

    # Paso [16]: Recorrer la lista de movimientos y buscar aquellos que coincidan con el número de cuenta ingresado.
    for item, mov in enumerate(lst):
        if mov[0] == numeroCuenta:
            # Paso [17]: Imprimir los movimientos correspondientes a la cuenta y marcar la bandera como verdadera.
            print(item, mov)
            existe = True
    
    # Paso [18]: Verificar si no se encontró la cuenta e imprimir un mensaje de advertencia.
    if not existe:
        print('No existe la cuenta ingresada...')

# Paso [19]: Definir una lista de strings que representan los movimientos de cuentas.
listaExterna = ["27200123456,MARIA FERNANDEZ,0000500056,30-05-2021,E",
                "27200321654,CARLOS TORRES,0000400045,31-05-2021,D",
                "27200987125,LAURA AQUINO,0000230000,30-05-2021,D",
                "27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E",
                "27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E",
                "27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D"]

# Paso [20]: Convertir la lista externa en una lista procesada con los movimientos de las cuentas.
cuentas = convertir(listaExterna)

# Paso [21]: Mostrar todos los movimientos de las cuentas.
movimientos(cuentas)

# Paso [22]: Mostrar los movimientos que son depósitos y el total acumulado.
sumar_depositos(cuentas)

# Paso [23]: Permitir al usuario buscar los movimientos de una cuenta específica.
movimiento_cuenta(cuentas)