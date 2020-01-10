#validar entero
def validar_entero(numero_positivo):
    if(isinstance(numero_positivo,int)==True and isinstance(numero_positivo,bool)==False and numero_positivo>=0):
        return True
    else:
        return False
    #fin if

#validar nombre
def validar_nombre(nombre):
    if(isinstance(nombre,str)==True and nombre.isdigit()==False):
        if(len(nombre)>=3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

#pedir entero
def pedir_entero(msg):
    n=-1
    while(validar_entero(n)==False):
        n=input(msg)
        if(n.isdigit()==True):
            n=int(n)
    return int(n)
#fin_def


def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido
