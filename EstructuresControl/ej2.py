# Obtener numero
num1 = int(input("Introduce un numero:"))
num2 = int(input("Introduce un numero:"))
sum = 0

while num1 <= num2:
    sum = sum + num1
    num1 = num1 + 1

print ("Los pares suman:" + str(sum))