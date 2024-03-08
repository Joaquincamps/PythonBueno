#"Escribe un programa en Python que evalúe el conocimiento de las capitales de diferentes países. 
#El programa debe presentar al usuario el nombre de un país de forma aleatoria y solicitar que ingrese 
#la capital correspondiente. Debe verificar si la respuesta proporcionada es correcta o incorrecta. 
#El programa debe realizar 10 preguntas en total, asegurándose de que no se repitan las preguntas durante la ejecución. 
#Al finalizar, el programa debe mostrar cuántas capitales se respondieron correctamente de las 10 preguntas realizadas."
#bin/python3

import random

diccionario={"Austria":"viena","Francia":"paris","chile":"santiago",
    "Yugoslavia":"belgrado","España":"madrid","Portugal":"lisboa","Reino Unido":"londres","Alemania":"berlin","Japón":"tokyo","China":"pekin"}
aleatorio=random.choice(list(diccionario.keys()))
capital=input("Dime la capital de "+aleatorio+":")
contador =0
correctas =0
falladas =0
while  contador <10:
    contador +=1
    aleatorio=random.choice(list(diccionario.keys()))
    capital=input("Dime la capital de "+aleatorio+":")
    lista=list(diccionario.keys())
    lista.remove(aleatorio)
    if capital==diccionario[aleatorio]:
        correctas +=1
    else:
        falladas +=1
print("El numero de aciertos es "+str(correctas)+ " y el numero de errores "+str(falladas)) 
print(lista)
