#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def precio(edad:int):
    if edad <= 4:
        print(f"La entrada es gratis, ya que tiene {edad} años.")
    elif edad > 4 and edad <= 18:
        print(f"La entrada son 5$, ya que tiene {edad} años.")
    elif edad > 18:
        print(f"La entrada son 10$, ya que tiene {edad} años.")
    else:
        print("ERROR")


def comprobar_edad(edad) -> int:
    try:
        int(edad)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    edad = int(edad)
    if edad < 0:
        print("La edad no puede ser negativa!!")
        return False
    elif edad > 100:
        print("La edad no puede ser mayor que cien!!")
        return False
    elif edad == 0:
        print("La edad no puede ser cero!!")
        return False
    else:
        return True


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    edad = input("Dime tu edad: ")
    while comprobar_edad(edad) == False:
        edad = input("Dame una edad valida: ")
    edad = int(edad)
    precio(edad)


if __name__=="__main__":
    main()