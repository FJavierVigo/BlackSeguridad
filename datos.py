
import json
from pathlib import Path


RUTA_ARCHIVO = Path(__file__).with_name("datos.json")


def buscar_agente(agentes):
    print("\n--- BUSCAR AGENTE ---")
    consulta = input("Nombre o parte del nombre: ").strip().lower()
    consulta = consulta.replace("  ", " ")
    palabras = consulta.split()

    if not palabras:
        print("Error: escribe un nombre para buscar.")
        return

    encontrados = 0
    for agente in agentes:
        nombre = agente["nombre"].lower()
        if all(palabra in nombre for palabra in palabras):
            print(f"Código: {agente['codigo']} | Nombre: {agente['nombre']}")
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron agentes con ese nombre.")


def guardar_datos(datos):
    try:
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
        print("Información guardada correctamente.")
        return True
    except OSError as error:
        print("No se pudo guardar la información:", error)
        return False


def cargar_datos():
    datos_vacios = {"agentes": [], "puestos": [], "turnos": []}

    if not RUTA_ARCHIVO.exists():
        return datos_vacios

    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if not isinstance(datos, dict):
            raise ValueError("El archivo no tiene la estructura esperada.")
        if not all(isinstance(datos.get(clave), list) for clave in datos_vacios):
            raise ValueError("Faltan listas de agentes, puestos o turnos.")
        return datos
    except (OSError, ValueError) as error:
        print("No se pudo cargar la información:", error)
        return datos_vacios
