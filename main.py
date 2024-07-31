import registrar_users
import cargar


while True:
    print("Binevenido :)\n que quiere hacer\n1. registrarse\n2.iniciar seccion\n3.mirar usuarios\n4.eliminar usuarios\n5.salir")
    print("Ingrese una opcion: ")
    try:
        opc=int(input(""))
        if opc == 1 :
            print("Binevenido a resgistrar Usuario")
            registrar_users.regis()
        elif opc== 2:
            print("Bienvenido a iniciar seccion")
            cargar.cargar_user()
        elif opc== 3:
            print("Bienvenido a mirar usuarios")
        elif opc== 4:
            print("Bienvenido a eliminar ususarios")
        elif opc== 5:
            print("Saliendoooooo")
            break
        else:
            print("opcion no valida")
    except Exception:
        print("Ingrese una opcion validaa")