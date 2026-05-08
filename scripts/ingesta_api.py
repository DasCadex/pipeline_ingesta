import requests, json, os
from datetime import datetime

def ingestar_desde_api(url: str, destino_carpeta: str) -> None:
    os.makedirs(destino_carpeta, exist_ok=True)
    print(f"Consultando API: {url}")
    respuesta = requests.get(url, timeout=10)

    if respuesta.status_code == 200:
        datos      = respuesta.json()
        timestamp  = datetime.now().strftime('%Y%m%d_%H%M%S')
        archivo    = os.path.join(destino_carpeta, f'datos_{timestamp}.json')
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        print(f"[OK] Guardado en: {archivo}")
    else:
        print(f"[ERROR] Codigo: {respuesta.status_code}")

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    ingestar_desde_api(url, "data/raw")