
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1


def comprobar_numero(numero) -> bool:
    try:
        int(numero)
    except ValueError:
        print("*Error*, intenta de nuevo")
        return False
    return True


def comprobar_negativo(numero:str) -> bool:
    if numero.startswith("-"):
        print("El numero es negativo intenta de nuevo: ")
        return False
    

def par(numero) -> bool :
    if numero % 2 == 0:
        return True
    elif numero % 2 == 1:
        return False


def triangulo(numero :int):
    cadena = ""
    triangulo = ""
    if par(numero) == True:
        inicio = 0
    else:
        inicio = 1
    for i in range(inicio, numero + 1, 2):
        cadena = str(i) + " " + cadena
        triangulo = triangulo + cadena + "\n"
    print(triangulo)


def main():
    numero = input("Dame un numero entero: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero entero: ")
    while  comprobar_negativo(numero) == False:
        numero = input("Dame un numero entero: ")
    numero = int(numero)
    triangulo(numero)
    


if __name__=="__main__":
    main()