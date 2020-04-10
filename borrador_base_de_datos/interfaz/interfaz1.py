# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:43:12 2020

@author: Giancarlo Gonzalez
"""
from tkinter import *
import tkinter as tk 

#===============================================================================================================================================================================================
#                               Caracteristicas de la pagina 
#===============================================================================================================================================================================================
mainW = tk.Tk()
mainW.title("Calculadora financiera")
mainW.geometry("700x700")
mainW.configure(bg = "lavender")
mainW.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')   
#===============================================================================================================================================================================================
#                                       titulo
#===============================================================================================================================================================================================
tt = tk.Label(mainW, text="Bienvenido ",bg="lavender",fg= "black",font = ("Brodway", 20) )
tt.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X  ) 

#===============================================================================================================================================================================================
#                                     Funciones
#===============================================================================================================================================================================================

#                                    Ventana IVA   
def ventanaiva():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular su iva",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    e2=tk.Label(win,text="Digite sus ingresos netos",bg="royal blue",fg= "white",font = ("vernada", 15))
    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    entrada1=tk.Entry(win)
    entrada1.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    def iva():
        a =(int(entrada1.get())/34270)
        if a>92000:
            e3=tk.Label(win,text="Usted debe pagar IVA bimestralmente",bg="royal blue",fg= "black",font = ("vernada", 15))
            e3.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        else:
            e3=tk.Label(win,text="Usted debe pagar IVA cuatrimestralmente",bg="royal blue",fg= "black",font = ("vernada", 15))
            e3.pack(padx = 5,pady=10,ipadx=5,ipady=10)
            
    calcular=tk.Button(win,text="Calcular",command=iva)
    calcular.pack(side=tk.TOP,padx=30,pady=30)
    calcular.configure(font=30)
#                                   Ventana retencion
def ventanaretencion():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular su retencion de fuente",bg="royal blue",fg= "white",font = ("vernada", 15))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    def compras():
        win.destroy()
        win1 = tk.Toplevel()
        win1.geometry("700x700")
        win1.configure(bg="lavender")
        win1.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
        e1 = tk.Label(win1,text="Ingrese el valor de la base de la compra para responsable del iva:",bg="royal blue",fg= "white",font = ("vernada", 15))
        e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
        entrada1=(tk.Entry(win1))
        entrada1.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        def pago_provedor():
            resultado_1 = tk.StringVar()
            iva=(int(entrada1.get())*0.19)
            if int(entrada1.get())>0:
                uvt_1=(int(entrada1.get())/34270)
                #print(uvt_1)
                if uvt_1>27:
                    com_iva=int(entrada1.get())+iva
                    resultado_1=str(com_iva-(int(entrada1.get())*0.035))
                    e2=tk.Label(win1,text="El valor del pago al provedor es: ",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
                    print(resultado_1)
                    e3=tk.Label(win1,text=resultado_1, padx = 5,pady=10,width=50)
                    e3.pack()
                else:
                    tk.messagebox.showwarning("error","ingrese nuevamente los datos")

            else:
                tk.messagebox.showwarning("error","ingrese nuevamente los datos")
        calcular=tk.Button(win1,text="Calcular",command=pago_provedor)
        calcular.pack(side=tk.TOP,padx=30,pady=30)
        calcular.configure(font=30)
        
    def servicios():
        win1 = tk.Toplevel()
        win1.geometry("700x700")
        win1.configure(bg="lavender")
        win1.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
        e1 = tk.Label(win1,text="Ingrese el valor de la base de la prestación del servicio: ",bg="royal blue",fg= "white",font = ("vernada", 15))
        e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
        entrada1=(tk.Entry(win1))
        entrada1.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        def valorapagar():
            resultado_1 = tk.StringVar()
            iva=(int(entrada1.get())*0.19)
            if int(entrada1.get())>0:
                uvt_1=(int(entrada1.get())/34270)
                if uvt_1>4:
                    com_iva=int(entrada1.get())+iva
                    resultado_1=str(com_iva-(int(entrada1.get())*0.04))
                    e2=tk.Label(win1,text="El valor neto del pago de servicios es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
                    e3=tk.Label(win1,text=resultado_1, padx = 5,pady=10,width=50)
                    e3.pack()
                if uvt_1<4:
                    resultado_final = ((int(entrada1.get())*0.19)+int(entrada1.get()))
                    e2=tk.Label(win1,text="El valor a pagar es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
                    e3=tk.Label(win1,text=resultado_final, padx = 5,pady=10,width=50)
                    e3.pack()
                    
                else:
                    tk.messagebox.showwarning("error","ingrese nuevamente los datos")

            else:
                tk.messagebox.showwarning("error","ingrese nuevamente los datos")
        calcular=tk.Button(win1,text="Calcular",command=valorapagar)
        calcular.configure(font=30)
        calcular.pack(side=tk.TOP,padx=30,pady=30) 
    def honorarios():
        win1 = tk.Toplevel()
        win1.geometry("700x700")
        win1.configure(bg="lavender")
        win1.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
        e1 = tk.Label(win1,text="Ingrese el valor de la base de la prestación del servicio: ",bg="royal blue",fg= "white",font = ("vernada", 15))
        e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
        entrada1=(tk.Entry(win1))
        entrada1.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        def pago_profesional():
            resultado_1 = tk.StringVar()
            iva=(int(entrada1.get())*0.19)
            if int(entrada1.get())>0:
                uvt_1=(int(entrada1.get())/34270)
                if uvt_1>0:
                    com_iva=int(entrada1.get())+iva
                    resultado_1=str(com_iva-(int(entrada1.get())*0.10))
                    e2=tk.Label(win1,text="El valor del pago al profesional es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
                    e3=tk.Label(win1,text=resultado_1, padx = 5,pady=10,width=50)
                    e3.pack()
                else:
                    tk.messagebox.showwarning("error","ingrese nuevamente los datos")

            else:
                tk.messagebox.showwarning("error","ingrese nuevamente los datos")
        calcular=tk.Button(win1,text="Calcular",command=pago_profesional)
        calcular.configure(font=30)
        calcular.pack(side=tk.TOP,padx=30,pady=30)

#                           menu desplegable retencion   
    mb1 = tk.Menubutton(win,text="Funciones")
    mb1.menu = tk.Menu(mb1)
    mb1["menu"] = mb1.menu
    mb1.menu.add_command(label="Retención en la fuente de compras",command = compras)
    mb1.menu.add_command(label="Retención de servicios",command = servicios )
    mb1.menu.add_command(label="Retencion de honorarios",command = honorarios )
    mb1.pack(padx=30,pady=30)
    mb1.configure(font=30)
    mb1.pack()
    
def ventanarenta():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para saber si es declarante de renta",bg="lavender",fg= "black",font = ("vernada", 15))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    i1 = tk.Label(win,text="Ingrese el valor de su patrimonio bruto en el último año:  ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e2=tk.Entry(win)
    e2.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el valor de sus compras y consumos totales en el último año: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e3=tk.Entry(win)
    e3.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el valor de sus ingresos brutos en el último año: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e4=tk.Entry(win)
    e4.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el valor total entre consignaciones, \n depósitos o inversiones que haya hecho en el último años:  ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e5=tk.Entry(win)
    e5.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el valor en consumos con tarjeta de crédito en el último año:  ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e6=tk.Entry(win)
    e6.pack(ipadx=5,ipady=5)
    def renta():
        if int(e2.get())>=149202000 or int(e3.get())>=46418000 or int(e4.get())>=46418000 or int(e5.get())>=46418000 or int(e6.get())>=46418000:
            e7=tk.Label(win,text="Usted es declarante de renta",bg="royal blue",fg= "black",font = ("vernada", 15))
            e7.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        else:
            e7=tk.Label(win,text="Usted NO es declarante de renta",bg="royal blue",fg= "black",font = ("vernada", 15))
            e7.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    calcular=tk.Button(win,text="Calcular",command=renta)
    calcular.configure(font=30)
    calcular.pack(side=tk.TOP,padx=30,pady=30)

def ventanavalorFuturo():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular el valor futuro",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    i1 = tk.Label(win,text="Ingrese la cantidad a solicitar de préstamo: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e2=tk.Entry(win)
    e2.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese la tasa de interés: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e3=tk.Entry(win)
    e3.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el tiempo a calcular en meses: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e4=tk.Entry(win)
    e4.pack(ipadx=5,ipady=5)
    def v_futuros(e2,e3,e4):
        vfuturo=int(e2.get())*(1+int(e3.get())**int(e4.get()))
        e2=tk.Label(win,text="El valor futuro es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
        e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        e3=tk.Label(win,text=vfuturo, padx = 5,pady=10,width=50)
        e3.pack()
    
    calcular=tk.Button(win,text="Calcular",command=v_futuros(e2,e3,e4))
    calcular.pack(side=tk.TOP,padx=30,pady=30)
    calcular.configure(font=30)

def ventanaCDT():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular sus ganacias con un CDT",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    calcular=tk.Button(win,text="Calcular")
    calcular.pack(side=tk.TOP)
    
def ventanaICredito():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular los intereses de un credito",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    calcular=tk.Button(win,text="Calcular")
    calcular.pack(side=tk.TOP)
    
def ventanatasaI():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular la tasa de interes",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    calcular=tk.Button(win,text="Calcular")
    calcular.pack(side=tk.TOP)
    
#===============================================================================================================================================================================================
#                                    Etiquetas
#===============================================================================================================================================================================================
e1 = tk.Label(mainW,text="Acontinuación encontrará una serie de funcoines, escoja la que desea consultar",bg="royal blue",fg="white",font=15 )
e1.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    

#===============================================================================================================================================================================================
#                                 Menu desplegable 
#===============================================================================================================================================================================================
mb = tk.Menubutton(mainW,text="Funciones")
mb.menu = tk.Menu(mb)
mb["menu"] = mb.menu
#Opciones
mb.menu.add_command(label="Pagar iva bimestral o cuatrimestralmente",command = ventanaiva )
mb.menu.add_command(label="Consultas acerca del pago de la retención en la fuente",command = ventanaretencion )
mb.menu.add_command(label="Saber si usted es declarante de renta",command = ventanarenta )
mb.menu.add_command(label="Conocer el valor futuro",command = ventanavalorFuturo )
mb.menu.add_command(label=" Obtener ganancia con un CDT",command = ventanaCDT )
mb.menu.add_command(label="Conocer los intereses que debe pagar por un crédito",command = ventanaICredito )
mb.menu.add_command(label="Conocer la tasa de interés",command = ventanatasaI )
mb.configure(font=20)
mb.pack(side=tk.TOP,padx=30,pady=30)





mainW.mainloop()