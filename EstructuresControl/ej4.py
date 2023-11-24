# Obtener contraseña y usuario
user = input("user:")
passw = input("password:")

if user == "root" and passw == "root123":
    print ("Acceso concedido")
else:
    print ("Acceso dengado")