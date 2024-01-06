list2 = [6,14,11,3,2,1,15,19]

num = int(input("Introduce un numero del 1 al 20: "))

def testrang (in1):
    if in1 >= 0 and in1 <= 21:
        return in1
    else: 
        print ("Has introducido un numero fuera del rango, el valor por defecto sera cero")
        in1 = 0
        return in1


def inlist (num1, list):
    if num1 in list:
        print("El numero esta en la lista")
    else:
        print("El numero no esta en la lista")

inlist(testrang(num),list2)