# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:45:16 2021

@author: DavidCamposSerrano
"""

#Dada la siguiente lista, que contiene las medidas de base y altura respectivas para 5 triangulos, calcular el area de todos ellos


"""
triangulos=[
            (3,2), TRIANGULO1:BASE:3 - ALTURA, 2
            (1,5), TRIANGULO2:BASE:1 - ALTURA, 5
            (6,7), TRIANGULO3:BASE:6 - ALTURA, 7
            ]
"""
import math
#¿Como vamos a recorrer la lista "triangulos"? con un for
#En cada iteracion tenemos una tupla, ya que cada elemento de la lista es una tupla formada por la base y la altura del triangulo (se trata de una lista de triangulos)
triangulos=[(3,2), (1,5), (6,7)]
listaCirculos=[3, 6, 1, 9, 5]
rectangulos=[(3,2), (1,5), (6,7)]
cuadrados=[4, 5, 7, 2, 8, 1, 6]
Listatriangulos=[(3, 2), (1, 5), (6, 7)]
Listarectángulo=[(3,2), (1, 5), (6, 7)]
Listacírculo=[3, 6, 1, 9, 5]
Listacuadrado=[4, 5, 7, 2, 8, 1, 6]

print("1.Area de un triangulo 1")
print("2.Area de un rectangulo")
print("3.Area de un circulo")
print("4.Area de un cuadrado")
numero=int(input("Elegir un numero de los anteriores "))
if(numero==1):
    for triangulo in triangulos: 
        print(f"El area de un triangulo de base {triangulo[0]} y altura {triangulo[1]} es {triangulo[0]*triangulo[1]/2}")
elif(numero==2):    
    for rectangulo in rectangulos:
        #print(rectangulos)
        #print(rectangulo[0]*rectangulo[1])
        print(f"El area de un rectangulo de base {rectangulo[0]} y altura {rectangulo[1]} es {rectangulo[0]* rectangulo[1]}")
elif(numero==3):   
    for radio in listaCirculos:
        #print(radio)
        #print(math.pi)
        #pi=round(math.pi, 2)
        print(f"El area de un circulo de  radio {radio} es {round(math.pi, 2)*radio**2}")
elif(numero==4):    
    for lado in cuadrados:
        print(f"El area de un cuadrado de lado {lado} es {lado**2}")
else:
    print("No ha elegido un numero correcto")
#--------------------------------------V1 trabajo GitHub---------------------------------------------    
opc=0
while(opc!=8):
    print("Calculadora")
    print("Introduzca uno de los numeros")
    print("1.SUMA de numeros")
    print("2.RESTA de numeros")
    print("3.MULTIPLICACIÓN de numeros")
    print("4.DIVISIÓN de numeros")
    print("5.COCIENTE de la división")
    print("6.RESTO de la división")
    print("7.EXPONENCIACIÓN")
    print("8.SALIR")
    opc=int(input("Eliga un numero de los anteriores "))
    while(opc<1 or opc>8):
        print("Calculadora")
        print("Introduzca uno de los numeros")
        print("1.SUMA de numeros")
        print("2.RESTA de numeros")
        print("3.MULTIPLICACIÓN de numeros")
        print("4.DIVISIÓN de numeros")
        print("5.COCIENTE de la división")
        print("6.RESTO de la división")
        print("7.EXPONENCIACIÓN")
        print("8.SALIR")
        opc=int(input("Eliga un numero de los anteriores "))
    if(opc==1):
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        resultado1=numero1+numero2
        print(f"\t La suma de estos dos numeros es: {resultado1}")
    
    elif(opc==2):
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        resultado1=numero1-numero2
        print(f"\t La resta de estos dos numeros es: {resultado1}")
    
    elif(opc==3):
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        resultado1=numero1*numero2
        print(f"\t La multiplicación de estos dos numeros es: {resultado1}")
        
    elif(opc==4):
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        if(numero2==0):
            print("El denominador no puede ser igual a 0")
        resultado1=numero1/numero2
        print(f"\t La división de estos dos numeros es: {resultado1}")
        
    elif(opc==5):
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        resultado1=numero1//numero2
        print(f"\t El cociente de estos dos numeros es: {resultado1}")
    
    elif(opc==6):
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        resultado1=numero1%numero2
        print(f"\t El resto de la división de estos dos numeros es: {resultado1}")
    
    elif(opc==7):
        numero1=int(input("Introduce el primer numero: "))
        numero2=int(input("Introduce el segundo numero: "))
        resultado1=numero1**numero2
        print(f"\t La división de estos dos numeros es: {resultado1}")
    
    elif(opc==8):
        print("\t Has elegido salir de la calculadora")
        
    else:
        print("ERROR")
#--------------------------------------V2 trabajo GitHub---------------------------------------------   
    #¿Como vamos a recorrer la lista "triangulos"? con un for
    #En cada iteracion tenemos una tupla, ya que cada elemento de la lista es una tupla formada por la base y la altura del triangulo (se trata de una lista de triangulos)
    triangulos=[(3,2), (1,5), (6,7)]
    listaCirculos=[3, 6, 1, 9, 5]
    rectangulos=[(3,2), (1,5), (6,7)]
    cuadrados=[4, 5, 7, 2, 8, 1, 6]
    opc=0
    while(opc!=12):
        print("Calculadora")
        print("Introduzca uno de los numeros")
        print("1.SUMA de numeros")
        print("2.RESTA de numeros")
        print("3.MULTIPLICACIÓN de numeros")
        print("4.DIVISIÓN de numeros")
        print("5.COCIENTE de la división")
        print("6.RESTO de la división")
        print("7.EXPONENCIACIÓN")
        print("8.Area de un triangulo")
        print("9.Area de un rectangulo")
        print("10.Area de un circulo")
        print("11.Area de un cuadrado")
        print("12.SALIR")
        opc=int(input("Eliga un numero de los anteriores "))
        while(opc<1 or opc>8):
            # print("Calculadora")
            # print("Introduzca uno de los numeros")
            # print("1.SUMA de numeros")
            # print("2.RESTA de numeros")
            # print("3.MULTIPLICACIÓN de numeros")
            # print("4.DIVISIÓN de numeros")
            # print("5.COCIENTE de la división")
            # print("6.RESTO de la división")
            # print("7.EXPONENCIACIÓN")
            # print("8.SALIR")
            # opc=int(input("Eliga un numero de los anteriores "))
        
            if(opc==1):
                    numero1=int(input("Introduce el primer numero: "))
                    numero2=int(input("Introduce el segundo numero: "))
                    resultado1=numero1+numero2
                    print(f"\t La suma de estos dos numeros es: {resultado1}")
                
            elif(opc==2):
                    numero1=int(input("Introduce el primer numero: "))
                    numero2=int(input("Introduce el segundo numero: "))
                    resultado1=numero1-numero2
                    print(f"\t La resta de estos dos numeros es: {resultado1}")
                
            elif(opc==3):
                    numero1=int(input("Introduce el primer numero: "))
                    numero2=int(input("Introduce el segundo numero: "))
                    resultado1=numero1*numero2
                    print(f"\t La multiplicación de estos dos numeros es: {resultado1}")
                    
            elif(opc==4):
                    numero1=int(input("Introduce el primer numero: "))
                    numero2=int(input("Introduce el segundo numero: "))
                    if(numero2==0):
                        print("El denominador no puede ser igual a 0")
                        resultado1=numero1/numero2
                        print(f"\t La división de estos dos numeros es: {resultado1}")
                    
            elif(opc==5):
                    numero1=int(input("Introduce el primer numero: "))
                    numero2=int(input("Introduce el segundo numero: "))
                    resultado1=numero1//numero2
                    print(f"\t El cociente de estos dos numeros es: {resultado1}")
                
            elif(opc==6):
                    numero1=int(input("Introduce el primer numero: "))
                    numero2=int(input("Introduce el segundo numero: "))
                    resultado1=numero1%numero2
                    print(f"\t El resto de la división de estos dos numeros es: {resultado1}")
                
            elif(opc==7):
                    numero1=int(input("Introduce el primer numero: "))
                    numero2=int(input("Introduce el segundo numero: "))
                    resultado1=numero1**numero2
                    print(f"\t La división de estos dos numeros es: {resultado1}")
                    
            elif(opc==8):
                for triangulo in triangulos: 
                    print(f"El area de un triangulo de base {triangulo[0]} y altura {triangulo[1]} es {triangulo[0]*triangulo[1]/2}")
            elif(opc==9):    
                for rectangulo in rectangulos:
                    #print(rectangulos)
                    #print(rectangulo[0]*rectangulo[1])
                    print(f"El area de un rectangulo de base {rectangulo[0]} y altura {rectangulo[1]} es {rectangulo[0]* rectangulo[1]}")
            elif(opc==10):   
                for radio in listaCirculos:
                    #print(radio)
                    #print(math.pi)
                    #pi=round(math.pi, 2)
                    print(f"El area de un circulo de  radio {radio} es {round(math.pi, 2)*radio**2}")
            elif(opc==11):    
                for lado in cuadrados:
                    print(f"El area de un cuadrado de lado {lado} es {lado**2}")
            else:
                print("No ha elegido un numero correcto")
                print("ERROR")
#--------------------------------------V2 trabajo GitHub---------------------------------------------   
nc=0
def sumar (x,y):
        print(f"la suma de {x} y {y} es: {x + y}")
def restar (x,y):
        print(f"la resta de {x} y {y} es: {x - y}")
def multiplicar (x,y):
        print(f"La multiplicación de {x} y {y} es: {x * y}")  
def dividir (x,y):
        if (y==0):
            print("El denominador no puede ser 0")
        print(f"La divisiÃón de {x} y {y} es: {x / y}")
def cociente (x,y):
        print(f"El cociente exacto de {x} y {y} es: {x // y}")
def resto (x,y):
        print(f"El resto de {x} y {y} es: {x % y}")
def exponente (x,y):
        print(f"El exponente de {x} y {y} es: {x ** y}")
def tri ():
        for triangulo in Listatriangulos:
            print(f"El área del triángulo {triangulo[0]} * {triangulo[1]} /2 es: {triangulo[0]*triangulo[1]/2}")
        print("\n")
def cuadrado ():
        for cuadrado in Listacuadrado:
            print(f"El área del cuadrado de lado {cuadrado} es: {cuadrado*cuadrado}")
def rectangulo ():
    for rectangulo in Listarectángulo:
        print(f"El área del rectángulo {rectangulo[0]} * {rectangulo[1]} es: {rectangulo[0]*rectangulo[1]}")
    print("\n")
def circulo ():
        for radio in Listacírculo:
            print(f"El área del círculo {radio} es: {round(math.pi, 2)*radio**2}")
        print("\n")
while (nc!=12):
    print("Calculadora")
    print("Introduzca uno de los siguientes números")
    print("1.Suma de 2 números")
    print("2.Resta de 2 números")
    print("3.Multiplicación de dos números")
    print("4.División de dos números")
    print("5.Cociente de dos números")
    print("6.Resto de la división de dos números")
    print("7.Exponente de dos números")
    #Añadimos areas a nuestra calculadora cientifica, las distancias de los lados ya definidas
    print("8.-Área de un triángulo")
    print("9.-Área de un cuadrado")
    print("10.-Área de un rectángulo")
    print("11.-Área de un círculo")
    nc=int(input("Introduzca uno de los números anteriores: "))
    while (nc<1 or nc>11):
        print("Calculadora")
        print("Introduzca uno de los siguientes números")
        print("1.Suma de 2 números")
        print("2.Resta de 2 números")
        print("3.Multiplicación de dos números")
        print("4.División de dos números")
        print("5.Cociente de dos números")
        print("6.Resto de la división de dos números")
        print("7.Exponente de dos números")
        print("8.-Área de un triángulo")
        print("9.-Área de un cuadrado")
        print("10.-Área de un rectángulo")
        print("11.-Área de un círculo")
        nc=int(input("Introduzca uno de los números anteriores: "))
    if (nc == 1):
            x=int(input("Escriba el primer número "))
            y=int(input("Escriba el segundo número "))
            sumar (x,y)
    elif (nc == 2):
            x=int(input("Escriba el primer número "))
            y=int(input("Escriba el segundo número "))
            restar (x,y)
    elif (nc == 3):
            x=int(input("Escriba el primer número "))
            y=int(input("Escriba el segundo número "))
            multiplicar (x,y)
    elif (nc == 4):
            x=int(input("Escriba el primer número "))
            y=int(input("Escriba el segundo número "))
            dividir (x,y)
    elif (nc == 5):
            x=int(input("Escriba el primer número "))
            y=int(input("Escriba el segundo número "))
            cociente (x,y)
    elif (nc == 6):
            x=int(input("Escriba el primer número "))
            y=int(input("Escriba el segundo número "))
            resto (x,y)
    elif (nc == 7):
            x=int(input("Escriba el primer número "))
            y=int(input("Escriba el segundo número "))
            exponente (x,y)
    elif (nc == 8):
            tri ()
    elif (nc == 9):
            cuadrado ()
    elif (nc == 10):
            rectangulo ()
    elif (nc == 11):
            circulo ()
    else:
        print("Ha elegido una opción incorrecta")
#----------------------------------------DATAFRAMES------------------------------------
import pandas as pd

#carga de los datos users:
userHeader = ['user_id', 'gender', 'age', 'ocupation', 'zip']
users = pd.read_table('d:/usuarios/Users/DavidCamposSerrano/Downloads/ml-1m/ml-1m/users.dat',
                       engine='python',
                       sep='::',
                       header=None,
                       names=userHeader)

print("Primeros 5 usuarios: \n%s" %users[:5])
# #guardar en txt como csv con separador ;
# users.to_csv('d:/usuarios/Users/DavidCamposSerrano/Downloads/ml-1m/ml-1m/MyUsers.csv', sep=';')

#carga de los datos ratings:
ratingsHeader = ['user_id', 'movie_id', 'rating',' timestamp']
ratings= pd.read_table('d:/usuarios/Users/DavidCamposSerrano/Downloads/ml-1m/ml-1m/ratings.dat',
                      engine='python',
                      sep='::',
                      header=None,
                      names=ratingsHeader)
print("Primeras 5 estadisticas: \n%s" %ratings[:5])

#carga de los datos movies:
moviesHeader = ['movie_id', 'title', 'genders']
movies= pd.read_table('d:/usuarios/Users/DavidCamposSerrano/Downloads/ml-1m/ml-1m/movies.dat',
                       engine='python',
                       sep='::',
                       header=None,
                       names=moviesHeader,
                       encoding='latin-1')
print("Primeras 5 pelis: \n%s" %movies[:5])
#vamos a juntar users con ratings
merge_users_ratings=pd.merge(users, ratings)
mergeTotal=pd.merge(merge_users_ratings, movies)
mergeTotal.to_csv('d:/usuarios/Users/DavidCamposSerrano/Downloads/ml-1m/ml-1m/Mymerge.csv', sep=';')
print(mergeTotal.loc[10])

#realizamos copia del DF Total
dfInicial=mergeTotal.copy()
dfInicial=dfInicial.groupby("title").size().sort_values(ascending=False)

#show avg ratings movie(groupby + avg)
avgRatings = mergeTotal.copy()
avgRatings = avgRatings.groupby(['movie_id', 'title']).mean()
print('Avg ratings: \n%s' % avgRatings['rating'][:10])

dataRating=mergeTotal.copy()
dataRating=dataRating.groupby(['movie_id', 'title'])['rating'].agg(['mean', 'sum', 'count', 'std'])

