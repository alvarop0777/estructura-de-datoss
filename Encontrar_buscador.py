
import os
import re
from collections import Counter
import urllib.request

def captureDataFromURL(url):
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8', errors='ignore')  # Read and decode the content
        # Expresión regular para capturar la información del User-Agent
        regex_navegador = r'"Mozilla\/.*?\(.*?;.*?;\s(.*?)\).*?"'
        navegadores = re.findall(regex_navegador, content)
        return navegadores
    except Exception as e:
        print(f"Error al leer el archivo desde la URL: {e}")
        return None

def procesarNavegadores(datos_navegadores, nombre_archivo="URL"):
    if datos_navegadores:
        contador_navegadores = Counter(datos_navegadores)
        
        # Obtener el total de navegadores encontrados
        total_navegadores = sum(contador_navegadores.values())
        
        print(f"\n=== RESULTADOS DEL ANÁLISIS DE NAVEGADORES ===")
        print(f"Archivo: {nombre_archivo}")
        print(f"Total de navegadores encontrados: {total_navegadores}")
        print(f"Tipos diferentes de navegadores: {len(contador_navegadores)}")
        print("\n--- Desglose por tipo de navegador ---")
        
        # Ordenar por frecuencia (de mayor a menor)
        navegadores_ordenados = contador_navegadores.most_common()
        
        # Calcular el ancho máximo para alinear correctamente
        max_width = max(len(nav) for nav, _ in navegadores_ordenados)
        
        # Imprimir con formato de tabla
        print(f"{'NAVEGADOR':<{max_width+2}} | {'CANTIDAD':<8} | {'PORCENTAJE':<10}")
        print("-" * (max_width+2 + 1 + 8 + 1 + 10))
        
        for navegador, count in navegadores_ordenados:
            porcentaje = (count / total_navegadores) * 100
            print(f"{navegador:<{max_width+2}} | {count:<8} | {porcentaje:.2f}%")
            
    else:
        print(f"\nNo se encontraron navegadores o hubo un error al leer el archivo: {nombre_archivo}")

if __name__ == "__main__":
    log_url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs"
    
    print(f"Procesando el archivo desde la URL: {log_url}")
    navegadores = captureDataFromURL(log_url)
    procesarNavegadores(navegadores)
