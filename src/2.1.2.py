
def pedir_y_comprobar(contraseña):
    contraseña_puesta = input("Introduce la contraseña: ").strip()
    while contraseña != contraseña_puesta:
        contraseña_puesta = input("Contraseña incorrecta, prueba de nuevo: ")
    return True

def main():
    contraseña = "aceituna"
    if pedir_y_comprobar(contraseña) == True:
        print("Contraseña correcta")


if __name__=="__main__":
    main()