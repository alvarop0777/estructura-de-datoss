import json

# Ruta específica donde se encuentra el archivo JSON
ruta_json = r"C:\Users\Alvaricoque\Downloads\modified_champions_json.json"

# Cargar los datos del archivo JSON
with open(ruta_json, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

print("\n===== CUARTOS DE FINAL CHAMPIONS LEAGUE 2018-2019 =====\n")

# Lista para guardar semifinalistas
semifinalistas = []

# Recorrer cada partido (adaptado a la estructura real del JSON)
for partido in datos["cuartos_de_final_champions_2019"]:
    local = partido["local"]
    visitante = partido["visitante"]
    
    # Mostrar resultados
    print(f"\n{local} vs {visitante}")
    print(f"IDA: {local} {partido['resultado_ida']} {visitante}")
    print(f"VUELTA: {visitante} {partido['resultado_vuelta']} {local}")
    print(f"GLOBAL: {partido['global']}")
    
    # Mostrar tarjetas (adaptado a la estructura real del JSON)
    print(f"\nTarjetas:")
    print(f"- Amarillas {local}: {partido['tarjetas']['amarillas_local']}")
    print(f"- Amarillas {visitante}: {partido['tarjetas']['amarillas_visitante']}")
    print(f"- Rojas {local}: {partido['tarjetas']['rojas_local']}")
    print(f"- Rojas {visitante}: {partido['tarjetas']['rojas_visitante']}")
    
    # Añadir el equipo clasificado
    semifinalistas.append(partido['clasificado'])
    
    print("-" * 50)

# Mostrar equipos semifinalistas
print("\n===== EQUIPOS QUE AVANZAN A SEMIFINALES =====")
for i, equipo in enumerate(semifinalistas, 1):
    print(f"{i}. {equipo}")
