
def comprobar_numero(entrada: str) -> bool :
    try:
        float(entrada)
    except ValueError:
        print("*Error*")
        return False
    return True



def main():
    entrada = input("Introduce un numero: ")
    if comprobar_numero(entrada) == True:
        print(f"es el numero {float(entrada)}")

if __name__=="__main__":
    main()