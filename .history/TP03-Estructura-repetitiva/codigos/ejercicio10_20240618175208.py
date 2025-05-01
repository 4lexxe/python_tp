#Una fábrica necesita un programa para calcular el salario y mostrar el detalle de sus empleados, los mismos
#tienen un sueldo básico común y se adiciona un 10% por cada aumento de categoría, un 5% por cada año de
#antigüedad. A todos los empleados se les descuenta un 11% por aportes jubilatorios y un 4% por obra social
#ambos del sueldo básico, y finalmente un aumento fijo de $200 en concepto de salario familiar por cada hijo
#menor de 18 años.

cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
sueldo_basico = float(input("Ingrese el sueldo básico común: "))

for i in range(cantidad_empleados):
    print("\nEmpleado", i+1)
    categoria = int(input("Ingrese la categoría del empleado: "))
    antiguedad = int(input("Ingrese la antigüedad en años del empleado: "))
    hijos = int(input("Ingrese la cantidad de hijos menores de 18 años del empleado: "))

    salario_categoriayantiguedad = sueldo_basico + (sueldo_basico * categoria * 0.1) + (sueldo_basico * antiguedad * 0.05)
    descuento_jubilatorio = salario_categoriayantiguedad * 0.11
    descuento_obrasocial = salario_categoriayantiguedad * 0.04
    salario_final = salario_categoriayantiguedad - descuento_jubilatorio - descuento_obrasocial + (hijos * 200)

    print("\nDetalle del empleado:")
    print("Sueldo básico: $", sueldo_basico)
    print("Categoría:", categoria)
    print("Antigüedad:", antiguedad, "años")
    print("Hijos menores de 18 años:", hijos)
    print("Aumento por categoría: $", sueldo_basico * categoria * 0.1)
    print("Aumento por antigüedad: $", sueldo_basico * antiguedad * 0.05)
    print("Descuento jubilatorio: $", descuento_jubilatorio)
    print("Descuento obra social: $", descuento_obrasocial)
    print("Aumento por salario familiar: $", hijos * 200)
    print("Salario final: $", salario_final)