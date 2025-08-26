import pandas as pd
import joblib

modelo = joblib.load("modelo_finanzas.pkl")

nuevo = [[622,61,411,122,145,66,52,72,14,105,31,54,61,10,12,7,6]]
prediccion = modelo.predict(nuevo)
print("Código recomendado:", prediccion[0])