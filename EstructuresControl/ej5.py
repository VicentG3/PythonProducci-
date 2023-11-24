# Obtener contraseña y usuario
user = input("user:")

for i in range(5):
    passw = input("password:")
    if user == "root" and passw == "root123":
        print ("Acceso concedido")
        break
    else:
        print ("Acceso dengado")
print("Conexion rechazada")