import libreria
def agregarVelocidad():
    distancia=libreria.pedir_numero("ingrese distancia",10,100)
    tiempo=libreria.pedir_numero("ingrese tiempo",30,60)
    print("ingrese velocidad", (distancia/tiempo))
def agregarDistancia():
    tiempo=libreria.pedir_numero("ingrese tiempo",40,100)
    velocidad=libreria.pedir_numero("ingrese velocidad",20,65)
    print("ingrese distancia",(velocidad/tiempo))


opc=0
max=3
while(opc!=max):
    print("########## MENU #######")
    print("1. agregar velocidad")
    print("#2.agregar distancia")
    print("#3. salir")
    opc=libreria.pedir_numero("ingrese numero",1,3)
    if(opc==1):
        agregarVelocidad()
    if(opc==2):
        agregarDistancia()
