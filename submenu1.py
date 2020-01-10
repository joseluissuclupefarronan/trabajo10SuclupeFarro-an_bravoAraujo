import libreria
def agregarPeso():
    masa=libreria.pedir_numero("ingrese masa",10,50)
    gravedad=libreria.pedir_numero("ingrese gravedad",10,100)
    print("ingrese peso", masa*gravedad)
def agregarMasa():
    peso=libreria.pedir_numero("ingrese peso",50,1000)
    gravedad=libreria.pedir_numero("ingrese gravedad",2,100)
    print("ingrese masa",peso/gravedad)

opc=0
max=3
while(opc!=max):
    print("########## MENU #######")
    print("1. agregar peso")
    print("#2.agregar masa")
    print("#3. salir")
    opc=libreria.pedir_numero("ingrese numero",1,3)
    if(opc==1):
        agregarPeso()
    if(opc==2):
        agregarMasa()

