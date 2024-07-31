import cargar as gg
def star():
    data = gg.cargar_user()
    docu = int(input("Ingrese su documento: "))
    if str(docu) in data["users"]:
        print("Bienvenido", data["users"][str(docu)]["Nombre"])

