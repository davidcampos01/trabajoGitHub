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

print("1.Area de un triangulo")
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
    

    
