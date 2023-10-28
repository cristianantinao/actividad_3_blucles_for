for numero in range (0,151):
    print(numero)
    
for numeros in range (5,1001):
    if numeros % 5 == 0:
        print(numeros) 

for x in range (1,101):
    if x % 5 ==0:
        print('Coding')
    elif x % 10 ==0:
        print('Coding Dojo')
    else : 
        print(x)
        
suma = 0
for y in range (0,11):
    if y % 2 == 1:
        suma = y+suma
        print (suma)

for cuenta_regresiva in range(2018,0,-4):
    print(cuenta_regresiva)

lownum =2
highnum =9
mult = 3
for i in range (lownum,highnum+1):
    if i % mult == 0:
        print(i)
