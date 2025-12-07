from pysentimiento import create_analyzer # Modelo preentrenado para análisis de textos en español
from limpiar_tweets import limpiar

def clasificar (tweet:str) -> str:
    """
    Recibe un tweet y lo clasifica en base a su polaridad ('POS', 'NEG', 'NEU') usando 
    'pysentimiento' la cual usa modelos ya entrenados para análisis de textos en español.
    
    Parámetros
    ----------------------------------
    tweet (str): Tweet a clasificar en base a su polaridad
    
    Regresa
    ----------------------------------
    str: Polaridad del tweet ['POS', 'NEG','NEU'], positivo negativo o neutro respectivamente
    """
    
    # Crear analizador de sentimiento en español
    analyzer = create_analyzer(task="sentiment", lang="es")

    # Limpiar el texto
    tweet = limpiar(tweet)

    # Analizar polaridad
    resultado = analyzer.predict(tweet)

    polaridad = resultado.output # POS, NEG o NEU
    
    return polaridad