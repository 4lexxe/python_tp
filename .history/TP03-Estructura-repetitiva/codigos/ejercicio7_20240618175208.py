edad =  int(input("Ingresar Edad: "))

for i in range (1,edad+1):
    if edad < 0:
        print("Error")
    print(i, "Años")