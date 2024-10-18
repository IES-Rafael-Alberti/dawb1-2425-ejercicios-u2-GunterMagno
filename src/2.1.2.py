
def comprobar_contraseña(contraseña: str) -> bool:
    contraseña_puesta = input("Introduce la contraseña: ")
    if contraseña == contraseña_puesta:
        return True
    else:
        return False



def main():
    contraseña = "aceituna"
    if comprobar_contraseña(contraseña) == True:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

if __name__=="__main__":
    main()