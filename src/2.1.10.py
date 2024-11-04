#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


def elegir_ingrediente(ingredientes):
    try:
        eleccion = str(input("Elige ingrediente: ")).capitalize
    except:
        print("Mal")
    if eleccion 



def comprobar_(tipo_pizza) -> bool:
    try:
        str(tipo_pizza)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    if tipo_pizza == "si":
        return 1
    elif tipo_pizza == "no":
        return 2
    else:
        return False


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    ingredientes_vegetarianos = ["Pimiento", "Tofu"]
    ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]
    ingredientes_pizza = ["Mozzarella", "Tomate"]
    tipo_pizza = input("Quieres una pizza vegetariana? (si / no): ").strip().lower()
    while comprobar_(tipo_pizza) == False:
        tipo_pizza = input("Quieres una pizza vegetariana? (si / no): ").strip().lower()
    if comprobar_(tipo_pizza) == 1:
        print("\nIngredientes disponibles para una pizza vegetariana:\n")
        for i in ingredientes_vegetarianos:
            print(f"-> {i}")
        print("\n")
        elegir_ingrediente(ingredientes_vegetarianos)
    elif comprobar_(tipo_pizza) == 2:
        print("\nIngredientes para una pizza no vegetariana:\n")
        for i in ingredientes_no_vegetarianos:
            print(f"-> {i}")
        print("\n")
        elegir_ingrediente(ingredientes_no_vegetarianos)

if __name__=="__main__":
    main()
