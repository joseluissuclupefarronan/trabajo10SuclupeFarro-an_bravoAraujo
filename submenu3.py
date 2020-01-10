import libreria
def agregarAreaTriangulo():
    base=libreria.pedir_numero("ingrese base",2,10)
    altura=libreria.pedir_numero("ingrese altura",5,30)
    print("ingrese Area del Triangulo", (base*altura)/2)
def agregarAltura():
    AreaTriangulo=libreria.pedir_numero("ingrese Area del Triangulo",20,100)
    base=libreria.pedir_numero("ingrese base",5,25)
    print("ingrese Altura",(base/AreaTriangulo)/2)

opc=0
max=3
while(opc!=max):
    print("########## MENU #######")
    print("1. agregar area del triangulo")
    print("#2.agregar altura")
    print("#3. salir")
    opc=libreria.pedir_numero("ingrese numero",1,3)
    if(opc==1):
        agregarAreaTriangulo()
    if(opc==2):
        agregarAltura()

