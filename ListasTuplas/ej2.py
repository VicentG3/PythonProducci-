list = []
list.append(int(input("Introduce un numero:")))
list.append(int(input("Introduce un numero:")))
list.append(int(input("Introduce un numero:")))
list.append(int(input("Introduce un numero:")))
list.append(int(input("Introduce un numero:")))

list2 = []
list2.append(int(input("Introduce un numero:")))
list2.append(int(input("Introduce un numero:")))
list2.append(int(input("Introduce un numero:")))
list2.append(int(input("Introduce un numero:")))
list2.append(int(input("Introduce un numero:")))

list3 = []

for i in list:
    if i in list2 and i not in list3:
        list3.append(i)

print (list3)

