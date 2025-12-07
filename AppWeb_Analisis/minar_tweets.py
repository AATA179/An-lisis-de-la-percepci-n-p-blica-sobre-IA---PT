import asyncio
import autenticar as auth
import extraer
import guardar_json as saveJson
import conectar_mongodb as saveMongo
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    """
    Función principal para el minado de tweets
    """
    # Carga de variables del archivo .env
    load_dotenv()
    
    # Llaves de autenticación
    auth_token = os.getenv("auth_token") # Obtener desde el archivo .env
    ct0 = os.getenv("ct0") # ct0 sacado del navegador
    
    query = "Sora AI" # Palabra o hashtag a buscar
    cantidad = 5 # Número de tweets a extraer de 5 a 500 cada 20 minutos
    
    # Crear un cliente autenticado con las llaves ingresadas
    cliente = auth.crear_cliente(auth_token, ct0)
    
    # Ejecutar el programa de forma asincrónica para extraer los tweets
    registros = asyncio.run(extraer.buscar_tweets(cliente, query, cantidad))
    
    # Guardar los tweets en archivo JSON
    saveJson.guardar_tweets(registros) # Descomentar esta línea para guardar en archivo .JSON
    
    # Guardar en Base de Datos 'MongoDB'
    # URL del cluster donde se encuentra la base de datos
    url = os.getenv("url") # Obtener desde el archivo .env
    # Nombre de la base de datos
    bd = os.getenv("bd")
    # Nombre de la colección donde se guardarán los tweets
    coleccion = os.getenv("coleccion")
    
    # Crear coleccion para las operaciones en MongoDB
    tabla = saveMongo.establecer_conexion(url, bd, coleccion)
    
    # Guardar los tweets en la colección
    saveMongo.guardar_tweets(tabla, registros)