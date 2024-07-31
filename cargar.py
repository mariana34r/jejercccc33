import json
ruta = "users.json"

def guarda_user(datos):
        with open(ruta, "w") as file:
            json.dump(datos,file, indent=4)
        print("Datos guardados exitosamente!!")
        print("**************************************************")


def cargar_user():
    try:
        with open(ruta, "r") as leer:
            datos=json.load(leer)
            return datos
    except FileNotFoundError:
        print("Error al guardar datos")
        print("**************************************************")
        return {"users" : {}}