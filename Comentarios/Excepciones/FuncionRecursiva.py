def recursiva():
    lista = []
    try:
        for i in range(3):
            numeros = int((input('Ingrese numeros 3 numeros')))
            lista.append(numeros)
    except ValueError:
        print('El tipo de dato no es correcto')
        recursiva()
    finally:
        return lista
recursiva()