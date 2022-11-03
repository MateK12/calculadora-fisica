import math, time, sys
import numpy as np
from matplotlib import pyplot
def simular(pla,angulo,masa,fuerza,E_friccion,materiales,friccion_estatica,friccion_dinamica,op_A,acel_A):
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
        # delay_print("TABLA DE MATERIALES:")
        print("\n1)Madera sobre madera \n2)Acero sobre hielo\n3)Teflón sobre teflón\n4)Caucho sobre cemento seco\n5)Vidrio sobre vidrio\n6)Esquí sobre nieve\n7)Madera sobre cuero\n8)Aluminio sobre acero\n9)Articulaciones humanas\n10)Personalizado")
        mat=materiales
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
            fric_e=friccion_estatica
            while fric_e>1 or fric_e<0:
                fric_e=float(input("Ingrese la fricción estatica menor que 1 y mayor que 0: "))
            fric_d=friccion_dinamica
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
    # delay_print ("¡Bienvenido/a a la calculadora física, hecha por Iñaki Góngora!")
    for poaa in range(1):
        result = []

        cont_resultados+=1
        if cont_resultados>1:
            # delay_print("¡Bienvenido de nuevo!")
            print ("\n¿Quiere usar un plano inclinado?")
            print ("\nSi: 1\nNo: 2")
        plano=pla
        if plano == 1:
            ang=angulo
            while ang > 90 or ang<0:
                print ("Eso no es una opción válida.")
                ang=float(input("Ingrese la inclinación en grados (0°-90°)"))
            ang=ang-ang*2
            ang=math.radians(ang)
            # delay_print("CALCULADORA DE ACELERACIÓN")
            grav=9.8
            masa=masa
            fuerza=fuerza
            peso=masa*grav
            pesoX=math.sin(ang)*peso
            pesoY=math.cos(ang)*peso
            normal=pesoY
            fric=E_friccion
            if fric==1:
                fricc(normal)
                fric_estatica=fric_e*normal
                fric_dinamica=fric_d*normal   
                resultado_2 = "\nLa fricción estática es: ",fric_estatica,"La fricción dinámica es: ",fric_dinamica
                result.append(resultado_2) 
                fuerzaNeta=fuerza+pesoX
                if fuerzaNeta>fric_estatica:

                    result.append("\nEl objeto se moverá")
                    acel=(fuerzaNeta-fric_dinamica)/masa
                    if acel<0:
                        result.append("El objeto se moverá cuesta abajo")
                    variable1 = "\nLa aceleración es: ",acel,"m/s^2"
                    result.append(variable1)
                    acel=round(acel,4)
                    resultado="El resultado número: ",cont_resultados," es igual a : ",acel,"m/s^2"
                    resultados.append(resultado)
                    # graf(acel)
                else:
                    result.append("\nEl objeto no se moverá")
                    result.append("\nLa aceleración es 0")
                    resultado="El resultado número: ",cont_resultados," es igual a: 0 m/s^2"
                    result.append(resultado)
                    resultados.append(resultado)      
                    
            elif fric==2:
                fuerzaNeta=fuerza+pesoX
                acel=fuerzaNeta/masa
                if acel<0:
                    result.append("El objeto se moverá cuesta abajo")
                vari = "\nLa aceleración es: ",acel,"m/s^2"
                result.append(vari)
                acel=round(acel,4)
                resultado="El resultado número: ",cont_resultados," es igual a: ",acel,"m/s^2"
                result.append(resultado)
                # graf(acel)
            else:
                print("¡Eso no es una opcion valida!")           


        elif plano == 2:
            # delay_print ("Fuerza: 1\nMasa: 2\nAceleración: 3")
            op=op_A
            if op == 1:
                # delay_print("CALCULADORA DE FUERZA")
                masa=masa
                acel=acel_A
                fuerza=masa*acel
                variable2=("La fuerza aplicada al objeto para lograr",acel,"m/s^2 es: ",fuerza,"N")
                result.append(variable2)
                fuerza=round(fuerza,4)
                resultado="El resultado número: ",cont_resultados," es igual a: ",fuerza,"N"
                result.append(resultado)

            elif op == 2:
                # delay_print("CALCULADORA DE MASA")
                fuerza=fuerza
                acel=acel_A
                masa=fuerza/acel
                variable3=("La masa del objeto para que al aplicarle una fuerza de",fuerza,"N, su aceleración sea", acel,"m/s^2, es: ",masa)
                result.append(variable3)
                masa=round(masa,4)
                resultado="El resultado número: ",cont_resultados," es igual a: ",masa,"kg"
                result.append(resultado)

            elif op == 3:
                # delay_print("CALCULADORA DE ACELERACIÓN")
                grav=9.8
                masa=masa
                fuerza=fuerza
                peso=grav*masa
                normal=peso
                fric=E_friccion
                if fric==1:
                    fricc(normal)
                    fric_estatica=fric_e*normal
                    fric_dinamica=fric_d*normal
                    var_e ="\nLa fricción estática es: ",fric_estatica
                    result.append(var_e)
                    var_d = "La fricción dinámica es: ",fric_dinamica
                    result.append(var_d)
                    if fuerza>fric_estatica:
                        result.append("\nEl objeto se moverá")
                        acel=(fuerza-fric_dinamica)/masa
                        if acel<0:
                            result.append("El objeto se moverá a la izquierda")
                        var1 ="\nLa aceleración es: ",acel,"m/s^2"
                        result.append(var1)
                        acel=round(acel,4)
                        var2="El resultado número: ",cont_resultados," es igual a: ",acel,"m/s^2"
                        result.append(var2)
                        # graf(acel)

                    else:
                        result.append("\nEl objeto no se moverá")
                        result.append("\nLa aceleración es 0")
                        resultado="El resultado número: ",cont_resultados," es igual a: 0 m/s^2"
                        result.append(resultado)       

                elif fric==2:
                    acel=fuerza/masa
                    if acel<0:
                            result.append("El objeto se moverá a la izquierda")
                    var3 = "\nLa aceleración es: ",acel,"m/s^2"
                    result.append(var3)
                    acel=round(acel,4)
                    resultado=('El resultado número: ',cont_resultados,'es igual a: ',acel,"m/s^2")
                    result.append(resultado)
                    # graf(acel)
                else:
                    print("¡Eso no es una opcion valida!")
                    
            else:
                print("Elija una operación valida")
        else:
            print("Elija una operación valida")
            
        
        

        # x=(input("\n¿Quiere realizar otro cálculo?\n1=Si\nOtro=No\n"))
        # if x =="1":
        #     x=True
        # else: 
        #     x=False
            
    print("¡Gracias por susar esta calculadora!")
    time.sleep(3)
    print(result)
    return result
    