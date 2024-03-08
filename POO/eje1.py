from math import sqrt
class Triangulo():
    def __init__(self,l1,l2,l3):
        self.l1=l1
        self.l2=l2
        self.l3=l3
    def get_l1(self):
        if type(self.l1) == int and self.l1 > 0:
            return self.l1
        else:
            print("Valor tiene que ser entero y mayor que 0")
    def get_l2(self):
        if type(self.l2) == int and self.l2 > 0:
            return self.l2
        else:
            print("Valor tiene que ser entero y mayor que 0")
    def get_l3(self):
        if type(self.l3) == int and self.l3 > 0:
            return self.l3
        else:
            print("Valor tiene que ser entero y mayor que 0")
    def Equilatero(self):
        if  self.get_l1()==self.get_l2()==self.get_l3():
            return "Triángulo equilátero"
        else:
            return None
    def Isosceles(self):
        if self.get_l1() == self.get_l2() or self.get_l1() == self.get_l3() or self.get_l2() == self.get_l3():
            return "Triangulo isosceles"
        else:
            return None
    def Escaleno(self):
        if  self.get_l1()!=self.get_l2()!=self.get_l3():
            return "Triángulo escaleno"
        else:
            return None
    def Imposible(self):
        if self.get_l1() + self.get_l2() <= self.get_l3() or self.get_l2() + self.get_l3() <= self.get_l1() or self.get_l1() + self.get_l3() <= self.get_l2():
            return "Triangulo imposible"
        else :
            None
    def AreaTriangulo(self):
        totalLados=self.get_l1()+self.get_l2()+self.get_l3()
        p=totalLados/2
        area=sqrt(p *(p-self.get_l1())*(p-self.get_l2())*(p-self.get_l3()))
        return "El área del triángulo es "+str(area)


mi_triangulo=Triangulo(2,4,4)
tipo_triangulo = ""
if mi_triangulo.Equilatero():
    tipo_triangulo = mi_triangulo.Equilatero()
elif mi_triangulo.Isosceles():
    tipo_triangulo = mi_triangulo.Isosceles()
elif mi_triangulo.Escaleno():
    tipo_triangulo = mi_triangulo.Escaleno()
elif mi_triangulo.Imposible():
    tipo_triangulo = mi_triangulo.Imposible()
if tipo_triangulo:
    print("El triángulo es:", tipo_triangulo)
else:
    print("El triángulo no es ni equilátero, isósceles ni escaleno.")
print(mi_triangulo.AreaTriangulo())
