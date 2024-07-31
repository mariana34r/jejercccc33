import cargar as gg
def regis ():
    data = gg.cargar_user()
    while True:
        try:
            docu = int(input("DIgite su documento :"))
            break
        except Exception:
            print("Ingrese un numero validoo")

    if str(docu) in data["users"]:
            print("Ya hay un usuario registrado con ese documento")


    else:
        datos = {}
        datos["Nombre"] = str(input("Digite su nombre: "))
        datos["Apellido"] = str(input("Digite su apellido: "))
        while True:
            try:
                datos["Edad"] = int(input("Ingrese su edad: "))
                break
            except Exception:
                print("Ingrese una edad valida")

    data["users"][docu]=datos
    gg.guarda_user(data)


