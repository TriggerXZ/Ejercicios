def Cine(salas, reserva, tarjeta):
    sala = input('Que tipo de sala quiere: ')
    if sala in salas:
        costo = salas[sala]
        cantidad = int(input('Cuantas voletas quieres: '))
        p_tar = input('Pagara con tarjeta si o no: ').lower()
        des_voletas = 500

        if p_tar == 'si':
            suma = costo*cantidad
            costos = suma*tarjeta
            print(
                f'El costo de la sala {sala} con la tarjeta es: {suma-costos}')
            noReserva = input('Tiene reserva si o no: ').lower()
            if noReserva == 'no':
                sreserva = suma-costos

                if cantidad >= 3:
                    desX_voletas = sreserva-des_voletas*cantidad
                    print(
                        f'Gracias a su compra de 3 voletas o mas se le descontaran 500 pesos por cada voleta comprada: {desX_voletas}')

                else:
                    print(f'El costo de la sala {sala} es {sreserva}')
            elif noReserva == 'si':
                sreserva = suma-costos+reserva

                if cantidad >= 3:
                    desX_voletas = sreserva-des_voletas*cantidad
                    print(
                        f'Gracias a su compra de 3 voletas o mas se le descontaran 500 pesos por cada voleta comprada: {desX_voletas}')

                else:
                    print(f'El costo de la sala {sala} es {sreserva}')
            else:
                noReserva = input('Tiene reserva si o no: ').lower()
                if noReserva == 'no':
                    print(f'El costo de la sala {sala} es {costo*cantidad}')
                else:
                    sreserva = costo*cantidad-reserva
                    print(f'El costo de la sala {sala} es {sreserva}')

        else:
            suma = costo*cantidad
            print(
                f'El costo de la sala {sala} sin la tarjeta es: {suma}')
            noReserva = input('Tiene reserva si o no: ').lower()
            if noReserva == 'no':

                if cantidad >= 3:
                    desX_voletas = suma-des_voletas*cantidad
                    print(
                        f'Gracias a su compra de 3 voletas o mas se le descontaran 500 pesos por cada voleta comprada: {desX_voletas}')

                else:
                    print(f'El costo de la sala {sala} es {suma}')
            elif noReserva == 'si':
                sreserva = suma-costos+reserva

                if cantidad >= 3:
                    desX_voletas = sreserva-des_voletas*cantidad
                    print(
                        f'Gracias a su compra de 3 voletas o mas se le descontaran 500 pesos por cada voleta comprada: {desX_voletas}')

                else:
                    print(f'El costo de la sala {sala} es {sreserva}')
            else:
                noReserva = input('Tiene reserva si o no: ').lower()
                if noReserva == 'no':
                    print(f'El costo de la sala {sala} es {costo*cantidad}')
                else:
                    sreserva = costo*cantidad-reserva
                    print(f'El costo de la sala {sala} es {sreserva}')

    else:
        print('La sala no existe')


Cine(salas={'dinamix': 18800, '3d': 15500,
     '2d': 11300}, reserva=2000, tarjeta=0.05)
