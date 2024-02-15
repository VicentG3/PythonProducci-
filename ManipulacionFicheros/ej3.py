def main():
    num = int(input("Introduce un número entero entre 1 y 10: "))
    m = int(input("Introduce otro número entero entre 1 y 10: "))
    try:
        with open(f"ManipulacionFicheros/tabla-{num}", "r") as f:
            table = f.readlines()
            print(table[m-1].strip("\n"))
    except FileNotFoundError:
        print("La tabla de este numero no existe")

if __name__ == "__main__":
    main()