class Cuenta():
    def __init__(self, titular,cantidad):
        self.titular=titular
        self.cantidad=cantidad
    def get_titular(self):
        if len(self.titular) ==0:
            return "Es obligatorio el nombre"
        else:
            return self.titular
    def set_titular(self,titular):
        self.titular=titular
    def get_cantidad(self):
        return self.cantidad
    def set_cantidad(self,cantidad):
        self.cantidad=cantidad
    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.cantidad)
    def ingresar(self,cantidad):
        if cantidad<=0:
            print("Error: la cantidad debe ser mayor a cero")
        else:
            self.cantidad=self.cantidad+cantidad
    def retirar(self,retiro):
        if retiro > self.cantidad:
            print("Su cuenta esta en numeros rojos")
        else:
            self.cantidad=self.cantidad-retiro

class cuentaJoven(Cuenta):
    def __init__(self, titular, cantidad,bonificacion,edad):
        super().__init__(titular, cantidad)
        self.bonificacion=bonificacion
        self.edad=edad
    def get_bonificacion(self):
        return self.bonificacion
    def set_bonificacion(self,bonificacion):
        self.bonificacion = bonificacion
    def get_edad(self):
        return self.edad
    def set_edad(self,edad):
        self.edad=edad
    def titularValido(self):
        if self.edad < 18 and self.edad > 25:
            return True
        else:
            return False
    def mostrar(self):
        super().mostrar()
        print("Cuenta joven")
        print("Bonificación:", self.bonificacion)



miCuenta=Cuenta("Jose",173.2)
miCuentaYoung=cuentaJoven("Juan",500.0,50,18)
miCuenta.ingresar(1900)
miCuenta.retirar(280)
miCuentaYoung.mostrar()