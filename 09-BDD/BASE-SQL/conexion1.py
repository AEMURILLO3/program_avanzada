#Función para obtener conexión a SQLite

import sqlite3

def obtener_conexion():
    return sqlite3.connect("09-BDD/BASE-SQL/app.db")
