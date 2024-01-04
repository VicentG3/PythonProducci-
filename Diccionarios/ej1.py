frecuencia = {}
mi_lista = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 1]

for i in mi_lista:
    if i in frecuencia:
        frecuencia[i] += 1
    else:
         frecuencia[i] = 1

mi_lista = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 1]

print("Lista:", mi_lista)
print("Diccionario de frecuencia:", frecuencia)
