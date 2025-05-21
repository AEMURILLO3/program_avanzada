from conexion2 import conectar

db = conectar()

# Buscar clínicas
for clinica in db.clinicas.find({"medicos": {"$gt": 20}}):
    print("Clínica con más de 20 médicos:", clinica)

# Buscar parques
for parque in db.parques.find({"precio": {"$lt": 3}}):
    print("Parque con entrada económica:", parque)
