# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:23:09 2020

@author: gianc
"""

#Se importan las bibliotecas utilizadas
import math as mt
import numpy as np
import matplotlib.pyplot as plt
#Mensaje que le pide al usuario escoger las diferentes funciones del programa
introducción=(input("Bienvenido. Esta es una calculadora financiera.IMPORTANTE: si al colocar el numero correspondiente vuelva a salir este mensaje, vuelva a ponerlo y hágalo hasta que el programa le pida otros datos. Le aseeguro que no serán más de 7 veces las que tenga que repetir este proceso. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor futuro presione 4. Para conocer la tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: "))


while introducción!="0" or introducción=="7":


    if introducción=="g7":
        break
#Caso 0
    if introducción=="0":
        print("Gracias por utilizar este programa.")
        break
#Caso 1
    if introducción=="1":
        a=int(input("Digite sus ingresos netos:" ))
       

       
        def pago_iva(a):
            i=a/34270
            if i>92000:
                print("Usted debe pagar IVA bimestralmente")
            if i<92000:
                print("Usted debe pagar IVA cuatrimestralmente")
                   
        pago_iva(a)

    introducción=(input("Bienvenido. Esta es una calculadora financiera. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor futuro presione 4. Para conocer la tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: "))
    if introducción=="0":
        print("Gracias por utilizar este programa.")
        break
    if introducción=="g7":
        break      
#    introducción=input("Bienvenido. Esta es una calculadora financiera. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor de valor futuro presione 4. Para conocerla tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: ")
   
#Caso 2
    if introducción=="2":
        rete_fuente=input("Para conocer la retención en la fuente de compras, presione c, para conocer el de servicios presione s y para el de honorarios presione h: ")
        #retención en caso de escoger C
        if rete_fuente=="c":
            compras=int(input("Ingrese el valor de la base de la compra para responsable del iva: "))
            iva=compras*0.19
            if compras>0:
                uvt_1=compras/34270
                if uvt_1>27:
                    com_iva=compras+iva
                    resultado_1=com_iva-compras*0.035
                    print("El valor del pago al proveedor es: ", resultado_1)


    #retención en caso de escoger H
        if rete_fuente=="h":
            honorarios=int(input("Ingrese el valor de la base de los honorarios para responsable de iva: "))
            iva_2=honorarios*0.19
            if honorarios>0:
                uvt_2=honorarios/34270
                if uvt_2>0:
                    com_iva_2=honorarios+iva_2
                    resultado_2=com_iva_2-honorarios*0.10
                    print("El valor del pago del pago al profesional es de: ", resultado_2)
           
            #retención en caso de escoger S
        if rete_fuente=="s":
            servicios=int(input("Ingrese el valor de la base de la prestación del servicio: "))
            iva_3=servicios*0.19
            if servicios>0:
                uvt_3=servicios/34270
                if uvt_3>4:
                    com_iva_3=servicios+iva_3
                    resultado_3=com_iva_3-servicios*0.04
                    print("El valor neto del pago de los servicios es: ", resultado_3)
                if uvt_3<4:
                    print("El valor a pagar es de: ", servicios*0.19+servicios)                    

    introducción=(input("Bienvenido. Esta es una calculadora financiera. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor de valor futuro presione 4. Para conocerla tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: "))
    if introducción=="0":
        print("Gracias por utilizar este programa.")
        break
    if introducción=="g7":
        break

#Caso 3
    if introducción=="3":
        patrimonio_bruto=int(input("Ingrese el valor de su patrimonio bruto en el último año: "))
        costos_consumos=int(input("Ingrese el valor de sus compras y consumos totales en el último año: "))
        ingresos_brutos=int(input("Ingrese el valor de sus ingresos brutos en el último año: "))
        consig_depos_inver=int(input("Ingrese el valor total entre consignaciones, depósitos o inversiones que haya hecho en el último años:"))
        consumos_tc=int(input("Ingrese el valor en consumos con tarjeta de crédito en el último año: "))


        if patrimonio_bruto>=149202000 or costos_consumos>=46418000 or ingresos_brutos>=46418000 or consig_depos_inver>=46418000 or consumos_tc>=46418000:
            print("Usted es declarante de renta")
        else:
            print("Usted NO es declarante de renta")
   
    introducción=(input("Bienvenido. Esta es una calculadora financiera. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor de valor futuro presione 4. Para conocerla tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: "))
    if introducción=="0":
        print("Gracias por utilizar este programa.")
        break
    if introducción=="g7":
        break
#Caso 4
    if introducción=="4":
    #valor futuro
        dinero_2=int(input("Ingrese la cantidad a solicitar de préstamo: "))
        tasa_2=float(input("Ingrese la tasa de interés: "))
        tiempo_2=float(input("Ingrese el tiempo a calcular en meses: "))

        def v_futuro (dinero_2, tasa_2, tiempo_2):
            v_futuro=dinero_2*((1+tasa_2)**tiempo_2)
            print("El valor futuro es de: ", v_futuro)
   
        v_futuro(dinero_2,tasa_2,tiempo_2)
    introducción=(input("Bienvenido. Esta es una calculadora financiera. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor de valor futuro presione 4. Para conocerla tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: "))
    if introducción=="0":
        print("Gracias por utilizar este programa.")
        break
    if introducción=="g7":
        break
#Caso 5
    if introducción=="5":
    #tasa de interés
        valor_futuro=int(input("Ingrese el valor futuro: "))
        valor_presente=int(input("Ingrese el valor presente: "))
        tiempo_3=int(input("Ingrese el tiempo a calcular en meses: "))
   
        def t_interes (valor_futuro, valor_presente,tiempo_3):
            tasa_interes=(valor_futuro/valor_presente)**(1/tiempo_3)-1
            ti=tasa_interes*100
            print("El interés es: ", ti, "%")
   
        t_interes(valor_futuro,valor_presente,tiempo_3)
    introducción=(input("Bienvenido. Esta es una calculadora financiera. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor de valor futuro presione 4. Para conocerla tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: "))
    if introducción=="0":
        print("Gracias por utilizar este programa.")
        break
    if introducción=="g7":
        break
#Caso 6
    if introducción=="6":
        valor_futuro_2=int(input("Ingrese valor futuro: "))
        valor_presente_2=float(input("Ingrese valor presente: "))
        i=float(input("Ingrese la tasa correspondiente: "))

        def calculo_tiempo(valor_futuro_2, valor_presente_2, i):
            c_tiempo=(mt.log(valor_futuro_2/valor_presente_2))/mt.log(1+i)
            print("El tiempo es de: ", c_tiempo, "bimestres")
   
        calculo_tiempo(valor_futuro_2,valor_presente_2,i)    
    introducción=(input("Bienvenido. Esta es una calculadora financiera. Para saber si debe pagar el iva de su empresa bimestralmente o cuatrimestralente presione 1.Para consultas acerca del pago de la retención en la fuente presione 2.Para saber si usted es declarante de renta presione 3.Para conocer el valor de valor futuro presione 4. Para conocerla tasa de interés presione 5.Para saber el tiempo que tiene que dejar invertido una suma con determinada tasa para obtener cierta ganancia presione 6. Para conocer los intereses que debe pagar por un crédito presione 7.Presione 0 para salir.  Su respuesta es: "))

    if introducción=="0":
        print("Gracias por utilizar este programa.")
        break

    if introducción=="g7":
        break

#Caso 7
    if introducción=="7":
        cantidad=int(input("Ingrese la cantidad a solicitar de préstamo: "))
        tasa=float(input("Ingrese la tasa de interés: "))
       
        n=int(input("Ingrese los años a calcular: "))

        def interes (cantidad, tasa, tiempo,):
            int_compuesto=cantidad*(((1+tasa)**tiempo)-1)
            print(int_compuesto)
            return(int_compuesto)
   


        print(interes,(cantidad, tasa))
        print("Recuerde que cada valor corresponde a cada año. Esto depende de los años ingresados aneriormente.")
        print("Al final de",n,"años, usted habrá pagado de intereses: " )

        x=np.zeros(n)
        y=np.zeros(n)

        tiempo=0
        for i in range(0,n):
            tiempo=tiempo+1
            x[i]=tiempo
            y[i]=interes(cantidad, tasa, tiempo)
   

   
        plt.scatter(x,y,color="red")

    print("Para poder ver la gráfica correspondiemte a la función 7 presione g7. Opción válida solo después de haber utilizado e ingresado los valores en la función 7.") 


    if introducción=="g7":
        break
    
    

