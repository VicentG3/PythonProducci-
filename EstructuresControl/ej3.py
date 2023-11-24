# Obtener numero
num1 = int(input("Introduce un numero:"))
num2 = int(input("Introduce un numero:"))
par = 0
impar = 0

while num1 <= num2:
    if (num1 % 2) == 0:
        par = par + num1
    else:
        impar = impar + num1
    num1 = num1 + 1

print ("Los pares suman:" + str(par))
print ("Los impares suman:" + str(impar))
