def mejor_opcion(libros):
    opcion = None
    ganancia_maxima = 0

    for libro in libros:
        precio = libro['precio']
        costo = libro['costo']
        demanda = libro['demanda']
        codigo = libro['codigo']
        autor = libro['autor']
        nombre = libro['nombre']
        año = libro['año']

        ganancia = precio - costo

        if ganancia >= 14000 and demanda >= 100:
            if demanda > 800:
                precio = precio * 1.1

            ganancia_total = ganancia * demanda

            if ganancia_total > ganancia_maxima:
                ganancia_maxima = ganancia_total
                opcion = {'nombre': nombre, 'autor': autor,
                          'codigo': codigo, 'año': año, 'precio': precio}

    if opcion == None:
        return "Ninguno de los libros es la mejor opción para ser vendido"
    else:
        return opcion


biblioteca = mejor_opcion(libros=[
    {'nombre': 'La Ilíada', 'autor': 'Homero', 'codigo': 1234,
        'año': 2000, 'precio': 15000, 'costo': 5000, 'demanda': 500},
    {'nombre': 'La Odisea', 'autor': 'Homero', 'codigo': 5678,
        'año': 2005, 'precio': 20000, 'costo': 8000, 'demanda': 200},
    {'nombre': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'codigo': 9012,
     'año': 1980, 'precio': 40000, 'costo': 20000, 'demanda': 1000}])

print(biblioteca)
