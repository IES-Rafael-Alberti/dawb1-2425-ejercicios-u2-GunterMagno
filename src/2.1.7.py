#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

 #   Renta	                         Tipo impositivo
 #   Menos de 10000€	                   5%
 #   Entre 10000€ y 20000€	               15%
 #   Entre 20000€ y 35000€	               20%
 #   Entre 35000€ y 60000€	               30%
 #   Más de 60000€	                       45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.


def renta(numero):
    numero = float(numero)
    if numero < 10000:
        print("Te corresponde un 5% de impositivo")
    elif numero >= 10000 and numero < 20000:
        print("Te corresponde un 15% de impositivo")
    elif numero >= 20000 and numero < 35000:
        print("Te corresponde un 20% de impositivo")
    elif numero >= 35000 and numero < 60000:
        print("Te corresponde un 30% de impositivo")
    elif numero >= 60000:
        print("Te corresponde un 45% de impositivo")


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
    numero = input("Dame un tus ingresos: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    renta(numero)


if __name__=="__main__":
    main()
