from twikit import Client
from datetime import datetime
from typing import List, Dict

async def buscar_tweets(cliente: Client, query: str, cantidad: int) -> List[Dict[str, str]]:
    """
    Función asíncrona 'buscar_tweets'
    Permite ejecutar operaciones de busqueda de tweets sin bloquear el programa
    Las busquedas obtenidas las guarda en una lista para posteriormente llamar a 'guardar_tweets' 
    y guardarlo en un archivo .json
    
    Parámetros 
    -------------------------------
    cliente (Client): El cliente con la autenticación de cookies
    query      (str): La palabra a buscar 
    cantidad   (int): Número de tweets a buscar
    
    Regresa
    ------------------------------
    List[Dict[str, str]]: Una lista de diccionarios con los tweets extraídos
    """
    
    tweets_obtenidos = [] # Lista para guardar los tweets
    registros = [] # Lista para guardar el diccionario de tweets
    
    while len(tweets_obtenidos) < cantidad:
        tweets = await cliente.search_tweet(f"{query} lang:es", 'Top') # Extraer tweets en español
        
        if not tweets:
            break  # Si ya no hay más tweets, salimos del bucle

        tweets_obtenidos.extend(tweets)  # Agregar los nuevos tweets
        tweets_obtenidos = tweets_obtenidos[:cantidad]  # Limitar la cantidad
        
    for tweet in tweets_obtenidos:
        # Convertir la cadena de fecha a un objeto datetime
        fecha_objeto = datetime.strptime(tweet.created_at, "%a %b %d %H:%M:%S %z %Y")
        # Dar formato a la fecha
        fecha_con_formato = fecha_objeto.strftime("%Y-%m-%d %H:%M:%S")
        
        # Datos a agregar
        nuevo_tweet = {
            "id": tweet.id,
            "Fecha": fecha_con_formato,
            "Usuario": tweet.user.name,
            "Contenido": tweet.text,
            "Tema": query
        }
        # Agregar el tweet a la lista
        registros.append(nuevo_tweet)
    print(f"Tweets extraidos: {len(registros)}")
    
    return registros
    