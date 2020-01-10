import libreria

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
