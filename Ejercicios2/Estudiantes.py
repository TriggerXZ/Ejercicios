estudiante = input("Ingrese el nombre del estudiante: ")
notas = []
contador = 0

for i in range(3):
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)
    contador += 1

suma = sum(notas)
promedio = suma / contador

if promedio >= 4:
    print(f"{estudiante} Aprobó con {promedio} (DP)")
elif 3.25 <= promedio < 4:
    print(f"{estudiante} Aprobó con {promedio} (N)")
elif 3 <= promedio < 3.25:
    print(f"{estudiante} Aprobó con {promedio} (PP)")
elif 1.5 <= promedio < 3:
    print(f"{estudiante} Reprobó con {promedio} (R)")
else:
    print(f"{estudiante} Reprobó con {promedio}")