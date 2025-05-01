"""Escribir el código en python que permita el registro de la edad del cliente y la cantidad de fichas que compra
en una sala de juegos para niños. El programa debe mostrar el monto total de la fichas compradas teniendo en
cuenta que si la edad está en el intervalo [4,7) el precio de las fichas es un 20% más barata y además reciben 5
fichas gratis, si la edad está en el intervalo [7,10) el precio de las fichas es un 15% más cara. Para edades fuera
de esos rangos no se permite el ingreso a la sala de juegos. El precio unitario de las fichas no varía y es de 35
pesos."""

edadCliente= int(input("ingrese la edad :"));
cantidadFichas= int(input("ingrese la cantidad de fichas a comprar: "));
precioFichas=35


if 4 <= edadCliente < 7:
    descuento=(precioFichas*20)/100
    print((precioFichas-descuento)*cantidadFichas);
elif 7<= edadCliente < 10:
    aumento=(precioFichas*15)/100;
    print(aumento)
    print((precioFichas+aumento)*cantidadFichas);
else:
    print("no se permite el ingreso")
