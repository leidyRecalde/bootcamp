########## juego de adivinanzas#####

numero_secreto= 7
adivino = False
intentos = 10
while adivino == False and intentos >0:
    apuesta = input("adivina el numero secreto del 1 al 100, tienes 10 intentos para adivinar:")
    intentos= intentos-1

    if int(apuesta) == numero_secreto:
        print("ganaste")
        adivino = True
    if numero_secreto > int (apuesta) :
        print("el numero introducido es menor")
    elif  numero_secreto< int (apuesta):
        print("el numero introducido es mayor")

print ("termino la cantidad de intentos", "perdiste")
###eje: buscar como generar un numero aleatorio para numero_secreto