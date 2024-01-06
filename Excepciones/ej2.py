
calu = input("Introdueix la clau del diccionari que vols consultar: ")

diccionari_cotxes = {
    "cotxe1": "Toyota",
    "cotxe2": "Ford",
    "cotxe3": "Honda",
    "cotxe4": "Chevrolet",
    "cotxe5": "Volkswagen",
    "cotxe6": "BMW"
}

try:
    x = diccionari_cotxes.get(calu)
    print(f"El valor de la clau {calu} és: {diccionari_cotxes[calu]}")
except KeyError:
       print("Error: La posició indicada no existeix a la llista.")
