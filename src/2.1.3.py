#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

def pedir_numeros():
    numero1 = input("Dame un numero: ")
    numero2 = input("Dame otro y hare la división: ")
    return (numero1, numero2)


def comprobar_numero(numero1) -> bool:
    try:
        float(numero1)
        return True
    except ValueError:
        print("*Error* ingresa otro numero por favor.")
        return False


def division(numero1, numero2) -> float:
    numero1 = float(numero1)
    numero2 = float(numero2)
    try:
        resultado = numero1 / numero2
        print(f"El resultado es {resultado}")
    except ZeroDivisionError:
        print("El divisor no puede ser cero, intentalo de nuevo.")
        pedir_numeros()


def main():
    numero1, numero2 = pedir_numeros()
    while comprobar_numero(numero1) == False:
        numero1, numero2 = pedir_numeros()
    division(numero1, numero2)


if __name__=="__main__":
    main()