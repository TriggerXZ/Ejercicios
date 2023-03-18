arr = [1, 2, 2, 5, 4, 6, 7, 8, 8, 8]

a = 1
num = arr[0]
frecuencia = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        frecuencia += 1
        if frecuencia > a:
            a = frecuencia
            num = arr[i]
    else:
        frecuencia = 1

print(f"Aparece: {a}")
print(f"Número: {num}")
