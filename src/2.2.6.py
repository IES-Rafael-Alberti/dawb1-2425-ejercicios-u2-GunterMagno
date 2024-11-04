#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

#*
#**
#***
#****
#*****



def dibujar_triangulo(numero):
     for i in range(1, numero + 1):
            print('*' * i)


def pedir_numero():
    numero = input("Dame un numero entero: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    return int(numero)

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
    numero = pedir_numero()
    dibujar_triangulo(numero)


if __name__=="__main__":
    main()
