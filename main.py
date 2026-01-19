# EN PROCESO, AUN HAY ERRORES
from datetime import date

hoy = date.today()

nombre = input("Ingrese su nombre: ")
objetivo = input("¿En que actividad deseas avanzar?: ")

while True:
    try:
        dias = int(input(f"Bien, {nombre} ¿cuál es tu objetivo semanal?: "))
        break
    except ValueError:
        print("Por favor ingresa un número válido.")

datos = {
    "nombre_usuario": nombre,
    "actividad": objetivo,
    "objetivo_semanal": dias,
    "hecho": 0,
}

print(f"Entonces deseas hacer {objetivo} {dias} veces a la semana.")

while True:
    respuesta = input(f"Hoy ({hoy}) hiciste {objetivo}? (si/no): ")

    if respuesta.lower() == "si":
        print("¡Excelente!")
        datos["hecho"] += 1
        break
    elif respuesta.lower() == "no":
        print("No te preocupes, mañana es un nuevo día para intentarlo.")
        break
    else:
        print("Respuesta no válida. Por favor responde con si o no.")

print(
    f"Llevas {datos['hecho']} de {datos['objetivo_semanal']} "
    f"veces esta semana."
)
