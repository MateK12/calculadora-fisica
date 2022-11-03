from asyncio.windows_events import NULL
import json
from operator import mod
from pyexpat import model
from unicodedata import name
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from email.policy import default
from enum import unique
import flask
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask_cors import CORS
from fisica import simular
motor = create_engine("mysql://root:@localhost/Volarg")  #Alchemy


app = Flask(__name__)       #Inicializamos Flask



mysql = MySQL(app)
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
    plano = request.json["plano"]
    opcion_calculo = request.json["que_calcular"]
    aceleracion = request.json["aceleracion"]
    print("llego",plano)
    # prueba = simular(plano,angulo,masa,fuerza,E_friccion,materiales,friccion_estatica,friccion_dinamica,opcion_calculo,aceleracion)
    prueba = simular(pla=plano,angulo=angulo,masa=masa,fuerza=fuerza,E_friccion=E_friccion,materiales=materiales,friccion_estatica =friccion_estatica,friccion_dinamica =friccion_dinamica,op_A =opcion_calculo,acel_A=aceleracion)
    respuesta = prueba
    print("prueba",prueba)
    msg = {
        "mensaje":respuesta
    }
    return msg

   




if __name__ == '__main__':
   
    app.run(debug=True, port=5000)