def identificar_acentuacion(palabra):
    """
    Esta función recibe una palabra y devuelve si es aguda, grave o esdrújula.
    """
    vocales = ["a", "e", "i", "o", "u"]
    acentos = ["á", "é", "í", "ó", "ú"]

    # Si la palabra termina en vocal, es aguda.
    if palabra[-1] in vocales:
        return "aguda"

    # Si la palabra termina en consonante y la penúltima letra es vocal, es grave.
    elif palabra[-1] not in vocales and palabra[-2] in vocales:
        return "grave"

    # Si la palabra termina en consonante y la penúltima letra es consonante, es esdrújula.
    elif palabra[-1] not in vocales and palabra[-2] not in vocales:
        return "esdrújula"

    # Si la palabra tiene acento ortográfico en la penúltima letra, se debe reevaluar
    elif palabra[-2] in acentos:
        
        # Si la palabra termina en vocal, es aguda.
        if palabra[-1] in vocales:
            return "aguda"
        
        # Si la palabra termina en consonante, es esdrújula.
        else:
            return "esdrújula"

print(identificar_acentuacion("sofá"))  # esdrújula
print(identificar_acentuacion("casa"))  # grave
print(identificar_acentuacion("café"))  # aguda
print(identificar_acentuacion("camión"))  # aguda (porque tiene acento en la última sílaba)
