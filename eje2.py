#!/usr/bin/env python3	 
alumnos = {'1A':{'nombre':'Teresa','apellido':'Ruiz','edad':19,'curso':1,'notas':[5.7,2.3,7.7]},
		   '2A':{'nombre':'Marcos','apellido':'Delgado','edad':18,'curso':2,'notas':[3.2,2.3,1]},
		   '3A':{'nombre':'Jeffry','apellido':'Noe','edad':23,'curso':2,'notas':[5.3,5,8.7]},
		   '4A':{'nombre':'Maria','apellido':'Castillo','edad':20,'curso':2,'notas':[4,5.9,6]},
           }
num=0
while num != 7: 
    print("1.Nuevo Alumno")  
    print("2.Eliminar Alumno")  
    print("3.Consultar Nota Alumno. Mostrar Media")  
    print("4.Consultar Alumnos por Curso")  
    print("5.Mostrar Todos Los Alumnos")  
    print("6.Modificar Notas de los Alumnos")  
    print("7.Salir") 
    num = int(input("Elige una opción: "))      
 

    if num == 1:
        cod=input("Ingrese su codigo:")
        nom=input("Ingrese su nombre:")
        ape=input("Ingrese su apellido:")
        edad=int(input("Ingrese su edad:"))
        curso=int(input("Ingrese el número del curso al que pertene:"))
        notas=float(input("Ingrese sus notas:"))
        alumnos[cod]= {'nombre':nom,'apellido':ape,'edad':edad,'curso':curso,'notas':[notas]}
    elif num ==2:
        cod=input("Ingrese su codigo:")
        if cod in alumnos.keys():
            del alumnos[cod]
            print("Alumno borrado")
        else:
            print("Error no existe")
    
    elif num==3:
        cod=input("Ingrese el código del alumno: ")
        if cod in alumnos.keys():
            for i in alumnos.values():
                alumno=alumnos[cod]
                marks=alumno['notas']
                media=(sum(marks))/len(marks)
                print(marks)    
            print("El/La alumno/a "+alumno["nombre"] + alumno['apellido']+ " tiene una media de  "+str(media))
        else:
            print("Alumno no existe")
    elif num ==4:
        curso=int(input("Ingrese el número del curso al que pertene:"))
        for i in alumnos.values():
            if i['curso']==curso:
                print(i)
            else:
                print("No hay estudiantes en este curso")
    elif num ==5:
        for clave ,valor in alumnos.items():
            print(clave,valor['nombre']+valor['apellido'])
        x=input(" ")

    elif num ==6:
        cod=input("Ingrese su codigo:")
        notas_nuevas=[]
        if cod in alumnos.keys():
            for i in  range (3):
                notas=float(input("Ingrese sus notas:"))
                notas_nuevas.append(notas)
            alumnos[cod]['notas']=notas_nuevas
        else:
            print("Error no existe")
