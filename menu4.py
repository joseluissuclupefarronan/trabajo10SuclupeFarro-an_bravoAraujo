import libreria

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
