
from pymongo import MongoClient


def coneccionDB(mongo_uri:str,database_name:str,collection_name:str):
    "coneccion a una colecccion en base de datos"
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    print(f'coneccion exitosa a la coleccion: {database_name}.{collection_name}')
    return collection 



# collection.insert_one(infoGlobal) # info_Global: dict
# collection.insert_many(cerdos_registrados) #cerdos_registrado : list