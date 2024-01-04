def introduir_notes():
    estudiants = {}
    for i in range(1, 11):
        nom = input(f"Introdueix el nom de l'estudiant {i}: ")
        nota = float(input(f"Introdueix la nota de {nom}: "))
        estudiants[str(i)] = {"nombre": nom, "nota": nota}
    return estudiants

def calcular_resultats(estudiants):
    aprovats = []
    suspesos = []
    suma_notes = 0

    for estudiant_id, dades in estudiants.items():
        nota = dades["nota"]
        suma_notes += nota

        if nota >= 5:
            aprovats.append(dades["nombre"])
        else:
            suspesos.append(dades["nombre"])

    mitjana = suma_notes / len(estudiants)

    return aprovats, suspesos, mitjana

def mostrar_resultats(aprovats, suspesos, mitjana):
    print("\nEstudiants aprovats:")
    for estudiant in aprovats:
        print(estudiant)

    print("\nEstudiants suspesos:")
    for estudiant in suspesos:
        print(estudiant)

    print(f"\nNota mitjana de la classe: {mitjana}")

estudiants = introduir_notes()
aprovats, suspesos, mitjana = calcular_resultats(estudiants)
mostrar_resultats(aprovats, suspesos, mitjana)
