num = int(input("Introduce un número entero entre 1 y 10: "))
try:
    with open(f"ManipulacionFicheros/tabla-{num}", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("La tabla de este numero no existe")
