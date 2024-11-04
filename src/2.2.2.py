#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


def comprobar_numero(numero) -> bool:
    try:
        int(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    return True


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    edad = input("Dime tu edad: ")
    while comprobar_numero(edad) == False:
        edad = input("Dame un numero valido: ")
    edad = int(edad)
    for i in range (1, edad+1):
        print(f"Has cumplido -> {i}")


if __name__=="__main__":
    main()

