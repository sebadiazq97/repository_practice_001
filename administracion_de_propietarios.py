# funciones requeridas
# - consultar propietarios
# - actualizar informacion
# - agregar nuevos departamentos
# - eliminar registros
# - mostrar datos almacen

piso1 = {
    "101":"Juan Vélez",
    "102":"María Soto"
}

piso2 = {
    "201":"Pedro Rojas",
    "102":"Ana Díaz"
}

piso3 = {
    "301":"Carlos Pérez",
    "302":"Claudia Torres"
}

piso4 = {
    "401":"José González",
    "402":"Camila Muñoz"
}


def menu():
    while True:

        print ("=======================================")
        print("SISTEMA DE ADMINISTRACION DE PROPIETARIOS")
        print ("=======================================")
        print("")
        print("1.Consultar Propietarios")
        print("2.Actualizar Informacion")
        print("3.Agregar Nuevos Departamentos")
        print("4.Eliminar Registros")
        print("5.Mostrar Datos Almacenados")
        print("6.Salir")


        while True:
            try:
                opcion = int(input("Ingrese opción: "))
                if opcion >= 1 and opcion <= 6:
                    break
                else:
                    print("ERROR: Debe ingresar un número entre 1 y 6")
                    print("")
            except:
                print("ERROR: Debe ingresar una de las opciones disponibles.")
                print("")
    
        if opcion == 6:
            print("Programa Finalizado")
            print ("Que tenga un buen dia....")
            break
menu()






print ( piso1)

