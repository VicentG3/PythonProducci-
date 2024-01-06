numero2 = int(input("Introduce un numero para saber si es entero: "))

def esprimer(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "No es un numero primo")
                break
        else:
            print(num, "Es un numero primo")
    else:
        print(num, "No es un numero primo")

esprimer(numero2)
