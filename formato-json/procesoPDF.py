import pdfplumber
import json

def extraer_pdf():
    jugadores = []
    try:
        with pdfplumber.open("../data/fuente_pdf_norteamerica_asia.pdf") as pdf:
            for pagina in pdf.pages:
                tabla = pagina.extract_table()
                if tabla:
                    # El error sugiere que fila[2] es la posición, no los goles.
                    # Vamos a ajustar los índices:
                    for fila in tabla[1:]: 
                        if not fila[0]: continue # Saltar filas vacías
                        
                        jugadores.append({
                            "nombre": fila[0],
                            "club_actual": fila[1],
                            "posicion": fila[2],  # Aquí estaba el error
                            "goles": int(fila[3]) if fila[3] and fila[3].isdigit() else 0,
                            "partidos": int(fila[4]) if fila[4] and fila[4].isdigit() else 0,
                            "seleccion": fila[5] if len(fila) > 5 else "N/A"
                        })
        
        with open('temp_pdf.json', 'w') as f:
            json.dump(jugadores, f)
        print("PDF procesado: temp_pdf.json creado con éxito.")
    except Exception as e:
        print(f"Error en PDF: {e}")

if __name__ == "__main__":
    extraer_pdf()

