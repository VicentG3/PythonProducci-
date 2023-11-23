# Sol·licitar informació a l'usuari
frase = input("Introdueix una frase: ")
lletra_original = input("Introdueix la lletra a reemplaçar: ")
lletra_reemplaçament = input("Introdueix la lletra pel qual reemplaçar: ")

# Comptar el nombre de vegades que la lletra original apareix a la frase
nombre_aparicions = frase.count(lletra_original)

# Reemplaçar la lletra original per la lletra de reemplaçament
frase_modificada = frase.replace(lletra_original, lletra_reemplaçament)

# Mostrar els resultats per pantalla
print("Nombre d'aparicions de", lletra_original, "a la frase:", nombre_aparicions)
print("Frase modificada:", frase_modificada)
