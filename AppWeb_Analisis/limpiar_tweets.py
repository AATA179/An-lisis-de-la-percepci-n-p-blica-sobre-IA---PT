import re # Para limpiar textos
from collections import Counter # Para la frecuencia de palabras

def limpiar (texto: str) -> str:
    """
    Recibe el texto a limpiar (tweet) y lo devuelve sin links, menciones y/o hashtags
    
    Parámetros
    -------------------------------
    texto (str): Tweet a limpiar 
    
    Regresa
    -------------------------------
    str: Tweet sin menciones, links ni hashtags
    """
    texto = re.sub(r"http\S+|www.\S+|@\w+|#\w+", "", texto).strip() # Limpiar texto
    
    return texto

def tokenizar (texto: str) -> Counter:
    """
    Tokeniza el texto y regresa la frecuencia de cada palabra (el número de veces que 
    se repite)
    
    Parámetros
    ------------------------------
    texto (str): Texto a tokenizar
    
    Regresa
    ------------------------------
    Counter: Diccionario de frecuencias de cada palabra
    """
    
    texto = limpiar(texto)
    # Pasar texto a minúsculas
    texto = texto.lower()
    # Quitar signos, carácteres y números
    texto = re.sub(r'[^a-záéíóúñ]', ' ', texto)
    
    # Lista de conectores para eliminarlos del texto
    conectores = [
        "el", "la", "los", "las", "de", "del", "a", "y", "o", "ó", "que", "qué", "en", "es",
        "un", "una","por", "para", "con", "se", "al", "le", "lo", "como", "su", "sus", "mas",
        "más", "si", "sí", "no", "tras", "yo", "ti", "tu", "tú", "dan", "te", "me", "mi", "va",
        "ir", "donde", "pero", "para", "eso", "esa", "porque", "ellos", "ellas", "nosotros", 
        "nosotras", "tienes", "tener", "esta", "está"
    ]
    # Tokenizar el texto (separar cada palabra)
    palabras = texto.split()
    
    # Filtrar el texto quitando los conectores
    palabras = [palabra for palabra in palabras if palabra not in conectores]

    return Counter(palabras)