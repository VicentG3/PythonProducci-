# Solicitar al usuario ingresar 5 números
numeros = []
while True:
    numero = input("Ingrese el número: ")
    if numero == "fi":
        break
    numeros.append(int(numero))

# Encontrar el número más grande
numero_mas_grande = max(numeros)

# Mostrar el resultado
print("El número más grande es:", numero_mas_grande)
