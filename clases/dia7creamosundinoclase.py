class Dino:
    ojos=2             #una variable es una caja donde lleva la informacion

    def __init__ (self, un_nombre,  un_color, canti_patas=4, un_genero=None): # en el metodo constructor se pone lo que es unico o diferenciador
        self.nombre=un_nombre # ejemplo colo se pone un_color
        self.color=un_color
        self.patas=canti_patas
        self.genero=un_genero

    def saludar(self):
        print("hola me llamo", self.nombre, "tengo", self.patas, "patas y soy",self.genero)

    def cortar_patas(self, canti_patas_a_cortar=1):
        self.patas= self.patas - canti_patas_a_cortar

    def decir_genero(self):
        print("hola soy,", self.nombre, "y me identifico como", self.genero)

pepe= Dino("macarena", "rosa", 4, "nena")
pepe.saludar()
pepa= Dino("angela","rojo",5, "nene")
pepa.saludar()
otro= Dino("anacleta","negro",15, "nene")
otro.saludar()

