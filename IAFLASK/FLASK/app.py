from flask import Flask, request, jsonify, render_template
import mysql.connector
from confiDB import connectionBD
import requests

from threading import Thread
import time

import joblib
modelo = joblib.load("IAFLASK/modelo_finanzas.pkl")

import json


supp_values = [643,-119,-69,221,187,139,66,174,53,196,73,76,70,51,60,75,64]

app = Flask(__name__)

@app.route("/recibir_dato", methods=["POST"])
def subir():
    data = request.json #Peticion HHTPS como diccionario
    id_usuario = data.get("id_usuario") #Recibe id_usuario
    id_grafico = data.get("id_grafico") #Recibe id_grafico


    conn = connectionBD()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM Gastos WHERE id_grafico = %s"

    cursor.execute(sql, (id_grafico,))
    answer = cursor.fetchall() #0 = id 1 = id_datos 2 = cat 3 = val

    order_data(answer)

    return jsonify({
        "status": "ok",
        "id_usuario": id_usuario,
        "id_grafico": id_grafico,
        "filas": len(answer),
        "datos": answer
    })


import numpy as np

def order_data(datos):
    if not datos:
        print("⚠️ No se encontraron registros en la BD")
        return []

    # Tomar SOLO la columna 'val' de las 17 filas
    fila = [line["val"] for line in datos]  

    # Convertir en una matriz con 1 fila y 17 columnas
    X = np.array(fila).reshape(1, -1)  

    # Predecir
    prediccion = modelo.predict(X)

    print("Predicción:", prediccion)
    return prediccion.tolist()

@app.route("/")
def inicio():
    return jsonify({"mensaje": "Hola desde Flask!"})


@app.route("/simulacion")
def simulacion():
    with app.test_client() as client:
        response = client.post(
            "/recibir_dato",
            data=json.dumps({"id_usuario": 5, "id_grafico": 23}),
            content_type="application/json"
        )
        return jsonify({
            "simulacion_status": response.status_code,
            "simulacion_data": response.get_json()
        })

if __name__ == "__main__":
    app.run(debug=True)
    

    # Levantar el servidor en un hilo aparte
    def run_server():
        app.run(debug=True)

    Thread(target=run_server).start()
    time.sleep(2)  # espera a que el server inicie

