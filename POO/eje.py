class Persona:
    def __init__(self, nombre,edad,DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def  get_edad(self):
        return self.edad
    def set_edad(self,edad):
        if type(edad)==int and edad>=0:
            self.edad=edad
        else:
            print("Error en la edad")
    def get_DNI(self):
        dni_arr=['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F' ,'P', 'D','X','B','N' ,'J', 'Z' ,'S' , 'Q', 'V', 'H', 'L','C','K','E']
        dniNum=int(self.DNI[0:8])
        dniresto=dniNum%23

        if dni_arr[dniresto] == str(self.DNI[8]):
            return ("Bienvenido")
        else:
            return ("No Bienvenido")
    def set_DNI(self, DNI):
        self.DNI=DNI
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad", self.edad)
        print("DNI:" , self.DNI)
    def mayor_edad(self):
        if self.edad >= 18:
            return "Tiene la mayoria de edad"
        else:
            return "Es menor de edad"

mi_persona=Persona("Juan",25,"05426323A")
mi_persona.get_DNI()
mi_persona.mostrar()
print(mi_persona.mayor_edad())
print(mi_persona.get_DNI())