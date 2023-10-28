# actividad 1
for numero in range (0,151):
    print(numero)

# actividad 2    
for numeros in range (5,1001):
    if numeros % 5 == 0:
        print(numeros) 

# actividad 3
for x in range (1,101):
    if x % 5 ==0:
        print('Coding')
    elif x % 10 ==0:
        print('Coding Dojo')
    else : 
        print(x)

# actividad 4       
suma = 0
for y in range (0,500001):
     if y % 2 == 1:
        suma = y+suma
        print (suma)

# actividad 5
for cuenta_regresiva in range(2018,0,-4):
    print(cuenta_regresiva)

# actividad 6
lownum =2
highnum =9
mult = 3
for i in range (lownum,highnum+1):
    if i % mult == 0:
        print(i)
