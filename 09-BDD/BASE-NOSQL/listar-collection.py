from conexion2 import conectar

db = conectar()

print("Colecciones disponibles:", db.list_collection_names())

print("\nClínicas:")
for clinica in db.clinicas.find():
    print(clinica)

print("\nParques:")
for parque in db.parques.find():
    print(parque)
