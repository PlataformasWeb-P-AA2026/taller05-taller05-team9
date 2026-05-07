import pandas as pd
import json

def extraer_csv():
    # Leemos el CSV desde la carpeta data
    df = pd.read_csv('../data/fuente_csv_sudamerica.csv')
    
    # Convertimos a lista de diccionarios
    jugadores = df.to_dict('records')
    
    with open('temp_sudamerica.json', 'w') as f:
        json.dump(jugadores, f)
    print("CSV procesado: temp_sudamerica.json creado.")

if __name__ == "__main__":
    extraer_csv()
