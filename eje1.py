class Jugador():
    def __init__(self,nombre,puntos_vida,ataque,defensa):
        self.nombre=nombre
        self.puntos_vida=puntos_vida
        self.ataque=ataque
        self.defensa=defensa
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_puntos(self):
        return self.puntos_vida
    def set_puntos(self,puntos_vida):
        self.puntos_vida=puntos_vida
    def get_ataque(self):
        return self.ataque
    def set_ataque(self, ataque):
        self.ataque=ataque
    def get_defensa(self):
        return self.defensa
    def set_defensa(self,defensa):
        self.defensa=defensa
    def atacar(self,enemigo):
        if self.get_ataque() > self.get_defensa():
            diferencia=self.get_ataque()-enemigo.get_defensa()
            total=enemigo.get_puntos() - diferencia
            enemigo.set_puntos(total)  # Actualiza los puntos de vida del enemigo
            return total
        else:
            total = enemigo.get_puntos() - self.get_ataque()
            return total
    def estar_vivo(self):
        if self.get_puntos() > 0:
            return True
        else: 
            return False

class Enemigo(Jugador):
    def __init__(self, nombre, puntos_vida, ataque, defensa):
        super().__init__(nombre, puntos_vida, ataque, defensa)
    def get_puntos(self):
        return super().get_puntos()
    def get_defensa(self):
        return super().get_defensa()
    def estar_vivo(self):
        return super().estar_vivo()

spiderman=Jugador("spiderman",100,65,23)
dundeVerde=Enemigo("duende verde",100,94,43)
print(spiderman.atacar(dundeVerde))
print(dundeVerde.get_puntos())
print(dundeVerde.estar_vivo())