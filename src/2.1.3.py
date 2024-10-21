#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

def pedir_numeros():
    numero1 = input("Dame un numero: ")
    numero2 = input("Dame otro y hare la división: ")
    return (numero1, numero2)


def comprobar_numero(numero1, numero2):
    try:
        float(numero1)
        float(numero2)
    except ValueError:
        print("*Error* ingresa otro numero por favor.")
        return False
    return True


def division(numero1, numero2) -> float:
    numero1 = float(numero1)
    numero2 = float(numero2)
    if numero1 or numero2 == 0:
        raise ValueError ("*Error* ningun numero puede valer cero, ingresa otro numero por favor.")
    resultado = numero1 / numero2
    print(f"El resultado es {resultado}")



def main():
    numero1, numero2 = pedir_numeros()
    while comprobar_numero(numero1,numero2) == False:
        numero1, numero2 = pedir_numeros()
    division(numero1, numero2)

if __name__=="__main__":
    main()