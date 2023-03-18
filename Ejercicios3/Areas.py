def area_Ciculo():
    radio = float(input("Ingresa el radio del circulo: "))
    formula = 3.1416*radio**2
    print(f"El area del circulo es {round(formula, 2)}")


def area_Rectangulo():
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    formula = base * altura
    print(f"El area del rectangulo es {round(formula, 2)}")


while True:
    opc= int(input("""
Elija una opcion:

1.Calcular Area de un circulo
2.Calcular Area de un Rectangulo
3.Salir del programa

"""))
    
    if opc == 1:
        area_Ciculo()
    elif opc == 2:
        area_Rectangulo()
    elif opc == 3:
        break
    else:
        print("!!!Elija una de las tres opiones¡¡¡")