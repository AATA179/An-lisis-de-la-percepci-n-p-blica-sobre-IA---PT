import json 
from typing import List, Dict

def guardar_tweets (registros: List[Dict[str, str]])-> None:
    """
    Agrega la lista de tweets con formato a un archivo json
    
    Parámetros
    -----------------------------
    registros (List[Dict[str, str]): Lista de diccionarios con los tweets
    
    Regresa
    -----------------------------
    None: Imprime en consola el estado del programa y extracción de tweets
    """
    
    archivo_json = "tweets.json" # Nombre del archivo .json donde se guardaran los tweets

    if not registros:
        print("No se agregó ningún tweet")
        return 

    # Intentar leer el archivo JSON, si no existe, crear una lista vacía
    try:
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            tweets = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        tweets = []  # Si el archivo no existe o está vacío, se usa una lista vacía

    # Agregar los nuevos registros sin borrar los existentes
    tweets.extend(registros)

    # Guardar los datos actualizados
    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(tweets, archivo, indent=4, ensure_ascii=False)

    print(f"{len(registros)} Tweets agregados correctamente en el archivo .json")