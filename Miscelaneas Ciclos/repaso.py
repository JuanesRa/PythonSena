import random
"""
x = 1
for i in range (1,15,x):
    x = x  + i
    print(x)
"""    

x = int(random.randint(50,100))
print(x)
if x % 2 == 0:
    for i in range(2,x+1,2):
        print(i)
else:
    for i in range(1,x+1,2):
        print(i)