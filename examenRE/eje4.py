#"Escribe un programa en Python que solicite al usuario ingresar el número 
#de filas y columnas para una tabla numérica. El programa debe generar
#una tabla con números ascendentes organizados en filas y columnas, 
#comenzando desde 1 y continuando hasta el número total de celdas en la tabla. Luego, debe mostrar la tabla generada."
filas = int(input('Ingrese numero de filas:'))
columnas = int(input("Ingrese numero de columnas:"))
for i in range(1, filas+1):
    for j in range(1, columnas+1):
        print(i*j, end="\t")
    print()