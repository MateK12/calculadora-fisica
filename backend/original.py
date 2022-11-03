import math, time, sys
import numpy as np
from matplotlib import pyplot
def graf(acel):
  fig, (ax1,ax2) = pyplot.subplots(1,2,sharex=True)
  x = np.array(range(20))
  y = np.zeros(len(x))
  y2= acel
  for i in range (len(x)):
    (y[i]) = acel*x[i]
  
  ax1.plot (x,y)
  pyplot.axhline(y=y2,color = "r")
  pyplot.xlabel ("Tiempo en segundos")
  ax1.set_ylabel ("Velocidad en metros por segundo")
  ax1.set_title ("Velocidad")
  ax1.grid()
  ax2.set_title("Aceleración")
  ax2.set_ylabel("Aceleración en metros por segundo cuadrado")
  ax2.grid()
  pyplot.show()
  print ("Gráfico de la velocidad con respecto al tiempo con una aceleración de:", acel,"m/s^2")

def fricc(normal):
    global fric_e, fric_d
    delay_print("TABLA DE MATERIALES:")
    print("\n1)Madera sobre madera \n2)Acero sobre hielo\n3)Teflón sobre teflón\n4)Caucho sobre cemento seco\n5)Vidrio sobre vidrio\n6)Esquí sobre nieve\n7)Madera sobre cuero\n8)Aluminio sobre acero\n9)Articulaciones humanas\n10)Personalizado")
    mat=int(input("\nElija sus materiales: "))
    if mat==1:
        fric_e=0.5
        fric_d=0.3
    elif mat==2:
        fric_e=0.03
        fric_d=0.02
    elif mat==3:
        fric_e=0.04
        fric_d=0.04
    elif mat==4:
        fric_e=1
        fric_d=0.8
    elif mat==5:
        fric_e=0.9
        fric_d=0.4
    elif mat==6:
        fric_e=0.1
        fric_d=0.05
    elif mat==7:
        fric_e=0.5
        fric_d=0.4
    elif mat==8:
        fric_e=0.61
        fric_d=0.47              
    elif mat==9:
        fric_e=0.02
        fric_d=0.003
    elif mat==10:
        fric_e=float(input("Ingrese la fricción estatica: "))
        while fric_e>1 or fric_e<0:
            fric_e=float(input("Ingrese la fricción estatica menor que 1 y mayor que 0: "))
        fric_d=float(input("Ingrese la fricción dinámica: "))
        while fric_d>1 or fric_d<0:
            fric_d=float(input("Ingrese la fricción dinámica menor que 1 y mayor que 0: "))
    else:
        print("¡Esa no es una opción valida!")

def delay_print (s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
        2
resultados=[]
cont_resultados=0
x=True
delay_print ("¡Bienvenido/a a la calculadora física, hecha por Iñaki Góngora!")
while x==True:
    cont_resultados+=1
    if cont_resultados>1:
        delay_print("¡Bienvenido de nuevo!")
    delay_print ("\n¿Quiere usar un plano inclinado?")
    delay_print ("\nSi: 1\nNo: 2")
    plano=int(input("\n"))
    if plano==1:
        ang=float(input("Ingrese la inclinación en grados (0° hasta 90°)"))
        while ang > 90 or ang<0:
            print ("Eso no es una opción válida.")
            ang=float(input("Ingrese la inclinación en grados (0°-90°)"))
        ang=ang-ang*2
        ang=math.radians(ang)
        delay_print("CALCULADORA DE ACELERACIÓN")
        grav=9.8
        masa=float(input("\nIngrese la masa(Kg): "))
        fuerza=float(input("Ingrese la fuerza(N): "))
        peso=masa*grav
        pesoX=math.sin(ang)*peso
        pesoY=math.cos(ang)*peso
        normal=pesoY
        fric=int(input("¿Hay fricción? \n\tSi:1 \n\tNo:2 \n\t"))
        if fric==1:
            fricc(normal)
            fric_estatica=fric_e*normal
            fric_dinamica=fric_d*normal    
            print("\nLa fricción estática es: ",fric_estatica)
            print("La fricción dinámica es: ",fric_dinamica)
            fuerzaNeta=fuerza+pesoX
            if fuerzaNeta>fric_estatica:
                delay_print ("\nEl objeto se moverá")
                acel=(fuerzaNeta-fric_dinamica)/masa
                if acel<0:
                    print("El objeto se moverá cuesta abajo")
                print("\nLa aceleración es: ",acel,"m/s^2")
                acel=round(acel,4)
                resultado="El resultado número: ",cont_resultados," es igual a : ",acel,"m/s^2"
                resultados.append(resultado)
                graf(acel)
            else:
                delay_print("\nEl objeto no se moverá")
                delay_print("\nLa aceleración es 0")
                resultado="El resultado número: ",cont_resultados," es igual a: 0 m/s^2"
                resultados.append(resultado)      
                
        elif fric==2:
            fuerzaNeta=fuerza+pesoX
            acel=fuerzaNeta/masa
            if acel<0:
                print("El objeto se moverá cuesta abajo")
            print("\nLa aceleración es: ",acel,"m/s^2")
            acel=round(acel,4)
            resultado="El resultado número: ",cont_resultados," es igual a: ",acel,"m/s^2"
            resultados.append(resultado)
            graf(acel)
        else:
            print("¡Eso no es una opcion valida!")           


    elif plano == 2:
        delay_print ("Fuerza: 1\nMasa: 2\nAceleración: 3")
        op=int(input("\n¿Qué quiere calcular? "))
        if op == 1:
            delay_print("CALCULADORA DE FUERZA")
            masa=float(input("\nIngrese la masa (Kg): "))
            acel=float(input("Ingrese la aceleración (m/s^2): "))
            fuerza=masa*acel
            print("La fuerza aplicada al objeto para lograr",acel,"m/s^2 es: ",fuerza,"N")
            fuerza=round(fuerza,4)
            resultado="El resultado número: ",cont_resultados," es igual a: ",fuerza,"N"
            resultados.append(resultado)

        elif op == 2:
            delay_print("CALCULADORA DE MASA")
            fuerza=float(input("\nIngrese la fuerza(N): "))
            acel=float(input("Ingrese la aceleración (m/s^2): "))
            masa=fuerza/acel
            print ("La masa del objeto para que al aplicarle una fuerza de",fuerza,"N, su aceleración sea", acel,"m/s^2, es: ",masa)
            masa=round(masa,4)
            resultado="El resultado número: ",cont_resultados," es igual a: ",masa,"kg"
            resultados.append(resultado)

        elif op == 3:
            delay_print("CALCULADORA DE ACELERACIÓN")
            grav=9.8
            masa=float(input("\nIngrese la masa(Kg): "))
            fuerza=float(input("Ingrese la fuerza(N): "))
            peso=grav*masa
            normal=peso
            fric=int(input("¿Hay fricción? \n\tSi:1 \n\tNo:2 \n\t"))
            if fric==1:
                fricc(normal)
                fric_estatica=fric_e*normal
                fric_dinamica=fric_d*normal
                print("\nLa fricción estática es: ",fric_estatica)
                print("La fricción dinámica es: ",fric_dinamica)

                if fuerza>fric_estatica:
                    delay_print ("\nEl objeto se moverá")
                    acel=(fuerza-fric_dinamica)/masa
                    if acel<0:
                        print("El objeto se moverá a la izquierda")
                    print("\nLa aceleración es: ",acel,"m/s^2")
                    acel=round(acel,4)
                    resultado="El resultado número: ",cont_resultados," es igual a: ",acel,"m/s^2"
                    resultados.append(resultado)
                    graf(acel)

                else:
                    delay_print("\nEl objeto no se moverá")
                    delay_print("\nLa aceleración es 0")
                    resultado="El resultado número: ",cont_resultados," es igual a: 0 m/s^2"
                    resultados.append(resultado)       

            elif fric==2:
                acel=fuerza/masa
                if acel<0:
                        print("El objeto se moverá a la izquierda")
                print("\nLa aceleración es: ",acel,"m/s^2")
                acel=round(acel,4)
                resultado=('El resultado número: ',cont_resultados,'es igual a: ',acel,"m/s^2")
                resultados.append(resultado)
                graf(acel)
            else:
                print("¡Eso no es una opcion valida!")
                
        else:
            delay_print("Elija una operación valida")
    else:
        delay_print("Elija una operación valida")
        
    
        
    x=(input("\n¿Quiere realizar otro cálculo?\n1=Si\nOtro=No\n"))
    if x =="1":
        x=True
    else: 
        x=False
        
print(resultados)
delay_print("¡Gracias por usar esta calculadora!")
time.sleep(3)