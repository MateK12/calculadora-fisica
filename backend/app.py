from asyncio.windows_events import NULL
import json
from operator import mod
from pyexpat import model
from unicodedata import name
from flask import Flask, render_template, request, jsonify

import flask

from flask_cors import CORS
from fisica import simular


app = Flask(__name__)       #Inicializamos Flask



CORS(app)

@app.route("/calcular", methods=["GET","POST"])           #Obtener datos, procesarlos y devolverlos
def calcular_plano():
    angulo = request.json["angulo"]
    E_friccion = request.json["existencia_friccion"]
    friccion_dinamica = request.json["friccion_dinamica"]
    friccion_estatica = request.json["friccion_estatica"]
    fuerza = request.json["fuerza"]
    materiales = request.json["materiales"]
    masa = request.json["masa"]
    pla = request.json["plano"]
    opcion_calculo = request.json["que_calcular"]
    aceleracion = request.json["aceleracion"]
    print(pla,angulo,masa,fuerza,E_friccion,materiales,friccion_estatica,friccion_dinamica)
    # prueba = simular(plano,angulo,masa,fuerza,E_friccion,materiales,friccion_estatica,friccion_dinamica,opcion_calculo,aceleracion)
    prueba = simular(pla=1,angulo=angulo,masa=masa,fuerza=fuerza,E_friccion=E_friccion,materiales=materiales,friccion_estatica =friccion_estatica,friccion_dinamica =friccion_dinamica,op_A =opcion_calculo,acel_A=aceleracion)
    respuesta = prueba
    print("prueba",prueba)
    msg = {
        "mensaje":respuesta
    }
    return msg

@app.route("/calcular_PNI", methods=["GET","POST"])           #Obtener datos, procesarlos y devolverlos
def calcular_plano_No_Inclinado():
    angulo = request.json["angulo"]
    E_friccion = request.json["existencia_friccion"]
    friccion_dinamica = request.json["friccion_dinamica"]
    friccion_estatica = request.json["friccion_estatica"]
    fuerza = request.json["fuerza"]
    materiales = request.json["materiales"]
    masa = request.json["masa"]
    pla = request.json["plano"]
    opcion_calculo = request.json["que_calcular"]
    aceleracion = request.json["aceleracion"]
    print(pla,angulo,masa,fuerza,E_friccion,materiales,friccion_estatica,friccion_dinamica)
    # prueba = simular(plano,angulo,masa,fuerza,E_friccion,materiales,friccion_estatica,friccion_dinamica,opcion_calculo,aceleracion)
    prueba = simular(pla=2,angulo=angulo,masa=masa,fuerza=fuerza,E_friccion=E_friccion,materiales=materiales,friccion_estatica =friccion_estatica,friccion_dinamica =friccion_dinamica,op_A =opcion_calculo,acel_A=aceleracion)
    respuesta = prueba
    print("prueba",prueba)
    msg = {
        "mensaje":respuesta
    }
    return msg

   
 




if __name__ == '__main__':
   
    app.run(debug=True, port=5000)