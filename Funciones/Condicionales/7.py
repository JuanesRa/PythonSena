def pagoHoras():
    if ht <= 40:
        pago = ht * 2600
        return 'Las horas de trabajo semanales del obrero fueron',ht, 'por lo cual el pago será de',pago
    else:
        he = ht-40
        total = (he*5000)+(40*2600)
        return 'Las horas de trabajo semanales del obrero fueron',ht, 'por lo cual el pago será de',total
    
ht = int(input('Ingrese las horas de trabajo semanales del obrero'))

print(pagoHoras())