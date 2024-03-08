op=input("Indica si quiere letra o palabra:")
contador=0
if op == 'letra':
    idf=open( "hola.txt", "r")
    pal=input("Indica la letra a contar:")
    linea=idf.readlines()
    print(linea)
    contador=0
    for i in range(len(linea)):
        if pal in linea[i]:
            contador+=1
    print("Hay "+str(contador)+" letras "+pal)

if op == 'palabra':
    idf=open( "hola.txt", "r")
    pal=input("Indica la palabra a contar:")
    linea=idf.readlines()
    print(linea)
    contador=0
    for i in range(len(linea)):
        if pal in linea[i]:
            contador+=1
    print("Hay "+str(contador)+" palabras "+pal)