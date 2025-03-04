import requests, re, json


def extractFromRegularExpresion(regex, data):
    if data:
        return re.findall(regex,data)
    return None
data = open("access.log","r")
regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\-\s\-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4})\:(\d{2}\:\d{2}\:\d{2})\s\+\d{4,6}\]\s\"(\b[A-Z]{3,7}\b)"

resultado = extractFromRegularExpresion(regex, data.read())

for i in range(len(resultado)):
    print(f"La ip: {resultado[i][0]}, la fecha es: {resultado[i][1]}, la hora: {resultado[i][2]} y el método: {resultado[i][3]}")
