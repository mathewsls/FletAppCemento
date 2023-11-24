from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://morocho:morocho@cluster0.tgzyb0a.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.Datos
collection = db.Datos_Tablas



def consultar():
    list = []
    cursor = collection.find()
    for document in cursor:
        list.append(document)
    return list
def agregar(dato):
    collection.insert_one(dato)

def eliminar(dato):
    collection.delete_one({"remision": dato})
