# PASO 1: Solicitamos datos de entrada al usuario
notaEstudiante = float(input("Ingrese la nota del estudiante: "));  # Convertimos la entrada a número decimal
regimen= int(input("Ingrese el régimen del estudiante: 1) diurno o 2) vespertino : "));  # Convertimos la entrada a número entero

# PASO 2: Evaluamos según el régimen del estudiante
if regimen == 1:
        # PASO 2.1: Para régimen diurno (1)
        if notaEstudiante > 3.5:
                # Si la nota es mayor a 3.5, el estudiante rinde examen
                print("El estudiante de regimen "+str(regimen)+ " rinde examen");
        else: 
                # Si la nota es menor o igual a 3.5, el estudiante reprueba
                print("El estudiante de regimen "+str(regimen)+ " ha reprobado");
elif regimen == 2:
        # PASO 2.2: Para régimen vespertino (2)
        if notaEstudiante > 6:
                # Si la nota es mayor a 6, el estudiante se exime del examen
                print("el estudiante de regimen "+str(regimen)+ " se exime del examen");
        elif notaEstudiante > 3.5 and notaEstudiante <= 6:
                # Si la nota está entre 3.5 y 6 (inclusive), el estudiante rinde examen
                print("El estudiante de regimen "+str(regimen)+ " rinde examen");
        else:
                # Si la nota es menor o igual a 3.5, el estudiante reprueba
                print("El estudiante de regimen "+str(regimen)+ " ha reprobado");