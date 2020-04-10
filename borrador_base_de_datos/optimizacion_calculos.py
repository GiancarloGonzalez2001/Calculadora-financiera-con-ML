# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:11:19 2020

@author: gianc
"""

import math as mt
import numpy as np
import matplotlib.pyplot as plt
#Mensaje que le pide al usuario escoger las diferentes funciones del programa
def funcionprincipal(introduccion):
    if introducción=="0":
        print("Gracias por utilizar este programa.")
    else:
        print("error")
introducción=(input("Bienvenido. Esta es una calculadora financiera.IMPORTANTE: si al colocar el numero correspondiente vuelva a salir este mensaje, vuelva a ponerlo y hágalo hasta que el programa le pida otros datos. Le aseeguro que no serán más de 7 veces las que tenga que repetir este proceso. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor futuro presione 4. Para conocer la tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: "))
funcionprincipal(introducción)    



var = tk.StringVar(mainW)
var.set("Seleccione")
opciones =["Pagar iva bimestral o cuatrimestralmente","Consultas acerca del pago de la retención en la fuente",
           "Saber si usted es declarante de renta","Conocer el valor futuro","Conocer la tasa de interés",
           " Obtener ganancia con un CDT","Conocer los intereses que debe pagar por un crédito"]
opcion = tk.OptionMenu(mainW,var,*opciones)
opcion.config(width=60)
opcion.pack(padx = 20,pady=20)