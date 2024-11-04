#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# Formula para calcular El capital tras un año.
#   amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 


def pedir_numero() -> int:
    amount = input("Dame una cantidad a invertir: ")
    while comprobar_numero(amount) == False:
        amount = input("Dame un numero valido: ")
    interest = input("\nDame el interes anual de la accion: ")
    while comprobar_numero(interest) == False:
        interest = input("Dame un numero valido: ")
    numero_años = input("\nDame el numero de años: ")
    while comprobar_numero(numero_años) == False:
        numero_años = input("Dame un numero valido: ")
    return (int(amount), int(interest), int(numero_años))



def comprobar_numero(numero) -> bool:
    try:
        float(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    return True


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    amount, interest, numero_años = pedir_numero()
    capital_año = (amount * (1 + interest / 100))

    print("\nCapital obtenido al final de cada año:")
    for año in range(1, numero_años + 1):
        print(f"\n{año} -> {capital_año:.2f}")
        capital_año = capital_año * (1 + interest / 100)
    print("")
        
        

        

if __name__=="__main__":
    main()

