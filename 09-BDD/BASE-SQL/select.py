
#Consultas para obtener información de las tablas

from conexion1 import obtener_conexion

def clinicas_mas_de_n_doctores(n):
    con = obtener_conexion()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ClinicasParticulares WHERE numero_doctores > ?", (n,))
    resultados = cursor.fetchall()
    con.close()
    return resultados

def parques_mas_de_n_juegos(juegos):
    con = obtener_conexion()
    cursor = con.cursor()
    cursor.execute("SELECT nombre, ubicacion FROM ParquesRecreativos WHERE cantidad_juegos > ?", (juegos,))
    resultados = cursor.fetchall()
    con.close()
    return resultados

def clinicas_con_especialidad(especialidad):
    con = obtener_conexion()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ClinicasParticulares WHERE especialidades LIKE ?", ('%' + especialidad + '%',))
    resultados = cursor.fetchall()
    con.close()
    return resultados

if __name__ == '__main__':
    print("Clínicas con más de 10 doctores:")
    for clinica in clinicas_mas_de_n_doctores(10):
        print(clinica)

    print("\nParques con más de 10 juegos:")
    for parque in parques_mas_de_n_juegos(10):
        print(parque)

    print("\nClínicas con especialidad en Cardiología:")
    for clinica in clinicas_con_especialidad('Cardiología'):
        print(clinica)
