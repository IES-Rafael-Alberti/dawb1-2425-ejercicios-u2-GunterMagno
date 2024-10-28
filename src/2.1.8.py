#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

#Nivel	            Puntuación
#Inaceptable	        0.0
#Aceptable	            0.4
#Meritorio	            0.6 o más

#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

def comprobar_puntuacion(numero):
    sueldo = 2400
    numero = float(numero)
    if numero == 0.0:
        total = sueldo * numero
        print(f"Tienes un nivel inaceptable, vas a recibir {total}$")
    elif numero == 0.4:
        total = sueldo * numero
        print(f"Tienes un nivel aceptable, vas a recibir {total}$") 
    elif numero >= 0.6:
        total = sueldo * numero
        print(f"Tienes un nivel meritorio, vas a recibir {total}$")
    else:
        print("Esta puntuacion es invalida, intenta de nuevo.")
        return False


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
    numero = input("Dame tu puntuacion: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    while comprobar_puntuacion(numero) == False:
        numero = input("Dame una puntuacion valida: ")
        comprobar_numero(numero)



if __name__=="__main__":
    main()