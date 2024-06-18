from Gestion_de_proyectos import *
from Lista_Enlazada import *
from datetime import datetime


def main():
    id = 0
    gestor = {}

    while True:
        print("")
        print("Opciones:")
        print("(1) Ingresar datos.")
        print("(2) Modificar datos.")
        print("(3) Consultar datos.")
        print("(4) Eliminar datos.")
        print("(5) Listar datos.")
        print("(6) Salir.")
        print("")
        opcion = input("Indique la Opcion que desea de manera númerica: ")

        if opcion == "1":
            id += 1
            nombre = input("Ingrese el nombre del proyecto: ")
            descripcion = input("Ingrese la descripción del proyecto: ")
            fecha_inicio = input(
                "Ingrese la fecha de inicio del proyecto (dd/mm/yyyy): "
            )
            fecha_vencimiento = input(
                "Ingrese la fecha de vencimiento del proyecto (dd/mm/yyyy): "
            )
            estado_actual = input("Ingrese el estado actual del proyecto: ")
            empresa = input("Ingrese el nombre de la empresa del proyecto: ")
            gerente = input("Ingrese el nombre del gerente del proyecto: ")
            fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
            fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%d/%m/%Y")

            gestor[id] = {
                "nombre": nombre,
                "descripcion": descripcion,
                "fecha_inicio": fecha_inicio,
                "fecha_vencimiento": fecha_vencimiento,
                "estado_actual": estado_actual,
                "empresa": empresa,
                "gerente": gerente,
            }
            print("El proyecto a sido creado, su ID es " + str(id))

        elif opcion == "2":
            id_proyecto = int(input("Ingrese el ID del Proyecto que desea modificar: "))
            if id_proyecto in gestor:
                nombre = input("Ingrese el nuevo nombre del proyecto: ")
                descripcion = input("Ingrese la nueva descripcion del proyecto: ")
                fecha_inicio = input(
                    "Ingrese la nueva fecha de inicio del proyecto (dd/mm/yyyy): "
                )
                fecha_vencimiento = input(
                    "Ingrese la nueva fecha de vencimiento del proyecto (dd/mm/yyyy): "
                )
                estado_actual = input("Ingrese el nuevo estado actual del proyecto: ")
                empresa = input(
                    "Ingrese el nombre de la empresa que maneja el proyecto: "
                )
                gerente = input("Ingrese el nombre del nuevo gerente del proyecto: ")

                # Convertir fechas a objetos datetime
                fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
                fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%d/%m/%Y")

                # Actualizar datos en el diccionario
                gestor[id_proyecto] = {
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "fecha_inicio": fecha_inicio,
                    "fecha_vencimiento": fecha_vencimiento,
                    "estado_actual": estado_actual,
                    "empresa": empresa,
                    "gerente": gerente,
                }
            else:
                print("El ID del proyecto no existe")

        elif opcion == "3":
            id_proyecto = int(input("Ingrese el ID del proyecto que desea consultar: "))
            if id_proyecto in gestor:
                proyecto = gestor[id_proyecto]
                print(f"ID: {id_proyecto}")
                print(f"Nombre: {proyecto['nombre']}")
                print(f"Descripcion: {proyecto['descripcion']}")
                print(
                    f"Fecha de inicio: {proyecto['fecha_inicio'].strftime('%d/%m/%Y')}"
                )
                print(
                    f"Fecha de vencimiento: {proyecto['fecha_vencimiento'].strftime('%d/%m/%Y')}"
                )
                print(f"Estado actual: {proyecto['estado_actual']}")
                print(f"Empresa: {proyecto['empresa']}")
                print(f"Gerente: {proyecto['gerente']}")
            else:
                print("El ID del proyecto no existe")

        elif opcion == "4":
            id_proyecto = int(input("Ingrese el ID del Proyecto que desea eliminar: "))
            if id_proyecto in gestor:
                del gestor[id_proyecto]
                print(f"El proyecto con ID {id_proyecto} ha sido eliminado.")
            else:
                print("El ID del proyecto no existe")

        elif opcion == "5":
            if gestor:
                for id_proyecto, proyecto in gestor.items():
                    print(f"ID: {id_proyecto}     Nombre: {proyecto['nombre']}")
            else:
                print("No hay proyectos para listar.")

        elif opcion == "6":
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()
