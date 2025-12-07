from flask import Flask, request
from generar_graficas import generar_nube, generar_pastel
import conectar_mongodb as Mongodb
import base64
from dotenv import load_dotenv
import os

# Carga de variables del archivo .env
load_dotenv()

# URL del cluster donde se encuentra la base de datos
url = os.getenv("url") # Obtener desde el archivo .env
# Nombre de la base de datos
bd = os.getenv("bd")
# Nombre de la colección donde se guardarán los tweets
coleccion = os.getenv("coleccion")

# Establecer conexión con la base de datos
collection = Mongodb.establecer_conexion(url, bd, coleccion)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():

    return """
    <html>
    
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            h1 {
                font-size: 56px !important;
            }
            option {
                font-weight: bold;
            }
            select {
                font-weight: bold !important;
            }
            button {
                background-color: #1B6F25 !important;
                color: white !important;
            }
            footer {
                background-color: #1B6F25;
            }
        </style>
    </head>
    
    <body style="background-color: #6DD179;" class="text-white d-flex flex-column min-vh-100">
        <div class="container mt-5 text-center">
            <h1 class="mb-4">Análisis de la percepción pública sobre IA</h1>

            <form action="/Analisis" method="GET" class="mx-auto" style="max-width: 350px;">
                <select name="opcion" class="form-select mb-3">
                    <option value="ChatGPT">ChatGPT</option>
                    <option value="DeepSeek">DeepSeek</option>
                    <option value="Gemini">Gemini</option>
                    <option value="Google Veo">Google Veo</option>
                    <option value="Microsoft Copilot">Copilot</option>
                    <option value="Sora AI">Sora AI</option>
                </select>

                <button type="submit" class="btn w-100">Buscar</button>
            </form>
        </div>

        <footer class="mt-auto text-center py-3 text-white">
            <p class="mb-0">&copy; 2025 Alvarado Aarón</p>
        </footer>
    </body>
    </html>
    """

@app.route("/Analisis", methods=["GET"])
def analisis():
    opcion = request.args.get("opcion")
    buffer1 = generar_pastel(collection, opcion)
    buffer2 = generar_nube(collection, opcion)

    # convertir a base64
    pastel = base64.b64encode(buffer1.getvalue()).decode("utf-8")
    nube = base64.b64encode(buffer2.getvalue()).decode("utf-8")
    
    return f"""
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .custom-header {{
                background-color: #1B6F25;
                color: white;
                padding: 15px;
                text-align: center;
                font-weight: bold;
                font-size: 36px;
            }}
        </style>
    </head>
    
    <body class="d-flex flex-column min-vh-100">
        <div class="custom-header"> Clasificación de polaridad de {opcion} </div>
        
        <div class="container my-4 d-flex justify-content-center align-items-end gap-5">
            <div class="text-center me-5">
                <img src="data:image/png;base64,{pastel}">
                <p class="fst-italic">Distribución de comentarios por polaridad</p>
            </div>
            <div class="text-center">
                <img src="data:image/png;base64,{nube}">
                <p class="fst-italic" style="margin-top: 55px;">Nube de palabras generada con los comentarios más destacados</p>
            </div>
        </div>
        
        <footer style="background-color: #1B6F25;" class="mt-auto text-center py-3 text-white">
            <p class="mb-0">&copy; 2025 Alvarado Aarón</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Correr la app, cualquier host (dispositivo) puede ingresar a ella
    app.run(host="0.0.0.0", port=1709, debug=True)