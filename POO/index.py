#!/usr/bin/env python3
class Personaje:
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre=nombre
        self.fuerza=fuerza
        self.inteligencia=inteligencia
        self.defensa=defensa
        self.vida=vida
    def atributos(self):
        print(self.nombre, ":",sep="")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida: ", self.vida)

    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza=self.fuerza+fuerza
        self.inteligencia=self.inteligencia+inteligencia
        self.defensa=self.defensa+defensa
    
    def esta_vivo(self):
        
        if self.vida >0:
            return  True
        else:
            return False
    def morir(self):
        self.vida = 0
        print(self.nombre,"Ha muerto")

    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self,enemigo):
        daño =self.daño(enemigo)
        enemigo.vida= enemigo.vida- daño
        print (self.nombre," ha realizado ",daño ," puntos de daño a ",enemigo.nombre)
        print ("La vida de ",enemigo.nombre," es de: ",enemigo.vida)
        if enemigo.esta_vivo():
             print ("La vida del enemigo ",enemigo.nombre , " es ",enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,espada):
       super().__init__(nombre,fuerza,inteligencia,defensa,vida)
       self.espada=espada
    def cambiar_arma(self):
        op=int(input("Elige la opcion:"))
        print("1.Espada oro")
        print("2.Espada diamante")
        if op ==1:
            self.espada=10
        elif op==2:
            self.espada=20
        else:
            print("Opcion incorrecta")
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,libro):
        super().__init__( nombre, fuerza, inteligencia, defensa,vida)
        self.libro=libro
    def atributos(self):
        super().atributos()
        print("Libro",self.libro)
    def daño (self,enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

goku=Personaje("Goku",20,15,10,100)
guts=Guerrero("Guts",20,10,10,100,5) 
vanessa=Mago("Vanessa",18,12,8,70,3)

goku.atacar(guts)
guts.atacar(vanessa)
vanessa.atacar(goku)

goku.atributos()
print("-------------------")
guts.atributos()
print("-------------------")
vanessa.atributos()        
'''      
guts=Guerrero("Guts",20,10,10,100,5) 
guts.cambiar_arma()
guts.atributos()
print(guts.espada)
   
    def get_fuerza(self):
        return self.fuerza
    def set_fuerza(self,fuerza):
        if fuerza < 0:
            print("No se pueden tener menos de cero puntos de Fuerza")
        else:
            self.fuerza=fuerza


mi_personaje=Personaje("Espartaco al Aparato",0,4,7,4)
mi_enemigo=Personaje("Maite",2,3,1,6)
print(mi_personaje.set_fuerza(90))
mi_personaje.atributos()

mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()

mi_personaje.atributos()
mi_personaje.subir_nivel(8,9,3)
mi_personaje.atributos()
print(mi_personaje.esta_vivo())
mi_personaje.morir()
mi_personaje.atributos()
'''