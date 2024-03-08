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
def pesoIdeal():
    class peso_ideal(IMC):
          def __init__(self, peso, estatura,sexo):
                super().__init__(peso, estatura)
                self.sexo=sexo

          def peso_ideal(self):
                if self.sexo =='hombre':
                    peso=super().get_altura() - 100
                    return peso
                else:
                    peso=super().get_altura() - 110
                    return peso