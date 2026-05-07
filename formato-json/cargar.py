import requests
import json

# Configuracion basada en tu puerto 5985 y credenciales locales
URL_BASE = "http://admin:admin@localhost:5985"
DB_NAME = "jugadores"
URL_DB = f"{URL_BASE}/{DB_NAME}"

def ejecutar_carga():
    print(f"Iniciando conexion con CouchDB en puerto 5985...")
    
    # 1. Intentar crear la base de datos
    
    try:
        requests.put(URL_DB)
    except Exception as e:
        print(f"Error de conexion inicial: {e}")
        return

    # 2. Leer el archivo unificado generado anteriormente
    try:
        with open('mundial_2026.json', 'r', encoding='utf-8') as f:
            datos_json = json.load(f)
        
        
        
        headers = {'Content-Type': 'application/json'}
        respuesta = requests.post(
            f"{URL_DB}/_bulk_docs", 
            json=datos_json, 
            headers=headers
        )
        
        if respuesta.status_code == 201:
            print("Carga finalizada con exito.")
            print(f"Base de datos actualizada: {URL_DB}")
        else:
            print(f"Error en la carga masiva. Status: {respuesta.status_code}")
            print(f"Detalle: {respuesta.text}")

    except FileNotFoundError:
        print("Error: El archivo 'mundial_2026.json' no existe en este directorio.")
    except json.JSONDecodeError:
        print("Error: El archivo 'mundial_2026.json' no tiene un formato JSON valido.")
    except Exception as e:
        print(f"Error inesperado durante la ejecucion: {e}")

if __name__ == "__main__":
    ejecutar_carga()
