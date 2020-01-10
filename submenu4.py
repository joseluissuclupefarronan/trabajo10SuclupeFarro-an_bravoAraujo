import libreria
def agregarAreaTapecio():
    base1=libreria.pedir_numero("ingrese base 1",5,150)
    base2=libreria.pedir_numero("ingrese base 2",10,100)
    altura=libreria.pedir_numero("ingrese altura",20,120)
    print("ingrese area del trapecio",((base1+base2)/2)*altura)
def agregarBase1():
    base2=libreria.pedir_numero("ingrese base 2",1,110)
    altura=libreria.pedir_numero("ingrese altura",10,150)
    AreaTapecio=libreria.pedir_numero("ingresar area de trapecio",200,300)
    print("ingrese base 1",((AreaTapecio+base2)/2)*altura)
opc=0
max=3
while(opc!=max):
      print("########## MENU #######")
      print("#1.agregar area del trapecio")
      print("#2.agregar base 1")
      print("#3.salir")
      opc=libreria.pedir_numero("ingrese numero",1,3)
      if(opc==1):
          agregarAreaTapecio()
      if(opc==2):
          agregarBase1()
