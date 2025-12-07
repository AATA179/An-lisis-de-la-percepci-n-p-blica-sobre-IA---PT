from twikit import Client

def crear_cliente (auth_token: str, ct0: str) -> Client:
    """
    Usa las cookies de un usuario de X existente (para obtener las cookies se inicia sesión en X en 
    un navegador)
    
    Parámetros
    -------------------------------
    auth_token (str): Token para autenticar la sesión de X por medio de las cookies del navegador
    ct0        (str): Token usado por Twitter para asegurarse de que las solicitudes provienen de 
                      una sesión legítima y no de un sitio malicioso
    
    Regresa
    ------------------------------
    Client : Un objeto tipo Client de twikit
    """
    # Crear cliente con cookies directamente
    cliente = Client(cookies={
        "auth_token": auth_token,
        "ct0": ct0
    }, language="es")  # Configurar el idioma del inicio de sesión en español 
    
    return cliente