num = int(input("Introduce un número entero entre 1 y 10: "))
with open(f"ManipulacionFicheros/tabla-{num}", "w") as f:
    for i in range(1,11):
        x = i * num
        f.write(f"{x}\n")
        #f.write(str(x) + '\n')
