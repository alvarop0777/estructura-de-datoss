import re
from collections import Counter

def extract_from_regular_expression(regex, data):
    return re.findall(regex, data) if data else []

# Expresiones regulares
regex_ips = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  # Extrae IPs
regex_errores = r'"\s(\d{3})\s'  # Extrae códigos de error HTTP (100-599)

# Leer el archivo una sola vez
with open(r"C:\Users\user\Downloads\access.log", "r") as file:
    data = file.read()

# Extraer IPs y códigos de error
ips = extract_from_regular_expression(regex_ips, data)
errores = extract_from_regular_expression(regex_errores, data)

# Filtrar IPs únicas y contar errores
ips_unicas = set(ips)  # Elimina duplicados automáticamente
conteo_errores = Counter(errores)  # Cuenta cuántas veces aparece cada error

# Imprimir resultados
print("IPs únicas encontradas:")
for ip in ips_unicas:
    print(ip)

print("Conteo de errores HTTP:")
for codigo, cantidad in sorted(conteo_errores.items()):
    print(f"Error {codigo}: {cantidad} veces")
