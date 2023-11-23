# Sol·licitar informació a l'usuari
posicio = int(input("Introdueix la posició d'inici: "))
longitud = int(input("Introdueix la longitud del substring: "))
frase = input("Introdueix una frase: ")

# Obtindre el substring basat en la posició d'inici i la longitud
substring_resultat = frase[posicio:posicio + longitud]
    
# Mostrar el resultat per pantalla
print("Resultat:", substring_resultat)
