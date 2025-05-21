#Script para insertar datos de ejemplo en las tablas

from conexion1 import obtener_conexion

def insertar_datos():
    con = obtener_conexion()
    cursor = con.cursor()

    # Insertar datos en Clínicas
    cursor.execute("""
        INSERT INTO ClinicasParticulares (nombre, direccion, telefono, especialidades, numero_doctores)
        VALUES (?, ?, ?, ?, ?)
    """, ('Clínica Santa María', 'Av. Siempre Viva 123', '0991234567', 'Cardiología, Pediatría', 15))

    cursor.execute("""
        INSERT INTO ClinicasParticulares (nombre, direccion, telefono, especialidades, numero_doctores)
        VALUES (?, ?, ?, ?, ?)
    """, ('Clínica Buenavista', 'Calle Falsa 456', '0997654321', 'Ginecología, Dermatología', 10))

    # Insertar datos en Parques
    cursor.execute("""
        INSERT INTO ParquesRecreativos (nombre, ubicacion, area_ha, cantidad_juegos, horario)
        VALUES (?, ?, ?, ?, ?)
    """, ('Parque Central', 'Centro de la ciudad', 5.4, 12, '08:00 - 18:00'))

    cursor.execute("""
        INSERT INTO ParquesRecreativos (nombre, ubicacion, area_ha, cantidad_juegos, horario)
        VALUES (?, ?, ?, ?, ?)
    """, ('Parque Infantil', 'Barrio La Paz', 2.2, 8, '09:00 - 17:00'))

    con.commit()
    con.close()

if __name__ == '__main__':
    insertar_datos()
    print("Datos insertados correctamente.")
