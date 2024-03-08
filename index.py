import random
may_arr=['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F' ,'P', 'D','X','B','N' ,'J', 'Z' ,'S' , 'Q', 'V', 'H', 'L','C','K','E']
min_arr=['t', 'r', 'w', 'a', 'g', 'm', 'y', 'f' ,'p', 'd','x','b','n' ,'j', 'z' ,'s' , 'q', 'v', 'h', 'l','c','k','e']
num_arr=['0','1','2','3','4','5','6','7','8','9']
esp_arr=['@','#','?','=','$','%','&','/']
generador=""
for i in range(3):
    generador += random.choice(may_arr)
    generador += random.choice(min_arr)
    generador += random.choice(num_arr)
    generador += random.choice(esp_arr)

print(generador)  

contrasena = input("Escribe la contraseña:")
es_fuerte=True
if len(contrasena) < 10:
    es_fuerte = False

for i in range(len(contrasena)):
    if contrasena[i].isdigit():
        True
    if contrasena[i].isupper():
        True
    if contrasena[i].islower():
        True
    if contrasena[i] not in esp_arr:
        True

if es_fuerte:
    print('Contraseña segura')
else:
    print("Su contraseña no es segura")
    print("Su contraseña es: "+generador)

