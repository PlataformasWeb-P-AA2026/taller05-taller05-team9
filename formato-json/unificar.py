import json

def unificar_datos():
    archivos = ['temp_europa.json', 'temp_sudamerica.json', 'temp_pdf.json']
    lista_final = []

    for nombre in archivos:
        try:
            with open(nombre, 'r', encoding='utf-8') as f:
                contenido = json.load(f)
                lista_final.extend(contenido)
                print(f"Cargados {len(contenido)} registros de {nombre}")
        except FileNotFoundError:
            print(f"No se encontró {nombre}")

    # Formato para CouchDB
    resultado = {"docs": lista_final}

    with open('mundial_2026.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=4, ensure_ascii=False)
    
    print("\nArchivo 'mundial_2026.json' generado.")

if __name__ == "__main__":
    unificar_datos()
