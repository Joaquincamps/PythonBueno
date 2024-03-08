def verfich(nombre_archivo, opcion, n):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        if opcion == "top":
            for i in range(n):
                linea=lineas[i].rstrip()
                print(linea)
        elif opcion =="botton":
            for i in range(-1,-1-n,-1):
                linea=lineas[i].rstrip()
                print(linea)
        else:
            for linea in lineas:
                print(linea.rstrip())

verfich("datos.txt", "botton", 3)
