def decifrador(cifrado, corrimiento):
    resultado = ""
    for letra in cifrado:
        if letra.isalpha():
            codigo = ord(letra)
            codigo -= corrimiento
            if letra.isupper():
                if codigo < ord("A"):
                    codigo += 26
                elif codigo > ord("Z"):
                    codigo -= 26
            elif letra.islower():
                if codigo < ord("a"):
                    codigo += 26
                elif codigo > ord("z"):
                    codigo -= 26
            resultado += chr(codigo)
        else:
            resultado += letra
    return resultado


decifrado = decifrador("lspe", 4)
print(decifrado)
