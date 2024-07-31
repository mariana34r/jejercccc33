import registrar_users
import cargar
import edit_users
import mostrar_user


while True:
    print("Binevenido :)\n que quiere hacer\n1. registrarse\n2.iniciar seccion\n3.mirar usuarios\n4.eliminar usuarios\n5.Editar Usuario\n6.Editar Usuario")
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
            mostrar_user.mostrar()
        elif opc== 4:
            print("Bienvenido a eliminar ususarios")
        elif opc== 5:
            print("Bienvenido a editar ususarios")
            edit_users.edit_users()
        elif opc== 6:
            print("Saliendoooooo")
            break
        else:
            print("opcion no valida")
    except Exception:
        print("Ingrese una opcion validaa")