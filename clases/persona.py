#programacion orientada a objetos#
class Persona: #definimos la clase es la plantilla(como una reseta para crear algo)
    edad = 0 #es un atributo de clase o propiedad del obeto que vamos a crear
    nacio = "paraguaya"
    def __init__ (self, un_nombre): #__init__ es el metodo constructor
                                    #metodos: son funciones dentro de una clase
        self.mi_nombre = un_nombre #usamos self para referirnos al objeto mismo

        print("hola naci, mallamo", self.mi_nombre)# no es obligatorio es para que nos de un mensae de que se cre0


    def cumple(self):# cumple es un metodo de la clase persona 
        self.edad = self.edad + 1 # que aumenta la propiedad edad en 1 
    def asignar_edad(self, una_edad): # asignar_edad es un metodo que recibe un argumento
                                  # numerico y asigna a la proiedad edad del objeto
        self.edad = una_edad
    def asignar_nacio(self, nancionalidad): # asignar_edad es un metodo que recibe un argumento
                                  # numerico y asigna a la proiedad edad del objeto
        self.nacio = nancionalidad
pepe =Persona ("pepito") #pepe es un objeto de clase persona
pepa =Persona ("pepito")
print(pepe.edad)
print(pepe.mi_nombre)
pepe.cumple()
print(pepe.edad)
# Eje. Agregar un metodo a la clase persona que asigne una nacionalidad y otro
#metoo saludar que imprima "hola soy"............. y mi nacionalidad es.....""
#def nacio(self):# cumple es un metodo de la clase persona 
 #       self.nacionalidad = self.nacionalidad # que aumenta la propiedad edad en 1 

pepe.asignar_nacio("brasilera")
print(pepe.nacio)
print("hola soy", pepe.nacio)
#cuando se crea un objeto se esta instanciando