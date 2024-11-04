#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


def salir(numero :int):
    if numero == "-1":
        return True
    else:
        return False


def par(numero :int, contador :int) -> int :
    numero = int(numero)
    if numero % 2 == 0:
        contador += 1
        return contador
    elif numero % 2 == 1:
        return contador


def comprobar_negativo(numero:str) -> str:
    if numero.startswith("-"):
        if numero == "-1":
            salir(numero)
            return True
        else:
            print("El numero es negativo intenta de nuevo: ")  
            return False
    else:
        return True
  


def comprobar_numero(numero) -> bool:
    try:
        int(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    if comprobar_negativo(numero) == False:
        return False
    return True


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    numero1 = 0
    numero = 0
    contador = 0

    numero = input("Dame un numero entero positivo: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    contador = par(numero, contador)

    numero1 = input("Dame otro numero entero positivo: ")
    while comprobar_numero(numero1) == False:
        numero1 = input("Dame otro numero valido: ")
    contador = par(numero1, contador)


    while salir(numero) == False or salir(numero1 == False):
        numero = int(numero)
        numero1 = int(numero1)
        suma = numero + numero1
        print(f"\nLa suma de los numero {numero} y {numero1} es {suma}\n")
        numero = input("Dame un numero entero positivo: ")
        while comprobar_numero(numero) == False:
            numero = input("Dame un numero valido: ")
        contador = par(numero, contador)

        numero1 = input("Dame otro numero entero positivo: ")
        while comprobar_numero(numero1) == False:
            numero1 = input("Dame otro numero valido: ")
        contador = par(numero1, contador)
        
    print(f"\nSe han introducido {contador} numeros pares.\n")
        


if __name__=="__main__":
    main()



