import re

def extract_from_regular_expression(regex, data):
    """Extrae datos de un texto usando una expresión regular."""
    if data:
        return re.findall(regex, data)
    return None

# Definir expresiones regulares
regex_ips = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # IPs
regex_errores = r'"\s(\d{3})\s\d{4,5}\s"'  # Códigos de estado HTTP

# Leer el archivo y extraer datos
file = open("C:\\Users\\306\\Downloads\\access.log\\access.log", "r")
contenido = file.read()
data = contenido
file.close()

# Extraer IPs y errores usando las expresiones regulares
resultado_ips = extract_from_regular_expression(regex_ips, data)
resultado_errores = extract_from_regular_expression(regex_errores, data)

# Convertir errores en enteros
if resultado_errores:
    resultado_errores = [int(e) for e in resultado_errores]

# Usamos set para asegurarnos de que solo imprimimos IPs únicas
ips_unicas = set(resultado_ips) if resultado_ips else set()

# Inicializar contadores de errores
error_100 = 0
error_200 = 0
error_300 = 0
error_400 = 0
error_500 = 0

# Contar errores HTTP por categorías
if resultado_errores:
    for error in resultado_errores:
        if 100 <= error < 200:
            error_100 += 1
        elif 200 <= error < 300:
            error_200 += 1
        elif 300 <= error < 400:
            error_300 += 1
        elif 400 <= error < 500:
            error_400 += 1
        elif 500 <= error < 600:
            error_500 += 1

# Imprimir las IPs únicas
print("\nIPs únicas encontradas:")
for ip in ips_unicas:
    print(ip)

# Imprimir el conteo de errores
print("\nCantidad de errores HTTP:")
print(f"100: {error_100}\n200: {error_200}\n300: {error_300}\n400: {error_400}\n500: {error_500}")
