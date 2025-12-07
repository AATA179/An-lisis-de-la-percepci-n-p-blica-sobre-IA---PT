from pymongo import MongoClient # Para la conexión con la BD
from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError
from typing import List, Dict

def establecer_conexion (url:str, database:str, coleccion:str) -> Collection:
    """
    Se establece la conexión con la base de datos donde se guardarán los tweets recolectados.
    
    Parámetros
    -----------------------------
    url       (str): URL de la base de datos en MongoDB
    database  (str): Nombre de la base de datos
    coleccion (str): Coleccion-tabla con la que se trabaja
    
    Regresa
    -----------------------------
    Collection: Objeto de PyMongo que representa la colección (tabla) donde se pueden 
    hacer operaciones como insert, find, etc.
    """
    # Conexión a la base de datos
    cliente = MongoClient(url)

    db = cliente[database]
    tabla = db[coleccion]  
    
    return tabla

def guardar_tweets (tabla:Collection, registros: List[Dict[str, str]])-> None:
    """
    Agrega la lista de tweets con formato a la base de datos en MongoDB
    
    Parámetros
    -----------------------------
    tabla              (Collection): Colección (tabla) en la base de datos donde se agregarán los tweets
    registros (List[Dict[str, str]): Lista de diccionarios con los tweets
    
    Regresa
    -----------------------------
    None: Imprime en consola el estado del programa y extracción de tweets
    """
    
    if not registros:
        print("No se agregó ningún tweet")
        return 

    # Contar cuantos tweets se insertan a la tabla
    contador = 0
    # Evitar insertar tweets duplicados
    for tweet in registros:
        try:
            tabla.insert_one(tweet)
            contador += 1
        except DuplicateKeyError:
            pass  # Ya existe el tweet


    print(f"{contador} Tweets agregados correctamente en la base de datos")