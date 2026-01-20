from datetime import date
import json

ARCHIVO = "datos.json"


def escribir_data():
    print("No se ha encontrado un archivo de datos. Vamos a configurarlo.")

    nombre = input("Ingrese su nombre: ")
    objetivo = input("¿En qué actividad deseas avanzar?: ")

    while True:
        try:
            dias = int(input(f"Bien, {nombre}, ¿cuál es tu objetivo semanal?: "))
            break
        except ValueError:
            print("Por favor ingresa un número válido.")

    datos = {
        "nombre_usuario": nombre,
        "actividad": objetivo,
        "objetivo_semanal": dias,
        "hecho": 0,
    }

    with open(ARCHIVO, "w") as archivo:
        json.dump(datos, archivo)

    print(f"Entonces deseas hacer {objetivo} {dias} veces a la semana.")
    return datos   


def cargar_data():
    try:
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None


def guardar_data(datos):
    with open(ARCHIVO, "w") as archivo:
        json.dump(datos, archivo)


hoy = date.today()

cargar = input("¿Deseas cargar tus datos anteriores? (si/no): ").lower()

if cargar == "si":
    datos = cargar_data()
    if datos is None:
        datos = escribir_data()
    else:
        print("ARCHIVO CARGADO CORRECTAMENTE\n")

elif cargar == "no":
    datos = escribir_data()

else:
    print("Entrada no válida.")
    exit()


nombre = datos["nombre_usuario"]
objetivo = datos["actividad"]

while True:
    respuesta = input(f"Hoy ({hoy}) hiciste {objetivo}? (si/no): ").lower()

    if respuesta == "si":
        print("¡Excelente!")
        datos["hecho"] += 1
        guardar_data(datos)
        break

    elif respuesta == "no":
        print("No te preocupes, mañana es un nuevo día para intentarlo.")
        break

    else:
        print("Respuesta no válida.")

print(
    f"Llevas {datos['hecho']} de {datos['objetivo_semanal']} "
    f"veces esta semana."
)
