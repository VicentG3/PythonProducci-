import tareas

task = {}
while True:
    print("1. Agregar nova tasca")
    print("2. Marcar tasca com completada")
    print("3. Mostrar totes les tasques")
    print("4. Eixir")
    action = int(input("Seleccione una opció (1/2/3/4): "))
    if action == 1:
        tareas.addtask(task)
    elif action == 2:
        tareas.completetask(task)
    elif action == 3:
        tareas.seetask(task)
    else:
        break
    print("")
    print("##############")
    print("")
