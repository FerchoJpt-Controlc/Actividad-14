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
                print()
            else:
                print("\nOpción inválida, vuelva a intentar")
        else:
            print("\nError: ingreso de datos no numéricos")
            opcion = 0

        if opcion != 4:
            input("\nPresione ENTER para continuar...")
