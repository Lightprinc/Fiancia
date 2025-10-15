from flask import Flask, request, jsonify
from .confiDB import connectionBD

import joblib
modelo = joblib.load("IAFLASK/modelo_finanzas.pkl")

import json
import numpy as np
import random


cat = ["Ingreso_mensual","Balance","Ahorro_total","Gasto_viveres","Gasto_renta","Gasto_electricidad","Gasto_agua","Gasto_transporte","Gasto_educacion","Gasto_equipamiento_mantenimiento_hogar","Gasto_gas","Gasto_ocio","Gasto_aficcion","gastos_indefinidos","deudas","suscripciones","pagos_tarjeta"
]

supp_val_list = [(1111,-74,504,128,146,69,45,70,19,101,33,63,56,9,13,8,6), 
(622,61,411,122,145,66,52,72,14,105,31,54,61,10,12,7,6),
(643,-119,-69,221,187,139,66,174,53,196,73,76,70,51,60,75,64),
(643,-119,-69,221,187,139,66,174,53,196,73,76,70,51,60,75,64),
(643,-119,-69,221,187,139,66,174,53,196,73,76,70,51,60,75,64),
(643,-119,-69,221,187,139,66,174,53,196,73,76,70,51,60,75)
]

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({"mensaje": "Hola desde Flask!"})


@app.route("/recibir_dato", methods=["POST"]) #Recibe datos y ejecuta "order_data" // Para self-request
def subir():
    data = request.json #Peticion HHTPS como diccionario
    id_usuario = data.get("id_usuario") #Recibe id_usuario
    id_grafico = data.get("id_grafico") #Recibe id_grafico


    conn = connectionBD()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM Gastos WHERE id_grafico = %s"

    cursor.execute(sql, (id_grafico,))
    answer = cursor.fetchall() #0 = id 1 = id_datos 2 = cat 3 = val

    prediccion=order_data(answer)

    return jsonify({
        "status": "ok",
        "id_usuario": id_usuario,
        "id_grafico": id_grafico,
        "filas": len(answer),
        "datos": answer
        ,"prediccion": prediccion.tolist()
    })

def order_data(datos): #Ordena los datos y hace la prediccion
    if not datos:
        print("⚠️ No se encontraron registros en la BD")
        return []

    # Tomar SOLO la columna 'val' de las 17 filas
    #fila = [line["val"] for line in datos] ejemplo

    emision = []
    for i in range(17):
        temp = 0
        for line in datos:
            if line["cat"] == cat[i]:
                temp += line["val"]
        emision.append(temp)  # siempre agrega uno (0 si no encontró nada)




    # Convertir en una matriz con 1 fila y 17 columnas
    X = np.array(emision).reshape(1, -1)  

    # Predecir
    prediccion = modelo.predict(X)

    print("Predicción:", prediccion)

    return prediccion
    #jsonify({"mensaje": prediccion.tolist()})

@app.route("/simulacion") #Simula una peticion POST al endpoint /recibir_dato
def simulacion():
     # Simular una petición POST al endpoint /recibir_dato
     # Usamos el cliente de prueba de Flask para hacer la petición internamente
     # sin necesidad de un cliente externo

    
    with app.test_client() as client: # Crear un cliente de prueba
        response = client.post( 
            "/recibir_dato", # Endpoint al que se hace la petición
            data=json.dumps({"id_usuario": 5, "id_grafico": 23}), # Datos en formato JSON
            content_type="application/json" 
        )
        return jsonify({
            "simulacion_status": response.status_code,
            "simulacion_data": response.get_json()
        })
    
@app.route("/sim") #Simula una peticion POST al endpoint /recibir_dato
def simulacion_valores(path, data):
     # Simular una petición POST al endpoint /recibir_dato
     # Usamos el cliente de prueba de Flask para hacer la petición internamente
     # sin necesidad de un cliente externo

    
    with app.test_client() as client: # Crear un cliente de prueba
        response = client.post( 
            path, # Endpoint al que se hace la petición
            data=json.dumps({"id_usuario": 5, "id_grafico": 23}), # Datos en formato JSON
            content_type="application/json" 
        )
        return jsonify({
            "simulacion_status": response.status_code,
            "simulacion_data": response.get_json()
        })

@app.route("/crear_datos_simulados")
def crear_datos_simulados(): #Crear datos simulados en la BD
    conn = connectionBD()
    cursor = conn.cursor()

    id_grafico = 23  # ID del gráfico para el usuario simulado
    
    sql = "DELETE FROM Gastos WHERE id_grafico = %s"
    cursor.execute(sql, (id_grafico,))

    select=random.randint(0, len(supp_val_list)) #lejir uno de los diferentes diccionarios
    print("Seleccionado:", select)

    supp_values = supp_val_list[select]
        

    for i in range(17):
        categoria = cat[i]  # usa la lista real de categorías
        valor = supp_values[i]
        cursor.execute(
            "INSERT INTO Gastos (id_grafico, cat, val) VALUES (%s, %s, %s)",
            (id_grafico, categoria, valor)
        )
    conn.commit()

    cursor.close()
    conn.close()
    print("Datos simulados insertados en la base de datos.")
    return jsonify({"mensaje": "Datos simulados insertados en la base de datos."})

"""@app.route("/añadir_gasto", methods=["POST"])
def añadir_gasto():
    data = request.json
    id_grafico = data.get("id_grafico")

    conn = connectionBD()
    cursor = conn.cursor()


    for g in data["gastos"]:
        categoria = g["cat"]
        valor = g["val"]
        cursor.execute(
            "INSERT INTO Gastos (id_grafico, cat, val) VALUES (%s, %s, %s)",
            (id_grafico, categoria, valor)
        )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Gastos añadido correctamente."})"""

@app.route("/añadir_gasto", methods=["POST"])
def añadir_gasto():
    data = request.json

    print("datos recibidos:", data)
    print("id_grafico:", data.get("id_grafico"))

    nombre = data.get("nombre")
    id_grafico = data.get("id_grafico")
    categoria = data.get("cat")
    valor = data.get("monto")

    

    conn = connectionBD()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO gastos (id_grafico, Nombre, Categoria, Monto) VALUES (%s,%s, %s, %s)",
        (id_grafico, nombre, categoria, valor)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Gasto añadido correctamente."})

@app.route("/crear_grafico", methods=["POST"])
def crear_grafico():
    data = request.json
    id_usuario = data.get("id_usuario")
    nombre = data.get("nombre")

    conn = connectionBD()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO grafico (id_usuario, nombre) VALUES (%s,%s)",
        (id_usuario, nombre)
    )
    conn.commit()
    nuevo_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Gráfico creado correctamente.", "id_grafico": nuevo_id})

@app.route("/ver_graficos/<int:id_usuario>", methods=["GET"])
def ver_graficos(id_usuario):
    print("id_usuario recibido:", id_usuario)

    # Convierte a entero si no es None
    if id_usuario is not None:
        try:
            id_usuario = int(id_usuario)
        except ValueError:
            return jsonify({"error": "id_usuario debe ser un número"}), 400

    conn = connectionBD()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM grafico WHERE id_usuario = %s"
    cursor.execute(sql, (id_usuario,))
    graficos = cursor.fetchall()

    print("Gráficos encontrados:", graficos)

    cursor.close()
    conn.close()

    return jsonify(graficos)

@app.route("/ver_gastos", methods=["GET"])
def ver_gastos():
    id_grafico = request.args.get("id_grafico")
    print("id_grafico recibido:", id_grafico)

    # Convierte a entero si no es None
    if id_grafico is not None:
        try:
            id_grafico = int(id_grafico)
        except ValueError:
            return jsonify({"error": "id_grafico debe ser un número"}), 400

    conn = connectionBD()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM gastos WHERE id_grafico = %s"
    cursor.execute(sql, (id_grafico,))
    gastos = cursor.fetchall()

    print("Gastos encontrados:", gastos)

    cursor.close()
    conn.close()

    return jsonify({"gastos": gastos})

@app.route("/ver_gastosxuser/<int:id_usuario>", methods=["GET"])
def ver_gastosx(id_usuario):
    conn = connectionBD()
    cursor = conn.cursor(dictionary=True)

    # Buscamos los gastos que pertenecen a los gráficos del usuario
    cursor.execute("""
        SELECT g.id, g.Nombre, g.Monto, g.Categoria, gr.nombre AS grafico_nombre
        FROM gastos g
        INNER JOIN grafico gr ON g.id_grafico = gr.id
        WHERE gr.id_usuario = %s
        ORDER BY g.id DESC
    """, (id_usuario,))

    gastos = cursor.fetchall()

    print("Gastos encontrados para el usuario", id_usuario, ":", gastos)

    cursor.close()
    conn.close()

    return jsonify(gastos)

@app.route("/ver_datos/<int:id_usuario>", methods=["GET"])
def ver_datos(id_usuario): #Funcion para ver todos los datos pertenecientes a un usuario
    conn = connectionBD()
    cursor = conn.cursor(dictionary=True)

    # Obtener gastos
    cursor.execute("""
        SELECT g.id, g.Nombre, g.Monto, g.Categoria, gr.nombre AS grafico_nombre
        FROM gastos g
        INNER JOIN grafico gr ON g.id_grafico = gr.id
        WHERE gr.id_usuario = %s
        ORDER BY g.id DESC
    """, (id_usuario,))
    gastos = cursor.fetchall()

    # Obtener graficos
    cursor.execute("SELECT * FROM grafico WHERE id_usuario = %s", (id_usuario,))
    graficos = cursor.fetchall()

    datos = {
        "gastos": gastos,
        "graficos": graficos
    }

    print("Datos encontrados:", datos)

    cursor.close()
    conn.close()

    return jsonify({"datos": datos})


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
  