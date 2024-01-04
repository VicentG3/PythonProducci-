usuarios = {
    "mmacia": {
        "nombre": "Martí",
        "apellido": "Macià",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "cbiriukov": {
        "nombre": "Chechu",
        "apellido": "Biriukov",
        "password": "123456"
    }
}

user = input("Introduce un usuario:")
passw = input("Introduce un contraseña:")

for _ in range(3):
    if user in usuarios and passw == usuarios[user]["password"]:
        print("Session iniciada")
        print ("Nombre:", usuarios[user]["nombre"])
        print ("Apellido:", usuarios[user]["apellido"])
        break
    else:
        user = input("Introduce un usuario:")
        passw = input("Introduce un contraseña:")





