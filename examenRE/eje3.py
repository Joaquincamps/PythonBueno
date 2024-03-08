#bin/python3
#"Escribe un programa en Python que permita a un usuario realizar una lista de la compra.
#El programa debe solicitar al usuario que ingrese los nombres y las cantidades de los productos
#que desea comprar. Debe mostrar la lista de la compra con el nombre y la cantidad de cada producto ingresado.
#El usuario puede finalizar la lista ingresando el símbolo asterisco '*'. El programa debe calcular y 
#mostrar el importe total de la compra en euros, considerando los precios de los productos previamente definidos en un diccionario."
print("Recuerda que para terminar de introducir productos, debes pulsar asterisco: '*'")
diccionario={"pan":0.56,"leche":1.15,"tomates":1.89,"lechuga":0.27,"pollo":3.75,"tercera":7.89,"pimientos":0.45,"cebollas":0.35}
lista=[]
totalCompra=0
claves=list(diccionario.keys())
while True:
    producto=input("Producto a comprar:")
    if producto == '*':
        break
    unidades = int(input("Unidades:"))
    if producto in claves:
        lista.append((producto,unidades,diccionario[producto]))
        totalCompra +=unidades * diccionario[producto]
for  producto,unidades,diccionario[producto] in lista:
    print("Producto: "+producto+" Unidades: "+str(unidades)+ " Precio: "+str(diccionario[producto]))
print("Total de la compra: "+str(totalCompra))