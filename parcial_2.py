import os
import requests
import re

def captureDataFromFile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            regexExpresion = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\b[A-Z]{3,7}\b\s(.*?)\s.*?(\d{3})"
            regex = re.findall(regexExpresion, content, re.MULTILINE)
            return regex
    except Exception as e:
        print(f"Error capturando datos de {file_path}: {e}")
        return None

def apiRequestData(data):
    JsonData = []
    if not data:
        print("No hay datos para procesar.")
        return

    URI = "http://ip-api.com/json/"
    ip_seen = set()

    for ip, path, code in data:
        if ip in ip_seen:
            continue  # Ya procesada

        ip_seen.add(ip)
        formatData = {"ip": ip, "code": code, 'path': path}

        try:
            response = requests.get(f"{URI}{ip}").json()
            formatData["country"] = response.get("country")
            formatData["city"] = response.get("city")
        except Exception as e:
            formatData["country"] = None
            formatData["city"] = None

        JsonData.append(formatData)
    return JsonData

# Directorio donde están los archivos
carpeta = "C:\\Users\\306\\Downloads\\http"

# Procesar cada archivo en la carpeta
for archivo in os.listdir(carpeta):
    file_path = os.path.join(carpeta, archivo)
    if os.path.isfile(file_path):  # Verifica que sea un archivo
        print(f"\nProcesando archivo: {archivo}")
        datos = captureDataFromFile(file_path)
        resultado = apiRequestData(datos)

        if resultado:
            print(f"{'IP':<16} {'País':<20} {'Código':<10} {'Tipo de Error'}")
            print("-" * 70)
            for entry in resultado:
                ip = entry.get("ip", "N/A")
                pais = entry.get("country") or "Desconocido"

                codigo = int(entry.get("code", 0))
                
                if codigo == 401:
                    error_tipo = "Intento fallido de inicio de sesión"
                elif codigo == 403:
                    error_tipo = "Acceso bloqueado (posible firewall)"
                elif codigo == 404:
                    error_tipo = "Acceso inusual o solicitud sospechosa"
                elif 500 <= codigo <= 599:
                    error_tipo = "Posibles alertas de seguridad"
                else:
                    continue  # Ignorar otros códigos

                print(f"{ip:<16} {pais:<20} {codigo:<10} {error_tipo}")
