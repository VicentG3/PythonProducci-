import ask
import ej1
import ej2 
import ej3

while True:
    print("1- Crear tabla multiplicar")
    print("2- Mostrar tabla multiplicar")
    print("3- Mostrar resultado de multiplicacion")
    print("4- Salir")

    try:
      ax = int(input("Seleciona opcion: "))
    except:
       print("No has introducido un valor valido")
       continue

    if ax == 1:
        ej1.main(ask.main())
    elif ax == 2:
        ej2.main(ask.main())
    elif ax == 3:
        ej3.main(ask.main(), ask.main())
    elif ax == 4:
        break
    else:
       print("Introduce un numero valido")
       continue
^!2M88aVeDWmJqt3w%S&9aYF








