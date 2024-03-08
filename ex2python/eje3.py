factura={}
cobrado=0
deuda=0
while True:
    print("1.Añadir factura:")
    print("2.Pagar factura:")
    print("3.Salir.")
    op=int(input("Escribe una de las opciones:"))
    if op ==1:
        num_factura = int(input("Introduce el numero de factura: "))
        coste = float(input("Introduce el coste de la factura:"))
        factura[num_factura]= coste
        deuda += coste
        print(factura)
    elif op ==2:
        num_factura = int(input("Introduce el numero de factura: "))
        if  num_factura in factura:
            deuda -=coste
            cobrado += coste
            factura.pop(num_factura,0)
    else:
        print("Total cobrado:", cobrado)
        print("Total pendiente de cobrar:", deuda)
        break