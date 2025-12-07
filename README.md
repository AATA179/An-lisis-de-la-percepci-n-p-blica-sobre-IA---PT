# Análisis de la percepción pública sobre IA - Aplicación Web
Aplicación web que extrae tweets desde una base de datos, analiza su polaridad y muestra los resultados con gráficas.

## Estructura del proyecto
```
MinadoTweets/
├── minar_tweets.py           # Función para extraer tweets y guardarlos en un archivo JSON y en MongoDB Atlas
├── autenticar.py             # Crea un cliente autenticado con las cookies ingresadas para la extracción de tweets
├── extraer.py                # Busca tweets con un 'query' ingresado y los extrae con ayuda de la biblioteca -twikit-
├── guardar_json.py           # Guarda los tweets extraidos en un archivo .JSON
├── conectar_mongodb.py       # Permite la conexión con MongoDB Atlas y el almacenado de tweets
├── limpiar_tweets.py         # Contiene funciones para limpiar textos
├── analizar_sentimiento.py   # Obtiene la polaridad (positivo, negativo, neutro) de un texto ingresado
├── actualizar_mongodb.py     # Agrega un nuevo campo llamado 'Polaridad' con la respectiva polaridad del tweet a la base de datos
├── generar_graficas.py       # Contiene las funciones para generar gráficas de pastel y nubes de palabras sobre los tweets analizados
├── desplegar_app.py          # Despliega la aplicación web con Flask
├── .env                      # Se debe crear con las credenciales correspondientes
```

## Requisitos
- Python 3.13 o superior
- Biblioteca twikit
- Biblioteca dotenv
- Biblioteca pysentimiento
- Biblioteca pymongo
- Biblioteca flask
- Biblioteca base64
- Biblioteca wordcloud
- Biblioteca collections
- Cookies del navegador con una cuenta de X abierta

## Extracción de cookies
```
- En un navegador iniciar sesión en X
- Ctrl + Shift + I
- Dar click en la pestaña 'Application'
- Posteriormente en 'Cookies'
- Copiar los valores de 'auth_token' y 'ct0' necesarios en -main.py-
```
Nota: Esto es necesario hacerlo una sola vez, las cookies pueden servir incluso si se cierra sesión o el navegador. 

## Funcionalidades
- Conexión a la base de datos MongoDB Atlas
- Extracción de tweets recientes usando twikit (sin necesidad de la API X)
- Almacenamiento estructurado en archivos .json y en MongoDB Atlas
- Lectura de los tweets almacenados
- Clasificación de polaridad de textos
- Generación de:
    * Gráficas de pastel
    * Nubes de palabras
- Interfaz web desarrollada con Flask para visualizar resultados

## Ejemplo de formato de guardado de los tweets
```
{
  "Fecha": "2025-07-06 12:12:12",
  "Usuario": "@aata179",
  "Contenido": "Texto dentro del tweet",
  "Tema": "Ejemplo",
  "Polaridad": "POS"
},
```

## Archivo .env
El archivo NO se incluye en el repositorio por cuestiones de privacidad, pero se debe crear en la raíz del proyecto con estas variables:
```
# URL del cluster donde se encuentra la base de datos
url = mongodb+srv://...
# Nombre de la base de datos
bd = ...
# Nombre de la colección donde se guardarán los tweets
coleccion = ...

# Llaves de autenticación para extraer los tweets
auth_token = ...
ct0 = ...
```

## Como ejecutar el proyecto
Para desplegar la aplicación con flask
```
python desplegar_app.py
```
Para minar tweets
```
python minar_tweets.py
```
## Resultados
La aplicación web muestra:
- Gráficas de polaridad por cada IA
- Nubes de palabras filtradas
- Información resumida del análisis total con gráficas visuales

## Limitaciones
- El programa ```minar_tweets.py``` puede correrse una vez cada 20 minutos.

## Créditos
- Proyecto desarrollado por Aarón Torrijos Alvarado para la UAM Azcapotzalco.
- El diseño visual de la interfaz (paleta de colores, estructura visual y propuesta estética) fue realizado por Azul Torrijos Alvarado.
