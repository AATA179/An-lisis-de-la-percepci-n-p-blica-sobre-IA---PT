import conectar_mongodb as Mongodb
from analizar_sentimiento import clasificar
from dotenv import load_dotenv
import os

def actualizar (url:str, bd:str, coleccion:str) -> None:
    """
    Agrega el campo "Polaridad" con su respectiva polaridad de cada tweet en la colección.
    
    Parámetros
    -------------------------------
    url       (str): URL de la base de datos en MongoDB
    bd        (str): Nombre de la base de datos
    coleccion (str): Coleccion-tabla con la que se trabaja
    
    Regresa
    ------------------------------
    None: Imprime en consola cuantos tweets se actualizaron con éxito
    """
    
    # Establecer conexión con la base de datos
    collection = Mongodb.establecer_conexion(url, bd, coleccion)

    # Consultar los valores distintos (Para actualizar por IA)
    Temas = collection.distinct("Tema")

    # Actualizar los archivos de la base de datos para agregar el campo 'Polaridad'
    # Actualizar la polaridad de todos los archivos

    contador = 0 # Para llevar control de los tweets que se actualizan
    print(f"Total de tweets: {collection.count_documents({})}")

    for tema in Temas:
        Documentos = collection.find({"Tema": tema})
        for documento in Documentos:
            tweet = documento.get("Contenido")
            polaridad = clasificar(tweet)
            collection.update_one({"id": documento["id"]}, {"$set": {"Polaridad": polaridad}})
            contador += 1

    print(f"Tweets actualizados: {contador}")

if __name__ == "__main__":
    
    # Carga de variables del archivo .env
    load_dotenv()

    # URL del cluster donde se encuentra la base de datos
    url = os.getenv("url") # Obtener desde el archivo .env
    # Nombre de la base de datos
    bd = os.getenv("bd")
    # Nombre de la colección donde se guardarán los tweets
    coleccion = os.getenv("coleccion")

    actualizar(url, bd, coleccion)