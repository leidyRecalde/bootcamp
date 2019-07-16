print(15-5/(2+2))
print("hola mundo")
print("mba´eichapa pora pa!!")
print("hola"*10)
print("hola carola"*15)
print(" hola carola "*5)
print(" la vaca lola "*2)#poner espacios antes o entre medio para que no se ensimen 
print(2-0)# hasta aui son tipos de datos
a=2
b=4
print(a+b)#variable seria la caja donde se guarda todo 
print(a+15)
print(a+2+b)
print(a+b+11+a)#fiarse en los valores de las letras 
c=5
d=1
print(a+b+c+d)#fijarse en los valores de cada letra
a=1
print(a+a+b)#siempre queda la ultima asignacion ejemplo si a es igual a 2 y despues a es igual a 1 el valor a coniderarse es la ultima ue fue asignado
print(a, b)# si utilizamos coma esto hace que haya espacio simplemente
#ejemplo. crear una variable nombre y una variable edad, con sus datos y despues imprimir: 
#hola me llamo---- y tengo ----anos
a="leidy"
b= 24# si es numero no necesariamente necesita las comillas
print("hola me llamo", a, "y tengo", b+1, "anos" )#textos van entre comillas y para separar van las comas 
#hola me llamo----tengo --- anos y mi hobby es---
hobby="fotografia"
print("hola me llamo",a,"tengo",b+1,"mi hobby es", hobby,)
listavacia= []
#ejercicio: crear una lista datos en el primer lugar este tu nombre y en e segundo lugar posicion este tu edad 
datos=["leidy", 24]
print("hola me llamo",datos[0], "y tengo",datos[1],"anos")# usar comas y el nombre de la lista para referirme al valor de las variables en las listas
datos[1] = 15
print("hola me llamo",datos[0], "y tengo",datos[1],"anos")
datos[0]="janina"
print("hola me llamo",datos[0], "y tengo",datos[1],"anos")
print (datos)
datos.append("programador")
print (datos)
#tarea: agregar una profesion y un hobby a la lista datos
datos.append("mediadora cultural")
print (datos)
datos.append("cantar")
print (datos)
datos.pop()#elimina el ultimo dato 
print (datos)
# funcion len () = lenght
dimencionesdedatos= len(datos)
print(dimencionesdedatos)
saludo= "hola que tal"
print(len(saludo))
print("la lista datos tiene", len(saludo), "elementos")
#eje. imprimir el ultimo elemento de una lista que no sabemos cuantos elemento tiene
maria=[1,2,3,4,15,16,17,19]
print (maria)
print(len(maria))
dimension=len(maria)-1
print(maria[dimension])
longitud=len(maria)-2
print(maria[longitud])
diesciseis=len(maria)-3
print(maria[diesciseis])
#bucles/loops/ciclos/interacciones
listas_temas=["variable","listas","tipos de datos"]
for concepto in listas_temas: 
    print("hoy aprendi",concepto)
    print("que gusto")
print("esto es lo que aprendi")

for variable_for in maria:
    #bloque de codigo
    print("esto se repite")
print("esto no se repite")
# ejerc. imprimir el valor del elemento con 3 signos de admiracion
lista_corta=["linda", "fea", "buena"]
for significa_for in lista_corta:
    print("!!!", significa_for)
    print("fin")
print("eso")
lista_larga=["mama","papa","hijo"]
for significa in lista_larga:
    print("!!!", significa)
    print("familia")
print("unida")

for x in range(10):
    print("hola", x)

for x in range(100):
    print("hola", x)
# imprimir el resulado de la suma de los numeros del 1 al 10
for 1 in range(1,10):
    print()








