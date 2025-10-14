import mysql.connector 

# Función para conectar a la base de datos
def connectionBD():
    return mysql.connector.connect(
    host="localhost",
    user="root", # Cambia por tu usuario de MySQL
    password="", 
    database="android_mysql"
)