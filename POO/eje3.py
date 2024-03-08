class Tiempo():
    def __init__(self,hora=0,minutos=0,segundos=0,dia=0,mes=0,anno=0):
        self.hora=hora
        self.minutos=minutos
        self.segundos=segundos
        self.dia=dia
        self.mes=mes
        self.anno=anno
    def gethora(self):
        return self.hora
    def sethora(self,hora):
        self.hora=hora
    def getmin(self):
        return self.minutos
    def  setmin(self,minutos):
        self.minutos= minutos
    def getseg(self):
        return self.segundos
    def  setseg(self, segundos):
        self.segundos=segundos
    def validar_hora(self):
        if self.hora==0 or self.hora >23:
            return False
        elif self.minutos <0 or self.minutos>59:
            return False
        elif self.segundos <0 or self.segundos>59:
            return False
        else:
            return True
    def validar_fecha(self):
        if self.dia >28 and self.mes ==2:
            return False
        elif self.dia >30 and self.mes != 4  and self.mes !=6 and self.mes!=9 and self.mes!=11:
            return False
        elif self.dia >31:
            return False
        else:
            return True
    def a_minutos(self):
        total=self.hora*60+self.minutos
        return total
    def a_segundos(self):
        total=self.a_minutos()*60 +self.segundos
        return total

dia=Tiempo(12,5,30,33,7,2017)
dia.sethora(15)
print(dia.gethora())
print(dia.validar_hora())
print(dia.validar_fecha())
