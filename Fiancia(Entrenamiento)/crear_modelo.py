import pandas as pd #Libreria pandas, manejo de archivos
from sklearn.model_selection import train_test_split # Divide los datos en entrenamiento y prueba
from sklearn.ensemble import RandomForestClassifier # Una Random Forest es un conjunto de muchos árboles de decisión. Cada árbol da su predicción, y se vota por mayoría.
from sklearn.metrics import classification_report, accuracy_score # Los "puntos" o "acurracy" del modelo
import joblib

datos = pd.read_csv("Fiancia(Receptor)/resultado_analisis.csv")

X = datos.drop(columns=["codigo_recomendacion"])  # Borra la columna "codigo recomendacion", sin actualizar la variable (datos.drop)
y = datos["codigo_recomendacion"]  # Solo se añade la variable que queremos que analice

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #(dato x a separar, dato y a separar, cuanto se usa para prueba, y una semilla de generacion establecida)

modelo = RandomForestClassifier(n_estimators=100, random_state=42) 
modelo.fit(X_train, y_train)


y_pred = modelo.predict(X_test)

print("Reporte de clasificación:")
print(classification_report(y_test, y_pred))
print("Precisión general:", accuracy_score(y_test, y_pred))


nuevo_usuario = pd.DataFrame([{
    "Ingreso_mensual": 800000,
    "Balance": -500000,
    "Ahorro_total": 100000,
    "Gasto_viveres": 400000,
    "Gasto_renta": 350000,
    "Gasto_electricidad": 80000,
    "Gasto_agua": 50000,
    "Gasto_transporte": 50000,
    "Gasto_educacion": 40000,
    "Gasto_equipamiento_mantenimiento_hogar": 0,
    "Gasto_gas": 0,
    "Gasto_ocio": 0,
    "Gasto_aficcion": 0,
    "gastos_indefinidos": 0,
    "deudas": 200000,
    "suscripciones": 10000,
    "pagos_tarjeta": 50000
}])

prediccion = modelo.predict(nuevo_usuario)
print("Recomendación para nuevo usuario:", prediccion[0])



joblib.dump(modelo, "modelo_finanzas.pkl")
