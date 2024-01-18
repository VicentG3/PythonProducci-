import operaciones

print("Introduce la operación que quieres realizar:")
print("1 suma")
print("2 resta")
print("3 multiplicacion")
print("4 division")

operacion = int(input("Operacion 1-4: "))
num1 = int(input("Numero 1:  "))
num2 = int(input("Numero 2:  "))

if operacion == 1:
    print(operaciones.suma(num1,num2))
elif operacion == 2:
    print(operaciones.resta(num1,num2))
elif operacion == 3:
    print(operaciones.multi(num1,num2))
elif operacion == 4:
    print(operaciones.divi(num1,num2))
else:
    print("No has introducido los datos correctos")