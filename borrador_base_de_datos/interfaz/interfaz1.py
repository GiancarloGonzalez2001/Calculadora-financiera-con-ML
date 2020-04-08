# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:43:12 2020

@author: gianc
"""

import tkinter as tk 
mainW = tk.Tk()
mainW.title("Bienvenido a la calculadora financiera")
mainW.geometry("7000x7000")
mainW.configure(bg = "white")
var = tk.StringVar(mainW)
var.set("Seleccione")
opciones =["Pagar iva bimestral o cuatrimestralmente","Consultas acerca del pago de la retención en la fuente",
           "Para saber si usted es declarante de renta","Conocer el valor futuro","Conocer la tasa de interés",
           " Obtener ganancia con un CDT","Conocer los intereses que debe pagar por un crédito"]
opcion = tk.OptionMenu(mainW,var,*opciones)
opcion.config(width=60)
opcion.pack(padx = 20,pady=20)
e1 = tk.Label(mainW, text="opcion seleccionada",bg="white",fg= "black" )
e1.pack(padx = 5,pady=5,ipadx=5,ipady=5 ) 
e2 = tk.Label(mainW,bg = "red",textvariable=var,padx=5,pady=5)
e2.pack() 





mainW.mainloop()