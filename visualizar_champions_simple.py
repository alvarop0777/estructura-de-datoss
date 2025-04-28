import json
import os

# Obtener la ruta del directorio actual donde está el script
directorio_actual = os.path.dirname(__file__)

# Construir la ruta completa al archivo JSON
ruta_json = os.path.join(directorio_actual, 'champions-2019-json.json')

# Cargar los datos del archivo JSON
with open(ruta_json, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

print("\n===== CUARTOS DE FINAL CHAMPIONS LEAGUE 2018-2019 =====\n")

# Recorrer cada partido
for partido_info in datos["cuartos_de_final_champions_2019"]:
    partido = partido_info["partido"]
    local = partido["local"]
    visitante = partido["visitante"]
    
    print(f"\n{local} vs {visitante}")
    print(f"IDA: {local} {partido['ida']['resultado']} {visitante}")
    print(f"VUELTA: {visitante} {partido['vuelta']['resultado']} {local}")
    print(f"GLOBAL: {partido['global']}")
    
    print("\nTarjetas Amarillas:")
    print(f"- {local} (IDA): {', '.join(partido['ida']['tarjetas_amarillas'].get(local, []) or ['Ninguna'])}")
    print(f"- {visitante} (IDA): {', '.join(partido['ida']['tarjetas_amarillas'].get(visitante, []) or ['Ninguna'])}")
    print(f"- {local} (VUELTA): {', '.join(partido['vuelta']['tarjetas_amarillas'].get(local, []) or ['Ninguna'])}")
    print(f"- {visitante} (VUELTA): {', '.join(partido['vuelta']['tarjetas_amarillas'].get(visitante, []) or ['Ninguna'])}")
    
    print("\nTarjetas Rojas:")
    print(f"- {local} (IDA): {', '.join(partido['ida']['tarjetas_rojas'].get(local, []) or ['Ninguna'])}")
    print(f"- {visitante} (IDA): {', '.join(partido['ida']['tarjetas_rojas'].get(visitante, []) or ['Ninguna'])}")
    print(f"- {local} (VUELTA): {', '.join(partido['vuelta']['tarjetas_rojas'].get(local, []) or ['Ninguna'])}")
    print(f"- {visitante} (VUELTA): {', '.join(partido['vuelta']['tarjetas_rojas'].get(visitante, []) or ['Ninguna'])}")
    
    print("-" * 50)
