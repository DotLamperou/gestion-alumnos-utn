import json

ARCHIVO = "alumnos.json"

def obtener_edad_validada():
    while True:
        try:
            entrada = input("Ingrese su edad: ")
            edad = int(entrada)
            if 18 <= edad <= 100:
                return edad
            print("Error: Edad fuera de rango (18-100).")
        except ValueError:
            print("Error: Ingrese un número válido.")

def guardar_datos(lista):
    with open(ARCHIVO, "w") as f:
        json.dump(lista, f, indent=4)

def cargar_datos():
    try:
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def buscar_alumno(lista, nombre_buscado):
    for alu in lista:
        if alu["nombre"].lower() == nombre_buscado.lower():
            return alu  # Devolvemos el diccionario del alumno encontrado
    return None  # Si terminó el bucle y no encontró nada