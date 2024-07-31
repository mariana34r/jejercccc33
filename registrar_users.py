import cargar as gg
def regis ():
    data = gg.cargar_user()
    docu = int(input("DIgite su documento :"))
    if str(docu) in data["users"]:
        print("Ya hay un usuario registrado con ese documento")
    else:
        datos = {}
        datos["Nombre"] = str(input("Digite su nombre: "))
        datos["Apellido"] = str(input("Digite su apellido: "))
        datos["Edad"] = int(input("Ingrese su edad: "))
        data["users"][docu]=datos
        gg.guarda_user(data)


