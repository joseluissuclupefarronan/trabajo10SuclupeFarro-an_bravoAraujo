import libreria
def agregarEspacioTotal():
    velocidad=libreria.pedir_numero("ingrese velocidad",40,130)
    tiempo=libreria.pedir_numero("ingrese tiempo",10,50)
    print("ingrese espacio total", (velocidad*tiempo))
def agregarVelocidad():
    tiempo=libreria.pedir_numero("ingrese tiempo",40,100)
    espacio_total=libreria.pedir_numero("ingrese espacio total",50,165)
    print("ingrese velocidad",(espacio_total/tiempo))


opc=0
max=3
while(opc!=max):
    print("########## MENU #######")
    print("1. agregar espacio total")
    print("#2.agregar velocidad")
    print("#3. salir")
    opc=libreria.pedir_numero("ingrese numero",1,3)
    if(opc==1):
        agregarEspacioTotal()
    if(opc==2):
        agregarVelocidad()
