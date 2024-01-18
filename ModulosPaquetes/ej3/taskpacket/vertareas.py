def seetask(taskdic):
    print("Lista de Tareas:")
    for item, amount in taskdic.items():
        print("{} ({})".format(item, amount))