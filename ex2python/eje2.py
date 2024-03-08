num=0
numeros=[]
while True:
    num=input("Introduce un numero:")
    if num =='*':
        break        
    numero=int(num)
    numeros.append(numero)
    cantidad=len(numeros)
    
        
print("Numeros introducidos:"+ str(len(numeros)))
print("Suma: "+ str(sum(numeros)))
print("Número mayor: "+ str(max(numeros)))
print("Número menor: "+ str(min(numeros)))
print("Media: "+str(sum(numeros)/cantidad))
