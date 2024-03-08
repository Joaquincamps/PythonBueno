usuarios = {}
op=0
while True:
    print("1.Nuevo")
    print("2.Listar")
    print("3.Salir")
    op=int(input("Diga una opcion:"))

    if op == 1:
        while True:
            print("Pulse * para dejar de introducir nombres:")
            nombre = input('Nombre:')
            if nombre == '*' and len(telefono) < 9:
                break
            telefono = input('Telefono:')
            usuarios[nombre] = telefono

    if op == 2:
        print('Lista de clientes')
        for i in usuarios :
            n=list(usuarios.keys())
            t=list(usuarios.values())
            print("NOMBRE:"+str(n))
            print("TELEFONO:"+str(t))
            print("------------------")
    if op==3:
        break

        

