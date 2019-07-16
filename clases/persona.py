#programacion orientada a objetos#
class Persona:
    edad = 0
    def __init__ (self, un_nombre):
        self.mi_nombre = un_nombre
        print("hola naci, mallamo", self.mi_nombre)

    def cumple(self):
        self.edad = self.edad + 1

pepe =Persona ("pepito")
pepa =Persona ("pepito")
print(pepe.edad)
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)
