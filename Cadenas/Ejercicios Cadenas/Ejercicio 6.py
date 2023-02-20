def ortografia(palabra):
    vocales = "aeiouáéíóúü"
    tildes = "áéíóú"
    silabas = 0
    for i in range(len(palabra)):
        if palabra[i] in vocales:
            silabas += 1
            if i == len(palabra)-1 and palabra[i] in tildes:
                acento = "aguda"
            elif i == len(palabra)-2 and palabra[i+1:i+3] == "ng":
                acento = "aguda"
            elif i == len(palabra)-2 and palabra[i+1] == "s":
                acento = "aguda"
            elif i == len(palabra)-2 and palabra[i+1] == "n":
                acento = "aguda"
            elif palabra[i] in tildes:
                acento = "esdrújula"
            elif silabas == 1:
                acento = "aguda"
            elif silabas == 2:
                acento = "grave"
            else:
                acento = "sobresdrújula"


    print(acento)

ortografia("balón")
