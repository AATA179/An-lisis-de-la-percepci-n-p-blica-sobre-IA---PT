import matplotlib
matplotlib.use('Agg') # Evita GUI para que no se generen errores al mantener abierta la app web
import matplotlib.pyplot as plt
from pymongo.collection import Collection
from wordcloud import WordCloud
from limpiar_tweets import tokenizar
from io import BytesIO # Para guardar la imagen en buffer

def generar_pastel (collection: Collection, IA:str) -> BytesIO:
    """
    Genera la gráfica de pastel de las polaridades de cada IA
    
    Parámetros
    ----------------------------------
    collection (Collection): Objeto de PyMongo que representa la tabla para trabajar con los tweets
    IA                (str): IA de la cual se va a generar la gráfica
    
    Regresa
    ---------------------------------
    BytesIO: Buffer en memoria que contiene la imagen generada en PNG 
    """
    
    labels = ['POS', 'NEG', 'NEU']
    valores = [
        collection.count_documents({"Polaridad": p, "Tema": IA})
        for p in labels
    ]
    
    colores = ['#8ED973', '#6DD179', '#339933']
    
    # Crear figura (para evitar que las gráficas se empiecen a encimar)
    fig, ax = plt.subplots()
    ax.pie(valores, labels=labels, autopct='%1.1f%%', colors=colores) # Generar gráfica

    # Guardar en buffer
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight') # Guardar en png sin escribir en el disco
    buffer.seek(0) # Regresa el cursor del buffer al inicio

    plt.close(fig)  # liberar memoria

    return buffer

def generar_nube(collection: Collection, IA:str) -> BytesIO:
    """
    Genera la nube de palabras en base a la frecuencia de palabras en los tweets positivos y negativos
    
    Parámetros
    ----------------------------------
    collection (Collection): Objeto de PyMongo que representa la tabla para trabajar con los tweets
    IA                (str): IA de la cual se va a generar la nube de palabras
    
    Regresa
    ---------------------------------
    BytesIO: Buffer en memoria que contiene la imagen generada en PNG 
    """
    
    Documentos = collection.find({
        "Tema": IA, # Buscar los que contenga en campo Tema = {IA}
        "Polaridad": { "$in": ["POS", "NEG"] } # Extraer solo los de polaridad positiva o 
                                               # negativa, esto porque los neutros en su mayoría
                                               # son anuncios, cursos o títulos de imágenes o 
                                               # videos creados con IA
    })
    # Concatenar todos los tweets de la consulta anterior
    texto = " ".join(documento.get("Contenido") for documento in Documentos)
    # Tokenizar 'texto' y obtener la frecuencia de cada palabra
    frecuencia = tokenizar(texto)
    
    # Crear figura (para evitar que las gráficas se empiecen a encimar)
    fig, ax = plt.subplots()
    
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate_from_frequencies(frecuencia)

    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    
    # Guardar en buffer
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight') # Guardar en png sin escribir en el disco
    buffer.seek(0) # Regresa el cursor del buffer al inicio

    plt.close(fig)  # liberar memoria

    return buffer
