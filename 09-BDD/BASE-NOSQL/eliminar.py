from conexion2 import conectar

db = conectar()

# Eliminar una clínica por nombre
db.clinicas.delete_one({"nombre": "Clínica Vida"})

# Eliminar todos los parques
# db.parques.delete_many({})
