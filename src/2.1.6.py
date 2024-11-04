#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def preg_nom() -> str:
    nombre = input("Dime tu nombre: ")
    while test_nom(nombre) == False:
        nombre = preg_nom()
    return nombre

def test_nom(nombre):
    try:
        str(nombre)
        nombre = str(nombre).strip().capitalize()
    except:
        print("Error, intentalo de nuevo")

def preg_gen():
    genero = input("Dime tu genero: ")
    test_gen(genero)
    while test_gen(genero) == False:
        genero = preg_gen()
    return genero

def test_gen(genero):
    try:
        str(genero)
        genero = str(genero).strip().lower()
    except:
        print("Sexno no valido. Ingresa hombre o mujer")

def determinar_grupo(nombre, genero):
    if genero == "mujer":
        if nombre[0] < 'M':
            print("Grupo A")
        else:
            print("Grupo B")
    elif genero == "hombre":
        if nombre[0] > "N":
            print("Grupo A")
        else:
            print("Grupo B")
    else:
        print("Sexno no valido. Ingresa hombre o mujer")
        genero = preg_gen()

def main():
    nombre = preg_nom()
    genero = preg_gen()
    determinar_grupo(nombre, genero)

if __name__=="__main__":
    main()