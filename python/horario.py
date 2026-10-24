dia = str(input("Ingrese el día en minusculas sin espacios : "))
hora = int(input("Ingrese elmodulo en numeros primera = 1, segunda =2, tercera = 3, RECREO NO CUENTA : "))



if dia == "lunes":
    match hora:
        case 1:
            print ("Tienes programación (2h)")
        case 2:
            print ("Tienes programación (1h)")
        case 3:
            print ("Tienes lenguaje de marcas")
        case 4:
            print ("Tienes sistemas informáticos (3h)")
        case 5:
            print ("Tienes sistemas informáticos (2h)")
        case 6:
            print ("Tienes sistemas informáticos (1h)")

if dia == "martes":
    match hora:
        case 1:
            print ("Tienes sistemas informáticos (2h)")
        case 2:
            print ("Tienes sistemas informáticos (1h)")
        case 3:
            print ("Tienes entorno de desarrollo")
        case 4:
            print ("Tienes Base de datos (3h)")
        case 5:
            print ("Tienes Base de datos (2h)")
        case 6:
            print ("Tienes Base de datos (1h)")
            
if dia == "miercoles":
    match hora:
        case 1:
            print ("Tienes Base de datos (3h)")
        case 2:
            print ("Tienes Base de datos (2h)")
        case 3:
            print ("Tienes Base de datos (1h)")
        case 4:
            print ("Tienes itinerario personal para la empleabilidad")
        case 5:
            print ("Tienes lenguaje de marcas")
        case 6:
            print ("Tienes digitalización")
                     
if dia == "jueves":
    match hora:
        case 1:
            print ("Tienes lenguaje de marcas")
        case 2:
            print ("Tienes programación (4h)")
        case 3:
            print ("Tienes programación (3h)")
        case 4:
            print ("Tienes programación (2h)")
        case 5:
            print ("Tienes programación (1h)")
        case 6:
            print ("Tienes itinerario personal para la empleabilidad")

if dia == "viernes":
    match hora:
        case 1:
            print ("Tienes programación (2h)")
        case 2:
            print ("Tienes programación (1h)")
        case 3:
            print ("Tienes entorno de desarrollo (2h)")
        case 4:
            print ("Tienes entorno de desarrollo (1h)")
        case 5:
            print ("Tienes sostenibilidad")
        case 6:
            print ("Tienes itinerario personal para la empleabilidad")