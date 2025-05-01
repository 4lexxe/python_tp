notaEstudiante = float(input("Ingrese la nota del estudiante: "));
regimen= int(input("Ingrese el régimen del estudiante: 1) diurno o 2) vespertino : "));

if regimen == 1:
        if notaEstudiante > 3.5:
                print("El estudiante de regimen "+str(regimen)+ " rinde examen");
        else: 
                print("El estudiante de regimen "+str(regimen)+ " ha reprobado");
elif regimen == 2:
        if notaEstudiante > 6:
                print("el estudiante de regimen "+str(regimen)+ " se exime del examen");
        elif notaEstudiante > 3.5 and notaEstudiante <= 6:
                print("El estudiante de regimen "+str(regimen)+ " rinde examen");
        else:
                print("El estudiante de regimen "+str(regimen)+ " ha reprobado");	