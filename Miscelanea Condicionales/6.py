d = int(input('Ingrese un número que será convertido a el día que corresponde del año'))
if d <= 31:
    print('Es el',d, 'de enero')
elif d <= 59:
    f = d - 31
    print('Es el',f, 'de febrero')
elif d <= 90:
    m = d - 59
    print('Es el',m, 'de marzo')
elif d <= 121:
    a = d - 90
    print('Es el',a, 'de abril')
elif d <= 152:
    ma = d - 121
    print('Es el',ma, 'de mayo')   
elif d <= 182:
    j = d - 152
    print('Es el',j, 'de junio')
elif d <= 213:
    ju = d - 182
    print('Es el',ju, 'de julio')
elif d <= 244:
    ag = d - 213
    print('Es el',ag, 'de agosto')
elif d <= 274:
    s = d - 244
    print('Es el',s, 'de septiembre')
elif d <= 305:
    o = d - 274
    print('Es el',o, 'de octubre')
elif d <= 335:
    n = d - 305
    print('Es el',n, 'de noviembre')
elif d <= 366:
    di = d - 335
    print('Es el',di, 'de diciembre')
else:
    print('El número está fuera de rango')