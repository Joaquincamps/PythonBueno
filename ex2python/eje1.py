from misfunciones import pesoIdeal
op=''
with open ('pacientes.txt','r') as archivo:
        lineas=archivo.readlines()
        while op != 'd':
            print("a. Nuevo paciente")
            print("b. Consultar DNI")
            print("c. Modificar peso y/o altura del paciente")
            print("d. Salir")
            op=input("Diga una letra:")
            if op == 'a':
                 paciente={}
                 with open ("paciente.txt",'w') as archivo:
                        for i in lineas:
                            claves=i.split("|")
                            clave=claves[0]
                            valor=claves[1:]
                            paciente[clave]=valor
                        for clave, valor in paciente.items():
                            archivo.write(clave+":"+"\n")
            elif op== 'b':
                for i in lineas:
                    claves=i.split("|")
                    dni=claves[0]
                    peso=claves[7]
                    estatura=claves[8]
            class IMC():
                def __init__(self,peso,estatura):
                    self.peso=peso
                    self.estatura=estatura
                def get_peso(self):
                    return self.peso
                def get_altura(self):
                     return self.estatura
                def calculo(self):
                     imc=self.get_peso() / (self.get_altura()*self.get_altura())
                     if imc > 40:
                          return "Obesidad mórbida"
                     elif imc > 35:
                          return "Obesidad moderada"
                     elif imc >30:
                          return "Obesidad leve"
                     elif imc > 25:
                          return "Sobrepeso"
                     elif imc >= 20 and imc <= 25:
                          return "Peso ideal"
                     else:
                          return "Anorexia"
                def peso(self):
                     pesoIdeal()