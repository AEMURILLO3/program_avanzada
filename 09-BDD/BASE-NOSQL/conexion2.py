from pymongo import MongoClient

def conectar():
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["servicios_ciudad"]
    return db