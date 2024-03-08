frase="En un lugar de la mancha de cuyo nombre no quiero acordarme"
letra = 'a'
contador=0
for i in frase:
    if i == letra:
        contador +=1
print("La letra "+ letra+ " aparece "+str(contador)+" veces en la frase")