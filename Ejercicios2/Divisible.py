def existe_divisible(lista, divisor):
    for numero in lista:
        if numero % divisor == 0:
            return True
    return False


numeros = []
divisor = 2
for i in range(0, 3):
    numero = int(input("Ingrese los números: "))
    numeros.append(numero)
if existe_divisible(numeros, divisor):
    print("Hay un numero que es divisible por", divisor)
else:
    print("Ningun numero es divisible por", divisor)
