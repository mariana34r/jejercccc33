import cargar as gg

def mostrar():
    data = gg.cargar_user()
    docu = int(input("Digite su documento: "))
    if str(docu) in data["users"]:
        print("El usuario", data["users"][str(docu)]["Nombre"],data["users"][str(docu)]["Apellido"], "con el documento", str(docu), "con la edad", data["users"][str(docu)]["Edad"] )
        
