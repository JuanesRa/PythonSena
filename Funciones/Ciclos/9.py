def exponenciacion(x,y):
    i = 1
    operacion = x
    while(i < y):
        i  = i + 1
        operacion = operacion * x
        
    return operacion

print(exponenciacion(5,4))