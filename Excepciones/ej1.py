def obtenir_valor():
    llista = [6, 14, 11, 3, 2, 1, 15, 19]

    try:
        posicio = int(input("Introdueix la posició de la llista que vols consultar: "))
        valor = llista[posicio]

        print(f"El valor a la posició {posicio} és: {valor}")

    except IndexError:
        print("Error: La posició indicada no existeix a la llista.")

    except ValueError:
        print("Error: Introdueix un valor enter com a posició.")

obtenir_valor()