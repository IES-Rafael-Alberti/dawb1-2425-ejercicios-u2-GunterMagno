#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def pedir_numero() -> int:
    numero = input("Dame un numero y te digo si es par o impar: ")
    while comprobar_numero(numero) == False:
        numero = pedir_numero()
    return (int(numero))


def comprobar_numero(numero) -> int:
    try:
        int(numero)
        return True
    except ValueError:
        print("*Error* ingresa otro numero por favor.")
        return False
    

def par(numero) :
    if numero % 2 == 0:
        return True
    elif numero % 2 == 1:
        return False

def main():
    numero = pedir_numero()
    if par(numero) == True:
        print(f"El numero {numero} es par.")
    else:
        print(f"El numero {numero} es impar")

if __name__=="__main__":
    main()