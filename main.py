def quick_sort(lista, clave):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[clave] < pivote[clave]]
        iguales = [x for x in lista if x[clave] == pivote[clave]]
        mayores = [x for x in lista[1:] if x[clave] > pivote[clave]]
        return quick_sort(menores, clave) + iguales + quick_sort(mayores, clave)


participantes = {}

def agregar():

    cantidad = int(input("¿Cuántos participantes desea ingresar? "))
    for i in range(cantidad):
        print(f"\nParticipante #{i+1}:")
        dorsal = input("Numero de dorsal: ")
        nombre = input("Nombre completo: ")
        edad = int(input("Edad: "))
        categoria = input("Categoría (Joven, Adulto, viejito): ")

        participantes[dorsal] = {
            "nombre": nombre,
            "edad": edad,
            "categoria": categoria
        }

    print("\nRegistro completado. Participantes ingresados:")

def ordenarPorNombre():
    if not participantes:
        print("No hay participantes registrados.")
        return

    lista_participantes = []

    for dorsal, datos in participantes.items():
        participante = {"dorsal": dorsal}
        participante.update(datos)
        lista_participantes.append(participante)

    ordenados = quick_sort(lista_participantes, "nombre")

    print("\nParticipantes ordenados por nombre:")
    for p in ordenados:
        print(f"- {p['nombre']} (Dorsal {p['dorsal']}, Edad {p['edad']}, Categoría: {p['categoria']})")

def Menu():
    opcion = 0

    while opcion != 4:
        print("\n-_M E N U_-")
        print("1. Agregar participante")
        print("2. Mostrar participantes ordenados por nombre")
        print("3. Mostrar participantes ordenados por edad")
        print("4. Salir")

        opcion_input = input("\nIngrese su opción: ")
        if opcion_input.isdigit():

            opcion = int(opcion_input)
            if opcion == 1:
                agregar()
            elif opcion == 2:
                ordenarPorNombre()
            else:
                print("\nOpción inválida, vuelva a intentar")
        else:
            print("\nError: ingreso de datos no numéricos")
            opcion = 0

        if opcion != 4:
            input("\nPresione ENTER para continuar...")

Menu()