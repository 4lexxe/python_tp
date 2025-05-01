#En una tienda de ropa se realiza una venta especial durante una semana. Cada cliente realiza una compra y, en función de su grupo (niños, adultos, seniors), se aplican ciertos descuentos o aumentos en el precio final. Además, al final de la semana, la tienda quiere saber cuál fue el grupo que más dinero gastó en total y cuánto gastó.

#Precios base=
#camisa: 100
#Pantalón: 150
#Zapatos: 200

#Descuentos y aumentos=
#Niños (grupo 1): 10% de descuento en todo.
#Adultos (grupo 2): 5% de aumento en todo.
#Seniors (grupo 3): 15% de descuento en todo.

#Además, por cada grupo se realiza la siguiente operación=

#El cliente puede comprar una o más de las prendas mencionadas
#El total de la compra de un cliente se calcula sumando los precios de las prendas seleccionadas y aplicando el descuento o aumento según el grupo.
#Al final de la semana, la tienda quiere saber:
#¿Qué grupo (niños, adultos, seniors) gastó más dinero?
#¿Cuánto gastó cada grupo en total?

camisa=100
pantalon=150
zapatos=200
gasto_niño=0
gasto_adulto=0
gasto_senior=0

sino=input("¿Desea empezar con la venta? (Si/No): ").lower()

while sino=="si":
    
    grupo=input("¿A que grupo pertenece?: (Niño/Adulto/Senior): ").lower()
    while grupo not in ["niño","adulto","senior"]:
        grupo=input("Error. ¿A que grupo pertenece?: (Niño/Adulto/Senior): ").lower()
        
    camisetas=int(input("¿Cuantas camisas desea llevar?: "))
    while camisetas<0:
        camisetas=int(input("Error. Valores Negativos. ¿Cuantas camisas desea llevar?: "))
    
    pantalones=int(input("¿Cuantas pantalones desea llevar?: "))
    while pantalones<0:
        pantalones=int(input("Error. Valores Negativos. ¿Cuantos pantalones desea llevar?: "))
    
    calzados=int(input("¿Cuantos zapatos desea llevar?: "))
    while calzados<0:
        calzados=int(input("Error. Valores Negativos. ¿Cuantos zapatos desea llevar?: "))
        
    if grupo=="niño":
        
        totalsindesc=camisetas*camisa+pantalon*pantalones+calzados*zapatos
        total=totalsindesc-totalsindesc*0.1
        gasto_niño+=total
    
    elif grupo=="adulto":
        
        totalsinaumento=camisetas*camisa+pantalon*pantalones+calzados*zapatos
        total=totalsinaumento+totalsinaumento*0.05
        gasto_adulto+=total
        
    elif grupo=="senior":
        
        totalsindesc=camisetas*camisa+pantalon*pantalones+calzados*zapatos
        total=totalsindesc-totalsindesc*0.15
        gasto_senior+=total
        
    sino=input("¿Desea continuar con la venta? (Si/No): ").lower()

# Determine the group that spent the most using max
max_gasto = max(gasto_niño, gasto_adulto, gasto_senior)

# Print the results
if max_gasto > 0:
  if max_gasto == gasto_niño:
    grupo_max = "Niño"
  elif max_gasto == gasto_adulto:
    grupo_max = "Adulto"
  else:
    grupo_max = "Senior"
  
  print(f"El grupo que más gastó es el grupo {grupo_max} con un gasto de ${max_gasto}.")
  print(f"Gastos por grupo: Niño: ${gasto_niño}, Adulto: ${gasto_adulto}, Senior: ${gasto_senior}")
else:
  print("Nadie compró o no se deseó empezar con la venta.")