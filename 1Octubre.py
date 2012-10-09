#!/usr/bin/python 
#(el -1 va a las entradas)
#Comparar activacion con 0

import random
from numpy import *

def main():
    miNumero = 0
    archivo = open('datos.txt', 'w')
    #umbral = .7
    #n = raw_input('Ingresa el valor de n: ')
    #x=array([1,2,3,4])
    #w=array([1.0,2.0,3.0,4.0])
    x = array([2.0, 1.0, 5.0])
    w = array([4.0, 3.5, 4.9])
    #multiplicacion=array([1.0,2.0,3.0,4.0])
    multiplicacion = array([4.2, 4.1 ,2.1])
    #valor = w + x
    suma = 0.0
    sumaTotal = 0.0

    LOW = -1
    HIGH = 1
    
    i = 0
    j = 0
    while j<49:
        while i < 2:
        
            if(i == 2):
                x[i] = -1
            x[i] = random.uniform(LOW, HIGH)
            w[i] = random.uniform(LOW,HIGH)
            multiplicacion[i] = w[i]*x[i]
            suma = suma + multiplicacion[i]
            '''print "\nVuelta numero = ", i
            print "Esto es x[i] = ", x[i]
            print "Esto es w[i] = ", w[i]
            print "Esto es multiplicacion = ", multiplicacion[i]
            print "Esto es suma = ", suma
            '''
            i = i+1
        
    #print "Esto es suma final == ", suma
            if (suma >= 0):
        #print "\n\nSalida == ", 1, ":)\n"
                miNumero = 1
            else:
        #print "\n\nSalida == ", 0, ":(\n"
                miNumero = 0    
        print x[0],"\t", x[1], "\t", miNumero, "\n"
        j = j + 1
    

main()
