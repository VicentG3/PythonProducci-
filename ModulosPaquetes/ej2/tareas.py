def addtask(taskdic):
    taskdic.update({str(input("Nueva tarea: ")):"Incompleta"})

def completetask(taskdic):
    completed = input("Nombre de la tarea completada: ")
    if taskdic.pop(completed, 0) == 0:
        print("La tarea no existe")
    else:
        taskdic.update({completed:"Completa"})    

def seetask(taskdic):
    print("Lista de Tareas:")
    for item, amount in taskdic.items():
        print("{} ({})".format(item, amount))