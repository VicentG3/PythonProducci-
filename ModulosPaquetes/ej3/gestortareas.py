# notas sobre importar paquetes
# import taskpacket
# taskpacket.editar.seetask()
# import taskpacket.editar oo from taskpacket import editar
# taskpacket.editar.seetask() oo editar.seetask()
# import taskpacket.editar as edit
# edit.seetask()
from taskpacket import editartareas as tareas
from taskpacket import vertareas


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
        vertareas.seetask(task)
    else:
        break
    print("")
    print("##############")
    print("")
