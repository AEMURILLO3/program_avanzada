from conexion2 import conectar

db = conectar()

# Insertar clínicas
clinicas = [
    {"nombre": "Clínica Vida", "direccion": "Av. Siempre Viva 123", "especialidades": ["Pediatría", "Cardiología"], "medicos": 25},
    {"nombre": "Salud Total", "direccion": "Calle Falsa 456", "especialidades": ["Dermatología", "Neurología"], "medicos": 18}
]
db.clinicas.insert_many(clinicas)

# Insertar parques
parques = [
    {"nombre": "Parque Central", "ubicacion": "Centro", "atracciones": ["Juegos infantiles", "Lago artificial"], "horario": "08:00-18:00", "precio": 2.0},
    {"nombre": "EcoParque", "ubicacion": "Norte", "atracciones": ["Senderos", "Zoológico"], "horario": "09:00-17:00", "precio": 3.5}
]
db.parques.insert_many(parques)
