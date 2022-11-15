def temperatura(grados):
    f = grados*1.8+32
    k = grados+273.15
    r = (grados+273.15)*9/5
    
    return grados,'grados Celsius a grados Fahrenheit es',f, 'a grados Kelvin es',k, 'a grados Rankine es',r

print(temperatura(15))