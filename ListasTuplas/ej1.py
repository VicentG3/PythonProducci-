list = [12, 23, 5, 29, 92, 64]

list.insert(0, list.pop())
list.append(list.pop(2))
list.insert(0, 14)

for i in list:
    x = 0
    if type(i) == int:
        x = i + x
    else:
        list.append(x)

list.extend([4, 11, 32])

for i in list:
    if i%2 == 0:
        continue
    else:
        list.remove(i)

list.sort()

list.clear()
