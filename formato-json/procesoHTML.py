from bs4 import BeautifulSoup
import json

def extraer_html():
    try:
        with open('../data/fuente_html_europa.html', 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        jugadores = []
        tabla = soup.find('table')
        
        for fila in tabla.find_all('tr')[1:]:  # Saltar encabezado
            cols = fila.find_all('td')
            if len(cols) >= 5:  # Asegurarnos de que la fila tenga suficientes columnas
                jugadores.append({
                    "nombre": cols[0].text.strip(),
                    "club_actual": cols[1].text.strip(),
                    "posicion": cols[2].text.strip(), # Aquí estaba el error (era 'Portero')
                    "goles": int(cols[3].text.strip()) if cols[3].text.strip().isdigit() else 0,
                    "partidos": int(cols[4].text.strip()) if cols[4].text.strip().isdigit() else 0,
                    "seleccion": "Europa"
                })
        
        with open('temp_europa.json', 'w', encoding='utf-8') as f:
            json.dump(jugadores, f, indent=4)
        print("HTML procesado: temp_europa.json creado con éxito.")
        
    except Exception as e:
        print(f"Error procesando HTML: {e}")

if __name__ == "__main__":
    extraer_html()
