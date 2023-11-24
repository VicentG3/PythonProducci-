# Solicitar al usuario ingresar 5 números
numeros = []
for i in range(5):
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

# Encontrar el número más grande
numero_mas_grande = max(numeros)

# Mostrar el resultado
print("El número más grande es:", numero_mas_grande)