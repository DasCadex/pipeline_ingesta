import shutil 
import os 
import logging 
from datetime import datetime

#-- 1. Configuración del logging-----------------------
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/ingesta.log"),#guarada en un archivo de log
        logging.StreamHandler()#muetra en consola el log
    ]


)


#--2. funcion de la ingesta -----------------------
def ingestar(origen: str, destino_carpeta:str) -> None:
    """Copia un archivo desde origen hacia destino_carpeta, creando la carpeta si no existe."""
    os.makedirs(destino_carpeta, exist_ok=True)
    nombre= os.path.basename(origen)
    destino= os.path.join(destino_carpeta, nombre)

    logging.info(f"Iniciando ingesta del archivo: (origen)")

    try :
        shutil.copy(origen, destino)
        logging.info(f"Iniciando ingesta: {origen}")

    except FileNotFoundError:
        logging.error(f"[ERROR] no se encontro el archivo : {origen}")
        raise
#-- 3 . Ejecución del script-----------------------
if __name__ == "__main__":
    ingestar("datos_prueba.csv", "data/raw")
    logging.info("Ingesta completada exitosamente")