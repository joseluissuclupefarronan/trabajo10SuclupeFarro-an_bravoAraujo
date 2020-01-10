import libreria
def agregarAceleracion():
    velocidad_final=libreria.pedir_numero("ingrese velodidad final",40,150)
    velocidad_inicial=libreria.pedir_numero("ingrese velocidad inicial",30,80)
    tiempo=libreria.pedir_numero("ingrese tiempo",2,10)
    print("ingrese aceleracion", (velocidad_final-velocidad_inicial)/tiempo)
def agregarTiempo():
    velocidad_final=libreria.pedir_numero("ingrese velodidad final",30,120)
    velocidad_inicial=libreria.pedir_numero("ingrese velocidad inicial",40,90)
    aceleracion=libreria.pedir_numero("ingrese aceleracion", 50,150)
    print("ingrese tiempo", (velocidad_final-velocidad_inicial)/aceleracion)

opc=0
max=3
while(opc!=max):
      print("########## MENU #######")
      print("#1.agregar velocidad inicial")
      print("#2.agregar velocidad final")
      print("#3.salir")
      opc=libreria.pedir_numero("ingrese numero",1,3)
      if(opc==1):
          agregarAceleracion()
      if(opc==2):
          agregarTiempo()
