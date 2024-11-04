#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.


import math


def primo(numero):
  if numero < 2:
       return False
  else:
      for i in range(2,int(math.sqrt(numero))):  #### ARREGLARRRRRRRRRRRRRRRRRRRRRRRRRRRR###############
          if numero % i == 0:
              return False
          return True


def comprobar_numero(numero) -> bool:
    try:
        int(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    return True


def pedir_numero():
    numero = input("Dame un numero entero: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    return int(numero)


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    numero = pedir_numero()
    if primo(numero) == False:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

if __name__ == "__main__":
    main()