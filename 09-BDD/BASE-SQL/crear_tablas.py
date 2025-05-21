#Crea las tablas ClinicasParticulares y ParquesRecreativos con sus características

from conexion1 import obtener_conexion

def crear_tablas():
    con = obtener_conexion()
    cursor = con.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ClinicasParticulares (
            id_clinica INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT,
            especialidades TEXT,
            numero_doctores INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ParquesRecreativos (
            id_parque INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ubicacion TEXT,
            area_ha REAL,
            cantidad_juegos INTEGER,
            horario TEXT
        )
    """)

    con.commit()
    con.close()

if __name__ == '__main__':
    crear_tablas()
    print("Tablas creadas correctamente.")
