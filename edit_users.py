import cargar as gg
def menu():
    menu  = ["1. Para nombre", "2. Para apellido", "3.Para edad", "4. Para salir"]
    for n in menu:
        print(n)

def edit_users():
    while True:
        data = gg.cargar_user()
        docu = int(input("Ingrese su documento, si quieres salir presiona 0: "))
        if docu == 0:
            print("Saliendo...")
            break
        elif str(docu) in data["users"]:
            while True:
                menu()
                op = int(input("Seleccione una opccion: "))
                if op == 1:
                    nuevo = str(input("Digite sus nuevos nombres: "))
                    data["users"][str(docu)]["Nombre"] = nuevo
                    gg.guarda_user(data)
                elif op ==2:
                    nuevo = str(input("Digite sus nuevos Apellidos: "))
                    data["users"][str(docu)]["Apellido"] = nuevo
                    gg.guarda_user(data)
                elif op == 3:
                    nuevo = int(input("Digite su nueva edad: "))
                    data["users"][str(docu)]["Edad"] = nuevo
                    gg.guarda_user(data)
                elif op == 4:
                    print("Saliendo...")
                    break
        else:
            print("Este documento no esta registrado")
            
