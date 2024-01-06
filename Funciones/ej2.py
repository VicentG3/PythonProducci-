from random import randint, uniform, random

num = randint(0, 10)


def randnum(num2):
    while True:
        adivina = int(input("Introduce un numero para saber si has acertado: "))
        if adivina == num2:
            print ("Has acertado el numero")
            break
        elif adivina < num2:
            print ("El numero que tienes que acertar es mayor")
        elif adivina > num2:
            print ("El numero que tienes que acertar es menor")

randnum(num)