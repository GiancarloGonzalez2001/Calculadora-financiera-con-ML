#se importan los mÃ³dulos a utilizar
from tkinter import *
import tkinter as tk 
from math import *
import math as mt
import sympy as sp
from matplotlib import pyplot


#===============================================================================================================================================================================================
#                               Caracteristicas de la pagina 
#===============================================================================================================================================================================================
mainW = tk.Tk()
mainW.title("Calculadora financiera")
mainW.geometry("700x700")
mainW.resizable(width=False, height=False)
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
    win.resizable(width=False, height=False)
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular el pago de iva",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    e2=tk.Label(win,text="Digite sus ingresos brutos",bg="royal blue",fg= "white",font = ("vernada", 15))
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
            
    e3=tk.Label(win,text="Para mayor información, consultar el art. 601 E.T.",bg="royal blue",fg= "black",font = ("vernada", 15))
    e3.pack(padx = 5,pady=10,ipadx=10,ipady=15)
    
    calcular=tk.Button(win,text="Calcular",command=iva)
    calcular.pack(side=tk.TOP,padx=30,pady=30)
    calcular.configure(font=30)
#################################################################################################################################################################                                                                                                  
def ventanaconvertidor():
    win = tk.Toplevel()
    win.geometry("800x800")
    win.resizable(width=False, height=False)
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para convertir tasas de interés vencidas",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    e10 = tk.Label(win,text="Para realizar la conversión siga las siguientes instrucciones"
                   "\n Se le solicitarán 3 datos: "
                   "\n El primero es el porcentaje actual "
                   "\n El segundo es el numero de veces que aparece el tiempo en un año de su tasa actual"
                   "\n Y el tercero es el numero de veces que aparece el tiempo en un año de la tasa que desea obtener ",bg="royal blue",fg="white",font=15 )
    e10.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    e11 = tk.Label(win,text="Ejemplo"
                   "\n Si tiene una tasa de 4% efectiva trimestral vencida y quiere pasarla a efectiva mensual vencida,"
                   "\n los datos que deberá ingresar son 4,4,12 respectivamente"
                   "\n (4%, 4 trimestres que tiene un año y 12 meses del año)",bg="royal blue",fg="white",font=15 )
    e11.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    entrada1=(tk.Entry(win))
    entrada1.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    entrada2=(tk.Entry(win))
    entrada2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    entrada3=(tk.Entry(win))
    entrada3.pack(padx = 5,pady=10,ipadx=5,ipady=10)
    def convertidor():
        resultado=tk.StringVar()
        a=int(entrada1.get())/100
        b=int(entrada2.get())
        c=int(entrada3.get())
        
        if a and b and c > 0:
            r=((1+a)**(b/c))-1
            resultado=str(r*100)
            e2=tk.Label(win,text="resultado",bg="royal blue",fg= "black",font = ("vernada", 15))
            e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
            e3=tk.Label(win,text=resultado, padx = 5,pady=10,width=50)
            e3.pack()
            e2=tk.Label(win,text="%",bg="royal blue",fg= "black",font = ("vernada", 15))
            e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
            e3=tk.Label(win,text=resultado, padx = 5,pady=10,width=50)
            e3.pack()
        else:
            tk.messagebox.showwarning("error","ingrese nuevamente los datos")  
    calcular=tk.Button(win,text="Convertir",command=convertidor)
    calcular.pack(side=tk.TOP,padx=30,pady=30)
    calcular.configure(font=30)
        
    
######################################################################################################################################################
def ventanaretencion():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.resizable(width=False, height=False)
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular su retencion de fuente",bg="lavender",fg= "black",font = ("vernada", 15))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    e10 = tk.Label(win,text="A continuación encontrará una serie de funciones, escoja la que desea consultar",bg="royal blue",fg="white",font=15 )
    e10.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X)

    def compras():
        win.destroy()
        win1 = tk.Toplevel()
        win1.geometry("700x700")
        win1.resizable(width=False, height=False)
        win1.configure(bg="lavender")
        win1.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
        e1 = tk.Label(win1,text="Ingrese el valor de la base de la compra para responsable del iva:",bg="royal blue",fg= "white",font = ("vernada", 15))
        e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
        entrada1=(tk.Entry(win1))
        entrada1.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        def pago_provedor():
            uvt=34270
            resultado_1 = tk.StringVar()
            iva=(int(entrada1.get())*0.19)
            if int(entrada1.get())>0:
                uvt_1=(int(entrada1.get())/uvt)
                #print(uvt_1)
                if uvt_1>=27:
                    com_iva=int(entrada1.get())+iva
                    resultado_1=float(com_iva-(int(entrada1.get())*0.025))
                    r1=round(resultado_1)
                    resultado_2=float(com_iva-(int(entrada1.get())*0.035))
                    r2=round(resultado_2)
                    e2=tk.Label(win1,text="Si usted es declarante de renta, el valor del pago al provedor es: ",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
                    e3=tk.Label(win1,text=("$",r1), padx = 5,pady=10,width=50)
                    e3.pack()
                    e4=tk.Label(win1,text="Si usted NO es declarante de renta, el valor del pago al provedor es: ",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e4.pack(padx = 5,pady=10,ipadx=5,ipady=10)
                    e5=tk.Label(win1,text=("$",r2), padx = 5,pady=10,width=50)
                    e5.pack()
                else:
                    e4=tk.Label(win1,text="Usted no debe aplicar retención",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e4.pack(padx = 5,pady=10,ipadx=5,ipady=10)

            else:
                tk.messagebox.showwarning("error","ingrese nuevamente los datos")
        calcular=tk.Button(win1,text="Calcular",command=pago_provedor)
        calcular.pack(side=tk.TOP,padx=30,pady=30)
        calcular.configure(font=30)
        
    def servicios():
        win1 = tk.Toplevel()
        win1.geometry("700x700")
        win1.resizable(width=False, height=False)
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
                    e2=tk.Label(win1,text="No aplica retención",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)

                    
                else:
                    e4=tk.Label(win1,text="Usted no debe aplicar retención",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e4.pack(padx = 5,pady=10,ipadx=5,ipady=10)

            else:
                tk.messagebox.showwarning("error","ingrese nuevamente los datos")
        calcular=tk.Button(win1,text="Calcular",command=valorapagar)
        calcular.configure(font=30)
        calcular.pack(side=tk.TOP,padx=30,pady=30) 
    def honorarios():
        win1 = tk.Toplevel()
        win1.geometry("700x700")
        win1.resizable(width=False, height=False)
        win1.configure(bg="lavender")
        win1.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
        e1 = tk.Label(win1,text="Ingrese el valor de la base de la prestación del servicio profesional: ",bg="royal blue",fg= "white",font = ("vernada", 15))
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
                    resultado_2=str(com_iva-(int(entrada1.get())*0.11))
                    e2=tk.Label(win1,text="Si es persona jurídica, el valor del pago al profesional es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e2.pack(padx = 5,pady=10,ipadx=5,ipady=10)
                    e3=tk.Label(win1,text=resultado_1, padx = 5,pady=10,width=50)
                    e3.pack()
                    e9=tk.Label(win1,text="Si es persona natural, el valor del pago al profesional es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e9.pack(padx = 5,pady=10,ipadx=5,ipady=10)
                    e8=tk.Label(win1,text=resultado_2, padx = 5,pady=10,width=50)
                    e8.pack()
                else:
                    e4=tk.Label(win1,text="Usted no debe aplicar retención",bg="royal blue",fg= "black",font = ("vernada", 15))
                    e4.pack(padx = 5,pady=10,ipadx=5,ipady=10)

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
    mb1.menu.add_command(label="Retención de honorarios",command = honorarios )
    mb1.pack(padx=30,pady=30)
    mb1.configure(font=30)
    mb1.pack()
################################################################################################################################################################    
def ventanarenta():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.resizable(width=False, height=False)
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para saber si usted es declarante de renta \n Para el año inmediatemente anterior",bg="lavender",fg= "black",font = ("vernada", 15))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    i1 = tk.Label(win,text="Ingrese el valor de su patrimonio bruto en el ultimo año:  ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e2=tk.Entry(win)
    e2.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el valor de sus compras y consumos totales en el ultimo año: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e3=tk.Entry(win)
    e3.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el valor de sus ingresos brutos en el ultimo año: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e4=tk.Entry(win)
    e4.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el valor total entre consignaciones, \n depositos o inversiones que haya hecho en el último año:  ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e5=tk.Entry(win)
    e5.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el valor en consumos con tarjeta de credito en el último año:  ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e6=tk.Entry(win)
    e6.pack(ipadx=5,ipady=5)
    def renta():
        uvt=34270
        v2=int(e2.get())/uvt
        v3=int(e3.get())/uvt
        v4=int(e4.get())/uvt
        v5=int(e5.get())/uvt
        v6=int(e6.get())/uvt
        if v2>=4500 or v3>=1400 or v4>=1400 or v5>=1400 or v6>=1400:
            e7=tk.Label(win,text="Usted es declarante de renta",bg="royal blue",fg= "black",font = ("vernada", 15))
            e7.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        else:
            e7=tk.Label(win,text="Usted NO es declarante de renta",bg="royal blue",fg= "black",font = ("vernada", 15))
            e7.pack(padx = 5,pady=10,ipadx=5,ipady=10)
            
    calcular=tk.Button(win,text="Calcular",command=renta)
    calcular.configure(font=30)
    calcular.pack(side=tk.TOP,padx=30,pady=30)
################################################################################################################################################################
def ventanainterescompuesto():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.resizable(width=False, height=False)
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular intereses",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    c1=tk.IntVar()
    c2=tk.IntVar()
    c3=tk.IntVar()
    i1 = tk.Label(win,text="Ingrese la cantidad a solicitar de préstamo o inversión: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e2=tk.Entry(win,textvariable=c1)
    e2.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese la tasa de interés anual",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)  
    i8 = tk.Label(win,text="Si necesita ayuda para convertir la tasa, por favor diríjase al apartado de convertidor de tasa",bg="royal blue",fg= "white",font = ("vernada", 12))
    i8.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    e3=tk.Entry(win,textvariable=c2)
    e3.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese el tiempo a calcular en años: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e4=tk.Entry(win,textvariable=c3)
    e4.pack(ipadx=5,ipady=5)
    def v_futuros():
        a = int(e2.get())
        b = int(e3.get())/100
        c = int(e4.get())
        try:
            interes_c= a*((1+b)**c-1)
            i=round(interes_c)
            interes_comp=interes_c+a
            i_comp=round(interes_comp)
            e7=tk.Label(win,text="El valor total recibido o pagado es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
            e7.pack(padx = 5,pady=10,ipadx=5,ipady=10)
            e8=tk.Label(win,text=("$",i_comp), padx = 5,pady=10,width=50)
            e8.pack()
            e9=tk.Label(win,text="El valor del interés recibido o pagado es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
            e9.pack(padx = 5,pady=10,ipadx=5,ipady=10)
            e10=tk.Label(win,text=("$",i), padx = 5,pady=10,width=50)
            e10.pack()
        except:
            tk.messagebox.showwarning("error","ingrese nuevamente los datos")
            
    
    calcular=tk.Button(win,text="Calcular",command=v_futuros)
    calcular.pack(side=tk.TOP,padx=30,pady=30)
    calcular.configure(font=30)
################################################################################################################################################################
def ventanaCDT():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.resizable(width=False, height=False)
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular el tiempo",bg="lavender",fg= "black",font = ("vernada", 15))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    c1=tk.IntVar()
    c2=tk.IntVar()
    c3=tk.IntVar()
    i1 = tk.Label(win,text="Ingrese valor que quiere recibir: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e2=tk.Entry(win,textvariable=c1)
    e2.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese valor actual o que va a invertir: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e3=tk.Entry(win,textvariable=c2)
    e3.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese la tasa de interés bimestral",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X) 
    i8 = tk.Label(win,text="Si necesita ayuda para convertir la tasa, por favor diríjase al apartado de convertidor de tasa",bg="royal blue",fg= "white",font = ("vernada", 12))
    i8.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    e4=tk.Entry(win,textvariable=c3)
    e4.pack(ipadx=5,ipady=5)
    def calculoT():
        try:
            a = int(e2.get())
            b = int(e3.get())
            c = int(e4.get())/100
            c_tiempo=(mt.log(a/b))/(mt.log(1+c))
            c_t=round(c_tiempo)
            e7=tk.Label(win,text="El tiempo es de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
            e7.pack(padx = 5,pady=10,ipadx=5,ipady=10)
            e8=tk.Label(win,text=(c_t,"Bimestres"), padx = 5,pady=10,width=50)
            e8.pack()
        except:
            tk.messagebox.showwarning("error","ingrese nuevamente los datos")
    calcular=tk.Button(win,text="Calcular",command=calculoT)
    calcular.configure(font=30)
    calcular.pack(side=tk.TOP,padx=30,pady=30)

################################################################################################################################################################    
def ventanavalorfuturo():
    win = tk.Toplevel()
    win.geometry("700x700")
    win.resizable(width=False, height=False)
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    e1 = tk.Label(win,text="Bienvenido al apartado para calcular el valor futuro",bg="lavender",fg= "black",font = ("vernada", 20))
    e1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    c1=tk.IntVar()
    c2=tk.IntVar()
    c3=tk.IntVar()
    i1 = tk.Label(win,text="Ingrese el valor presente: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e2=tk.Entry(win,textvariable=c1)
    e2.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese la tasa de interés mensual: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    i8 = tk.Label(win,text="Si necesita ayuda para convertir la tasa, por favor diríjase al apartado de convertidor de tasa",bg="royal blue",fg= "white",font = ("vernada", 12))
    i8.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    e3=tk.Entry(win,textvariable=c2)
    e3.pack(ipadx=5,ipady=5)
    i1 = tk.Label(win,text="Ingrese los meses a calcular: ",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)    
    e4=tk.Entry(win,textvariable=c3)
    e4.pack(ipadx=5,ipady=5)
    def t_interes():
        a = int(e2.get())
        b = int(e3.get())/100
        c = int(e4.get())
        v = a*(1+b)**c
        vf=round(v)
        e7=tk.Label(win,text="En el tiempo introducido, el valor futuro será de: ",bg="royal blue",fg= "black",font = ("vernada", 15))
        e7.pack(padx = 5,pady=10,ipadx=5,ipady=10)
        e8=tk.Label(win,text=("$",vf), padx = 5,pady=10,width=50)
        e8.pack()
    calcular=tk.Button(win,text="Calcular",command=t_interes)
    calcular.configure(font=30)
    calcular.pack(side=tk.TOP,padx=30,pady=30)

# #############################################################################################################################################
def ventana_calculadora_basica():

    ventana = tk.Toplevel()
    ventana.title("Calculadora básica")
    ventana.geometry("400x550")
    ventana.resizable(width=False, height=False)
    ventana.configure(background="lavender")
    ventana.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
    tk.messagebox.showwarning("Atención!","Es importante tener en cuenta los parentesis para Exp o Sqrt\n Ej: Exp(n) o sqrt(n)")
    #Código adaptado de https://github.com/DavidArmendariz/YouTube-Codes. Las funciones para la calculadora básica se adaparon a nuestro caso en base a ese código
    color_boton="red"
    ancho_boton=10
    alto_boton=3
    operador = ""
    texto_pantalla = tk.StringVar()
    def clear():
        global operador
        operador = ""
        texto_pantalla.set("0")
    def click(b):
        global operador
        operador += str(b)
        texto_pantalla.set(operador)
    def resultado():
        global operador
        try:
            r = str(eval(operador))
        except:
            r = "ERROR"
        texto_pantalla.set(r)
        
    clear()
#primera fila
    Boton7 = Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(7)).grid(row=1,column=0,pady=10)

    Boton8 = Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(8)).grid(row=1,column=1,pady=10)

    Boton9 = Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(9)).grid(row=1,column=2,pady=10)

    BotonDiv = Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("/")).grid(row=1,column=3,pady=10)    
                    
#segunda fila
    Boton4 = Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(4)).grid(row=2,column=0,pady=10)
    
    Boton5 = Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(5)).grid(row=2,column=1,pady=10)

    Boton6 = Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(6)).grid(row=2,column=2,pady=10)

    BotonMult = Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("*")).grid(row=2,column=3,pady=10)

#tercera fila
    Boton1 = Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(1)).grid(row=3,column=0,pady=10)

    Boton2 = Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(2)).grid(row=3,column=1,pady=10)

    Boton3 = Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(3)).grid(row=3,column=2,pady=10)

    BotonResta = Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("-")).grid(row=3,column=3,pady=10)
    
#cuarta fila
    BotonPunto = Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(".")).grid(row=4,column=0,pady=10)
    
    Boton0 = Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(0)).grid(row=4,column=1,pady=10)

    BotonMod = Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("%")).grid(row=4,column=2,pady=10)

    BotonSuma = Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("+")).grid(row=4,column=3,pady=10)
#quinta fila
    BotonParenIzq = Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("(")).grid(row=5,column=0,pady=10)
    
    BotonParenDer = Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click(")")).grid(row=5,column=1,pady=10)
    
    BotonClear = Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).grid(row=5,column=2,pady=10)
    
    BotonEXP = Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("exp")).grid(row=5,column=3,pady=10)

#sexta fila
    BotonPi = Button(ventana,text="pi",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("pi")).grid(row=6,column=0,pady=10)
    
    BotonRaiz = Button(ventana,text="sqrt",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:click("sqrt")).grid(row=6,column=1,pady=10)
    
    BotonIgual = Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).grid(row=6,column=2,pady=20)
    
#se crea la pantalla de la calculadora   
    Pantalla = Entry(ventana,font=("arial",20,"bold"),width=22,borderwidth=10,background="yellow",textvariable=texto_pantalla)
    Pantalla.grid(row=0,column=0,columnspan=4,padx=20,pady=20)
    
    ventana.mainloop()
#===========================================================================================================================================================
def cal_derivadas():
    win = tk.Toplevel()
    win.geometry("700x600")
    win.resizable(width=False, height=False)
    win.configure(bg="lavender")
    win.iconbitmap(r'q5970meyn6ddojdz1wno81586489001_NEv_icon.ico')
#    imagen3 = tk.PhotoImage(file="images1.png")
#    lbimagen3 = tk.Label(win, image=imagen3)
#    lbimagen3.place(x=0, y=200)
    texto1 = tk.Label(win,text="Calculadora que obtiene derivadas",bg="lavender",fg= "black",font = ("vernada", 20))
    texto1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    i1 = tk.Label(win,text="Ingrese su función utilizando * para indicar multilicación y ** para indicar potencia. Ejemplo: 2*x**2",bg="royal blue",fg= "white",font = ("vernada", 12))
    i1.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    i2 = tk.Label(win,text="Si ingresa un texto, le será retornado el valor 1",bg="royal blue",fg= "white",font = ("vernada", 12))
    i2.pack(padx = 5,pady=10,ipadx=5,ipady=10,fill=tk.X)
    woo=tk.StringVar()
    x= sp.symbols("x")
    pant=tk.Entry(win,textvariable=woo)
    pant.pack(ipadx=5,ipady=5)

    def derivar():
        y=str(pant.get())
        global imagen4
        global d
        try:
            d=sp.diff(y)
            new = sp.sympify(d)
            m = range(-10,10)
            # Graficar ambas funciones.
            pyplot.plot(m, [new.subs(x,i) for i in m])
            # Establecer el color de los ejes.
            pyplot.axhline(0, color="black")
            pyplot.axvline(0, color="black")
            # Limitar los valores de los ejes.
            pyplot.xlim(-10, 10)
            pyplot.ylim(-10, 10)
            # Guardar gráfico como imágen PNG.
            pyplot.savefig("output.png")
            # Mostrarlo.
            pyplot.show()
            der=tk.Label(win,text=(d),bg ="royal blue", padx = 5,pady=10,width=50)
            der.pack()
            win.update()
            #lbimagen2.pack()
            
        except:
            tk.messagebox.showwarning("error","ingrese nuevamente la función. Recuerde que la forma de entrada es con un * para indicar multiplicación y con ** para indicar potencia")
    def Refresher():
        global imagen4
        global d
        win.after(1000, Refresher) # every second...
#        der=tk.Label(win,text=(d),bg ="royal blue", padx = 5,pady=10,width=50)
#        der.place(x=200, y=200)
#        der.pack()
        imagen4 = tk.PhotoImage(file="output.png")
        lbimagen4 = tk.Label(win, image=imagen4)
        lbimagen4.place(x=130, y=300)        
    calcular_der=tk.Button(win,text="derivada",fg= "blue",command=(derivar))
    calcular_der.pack(side=tk.TOP)
       
    Refresher()
    win.mainloop()
    
# #===============================================================================================================================================================================================
#                                    Etiquetas
#===============================================================================================================================================================================================
e1 = tk.Label(mainW,text="Esta no es una calculadora normal, aquí encontra una calculadora"
                          " financiera \n en la que podrá realizar diferentes operaciones enfocadas al sector financiero, \n"
                          "también encontrará una calculadora matemática con las operaciones \n tradicionales y además con otra que deriva cualquier función introducida." 
                          "\n A continuación encontrará unas funciones, oprima la que desea consultar ",bg="royal blue",fg="white",font=17 )
e1.pack(padx = 5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    

#===============================================================================================================================================================================================
#                                 Menu desplegable 
#===============================================================================================================================================================================================
#calculadora financiera
mb = tk.Menubutton(mainW,text="Calculadora Financiera")

mb.menu = tk.Menu(mb)
mb["menu"] = mb.menu
#Opciones
mb.menu.add_command(label="Convertidor de tasas",command = ventanaconvertidor )
mb.menu.add_command(label="Pagar iva bimestral o cuatrimestralmente (empresas)",command = ventanaiva )
mb.menu.add_command(label="Valor a pagar y aplicación de la retención en la fuente",command = ventanaretencion )
mb.menu.add_command(label="Saber si usted es declarante de renta",command = ventanarenta )
mb.menu.add_command(label="Conocer el valor futuro de una inversión o un préstamo",command = ventanavalorfuturo )
mb.menu.add_command(label="Calcular el interés cobrado en el préstamo o recibido en la inversión",command = ventanainterescompuesto)
mb.menu.add_command(label="Calcular el tiempo de una inversión o préstamo para obtener beneficios o pagos",command = ventanaCDT )
mb.configure(font=20)
mb.pack(side=tk.TOP,padx=30,pady=30)
mb.place(x=425,y=250)
#calculadora matemática
cal_m=tk.Menubutton(mainW,text="Calculadora matemática")
cal_m.pack(side=tk.TOP,padx=30,pady=30)
cal_m.place(x=100,y=250)
cal_m.configure(font=40)
cal_m.menu=tk.Menu(cal_m)
cal_m["menu"]=cal_m.menu
cal_m.menu.add_command(label="Calculadora básica",command=ventana_calculadora_basica)
cal_m.menu.add_command(label="Calculadora de derivadas",command=cal_derivadas)
imagen1 = tk.PhotoImage(file="calculator2.png")
lbimagen1 = tk.Label(mainW, image=imagen1)
lbimagen1.place(x=20, y=300)


imagen2 = tk.PhotoImage(file="presentation1.png")
lbimagen2 = tk.Label(mainW, image=imagen2)
lbimagen2.place(x=350, y=300)


mainW.mainloop()

