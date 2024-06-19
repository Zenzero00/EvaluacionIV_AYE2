from Pilas import *
from datetime import datetime


# Integrantes:
#     Francisco Unda V27963513
#     Santiago Pinto V30889670
#     Francisco Román
def main():
    gestor = {}
    id = 0
    id_tarea = 0
    pila_prioridades = Pila()
    cola_vencimiento = Cola()
    # Ciclo General
    while True:
        print("")
        print("Nota: No se pueden añadir tareas si no hay proyectos creados")
        print("y no se pueden crear subtareas si no hay tareas creadas")
        print("Menu Principal:")
        print("(1) Menú de Proyectos.")
        print("(2) Menú de Tareas.")
        print("(0) Salir.")
        print("")

        opcion = input("Indique la Opcion que desea de manera númerica: ")

        if opcion == "0":
            break

        elif opcion == "1":
            while True:
                print("")
                print("Menu de Proyectos:")
                print("(1) Ingresar Proyecto.")
                print("(2) Modificar Proyecto.")
                print("(3) Consultar Proyecto.")
                print("(4) Eliminar Proyecto.")
                print("(5) Listar Proyectos.")
                print("(0) Salir al Menu Principal.")
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
                    equipo = input("Ingrese el nombre del equipo del proyecto: ")
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
                        "equipo": equipo,
                    }

                    print("El proyecto a sido creado, su ID es " + str(id))

                elif opcion == "2":
                    id_proyecto = int(
                        input("Ingrese el ID del Proyecto que desea modificar: ")
                    )
                    if id_proyecto in gestor:
                        nombre = input("Ingrese el nuevo nombre del proyecto: ")
                        descripcion = input(
                            "Ingrese la nueva descripcion del proyecto: "
                        )
                        fecha_inicio = input(
                            "Ingrese la nueva fecha de inicio del proyecto (dd/mm/yyyy): "
                        )
                        fecha_vencimiento = input(
                            "Ingrese la nueva fecha de vencimiento del proyecto (dd/mm/yyyy): "
                        )
                        estado_actual = input(
                            "Ingrese el nuevo estado actual del proyecto: "
                        )
                        empresa = input(
                            "Ingrese el nombre de la empresa que maneja el proyecto: "
                        )
                        gerente = input(
                            "Ingrese el nombre del nuevo gerente del proyecto: "
                        )
                        equipo = input(
                            "Ingrese el nombre del nuevo equipo del proyecto: "
                        )

                        # Convertir fechas a objetos datetime
                        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
                        fecha_vencimiento = datetime.strptime(
                            fecha_vencimiento, "%d/%m/%Y"
                        )

                        # Actualizar datos en el diccionario
                        gestor[id_proyecto] = {
                            "nombre": nombre,
                            "descripcion": descripcion,
                            "fecha_inicio": fecha_inicio,
                            "fecha_vencimiento": fecha_vencimiento,
                            "estado_actual": estado_actual,
                            "empresa": empresa,
                            "gerente": gerente,
                            "equipo": equipo,
                        }
                    else:
                        print("El ID del proyecto no existe")

                elif opcion == "3":
                    id_proyecto = int(
                        input("Ingrese el ID del proyecto que desea consultar: ")
                    )
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
                        print(f"Equipo: {proyecto['equipo']}")
                    else:
                        print("El ID del proyecto no existe")

                elif opcion == "4":
                    id_proyecto = int(
                        input("Ingrese el ID del Proyecto que desea eliminar: ")
                    )
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

                elif opcion == "0":
                    break
                else:
                    print("Opcion no valida")

        elif opcion == "2":
            if id != 0:
                while True:
                    print("")
                    print("Menu de Tareas:")
                    print("(1) Añadir Tarea.")
                    print("(2) Actualizar Tarea.")
                    print("(3) Consultar Tarea.")
                    print("(4) Eliminar Tarea.")
                    print("(0) Salir al Menu Principal.")
                    print("")
                    opcion = input("Indique la Opcion que desea de manera númerica: ")

                    if opcion == "0":
                        break

                    elif opcion == "1":
                        print("Opciones para añadir Tareas.")
                        print("Nota para almacenar una tarea, necesita estar creada.")
                        print("(1) Añadir una Tarea nueva.")
                        print("(2) Almacenar una Tarea Prioritaria.")
                        print("(0) Salir al Menu de Tareas.")
                        print("")
                        opcion = input(
                            "Indique la Opcion que desea de manera númerica: "
                        )
                        if opcion == "1":
                            id_proyecto = int(
                                input(
                                    "Ingrese el ID del Proyecto al que desea agregarle una Tarea: "
                                )
                            )
                            if id_proyecto in gestor:
                                id_tarea += 1
                                nombre_tarea = input("Ingrese el nombre de la tarea: ")
                                empresa_tarea = input(
                                    "Ingrese el nombre de la empresa o cliente a la que va dirigida la Tarea: "
                                )
                                descripcion_tarea = input(
                                    "Ingrese la descripcion de la tarea: "
                                )
                                fecha_inicio_tarea = input(
                                    "Ingrese la fecha de inicio de la Tarea (dd/mm/yyyy): "
                                )
                                fecha_vencimiento_tarea = input(
                                    "Ingrese la fecha de vencimiento de la Tarea (dd/mm/yyyy): "
                                )
                                estado_tarea = input("Ingrese el estado de la tarea: ")
                                porcentaje_tarea = float(
                                    input(
                                        "Ingrese del 0 al 100 el porcentaje del progreso de la Tarea: "
                                    )
                                )
                                fecha_inicio_tarea = datetime.strptime(
                                    fecha_inicio_tarea, "%d/%m/%Y"
                                )
                                fecha_vencimiento_tarea = datetime.strptime(
                                    fecha_vencimiento_tarea, "%d/%m/%Y"
                                )
                                if "tareas" not in gestor[id_proyecto]:
                                    gestor[id_proyecto]["tareas"] = {}

                                gestor[id_proyecto]["tareas"][id_tarea] = {
                                    "id_proyecto": id_proyecto,
                                    "id_tarea": id_tarea,
                                    "nombre_tarea": nombre_tarea,
                                    "empresa_tarea": empresa_tarea,
                                    "descripcion_tarea": descripcion_tarea,
                                    "fecha_de_inicio_tarea": fecha_inicio_tarea,
                                    "fecha_de_vencimiento_tarea": fecha_vencimiento_tarea,
                                    "estado_tarea": estado_tarea,
                                    "porcentaje": porcentaje_tarea,
                                }
                                cola_vencimiento.agregar(
                                    gestor[id_proyecto]["tareas"][id_tarea]
                                )
                                print(
                                    "La Tarea a sido creada, su ID es " + str(id_tarea)
                                )
                            else:
                                print("El ID del Proyecto no existe")

                        elif opcion == "2":
                            id_proyecto = int(input("Ingrese el ID del Proyecto: "))
                            id_tarea_consulta = int(
                                input(
                                    "Ingrese el ID de la Tarea la cual desea priorizar: "
                                )
                            )
                            pila_prioridades.agregar(
                                gestor[id_proyecto]["tareas"][id_tarea_consulta]
                            )
                        elif opcion == "0":
                            pass
                        else:
                            print("Opcion no valida")
                    elif opcion == "2":
                        id_proyecto = int(input("Ingrese el ID del Proyecto: "))
                        id_tarea_consulta = int(
                            input(
                                "Ingrese el ID de la Tarea la cual desea actualizar: "
                            )
                        )
                        if id_proyecto in gestor:
                            nombre_tarea = input(
                                "Ingrese el nuevo nombre de la tarea: "
                            )
                            empresa_tarea = input(
                                "Ingrese el nuevo nombre de la empresa o cliente a la que va dirigida la Tarea: "
                            )
                            descripcion_tarea = input(
                                "Ingrese la nueva descripcion de la tarea: "
                            )
                            fecha_inicio_tarea = input(
                                "Ingrese la nueva fecha de inicio de la Tarea (dd/mm/yyyy): "
                            )
                            fecha_vencimiento_tarea = input(
                                "Ingrese la nueva fecha de vencimiento de la Tarea (dd/mm/yyyy): "
                            )
                            estado_tarea = input(
                                "Ingrese el nuevo estado de la tarea: "
                            )
                            porcentaje_tarea = float(
                                input(
                                    "Ingrese del 0 al 100 el nuevo porcentaje del progreso de la Tarea: "
                                )
                            )
                            fecha_inicio_tarea = datetime.strptime(
                                fecha_inicio_tarea, "%d/%m/%Y"
                            )
                            fecha_vencimiento_tarea = datetime.strptime(
                                fecha_vencimiento_tarea, "%d/%m/%Y"
                            )

                            gestor[id_proyecto]["tareas"][id_tarea_consulta] = {
                                "id_proyecto": id_proyecto,
                                "id_tarea": id_tarea_consulta,
                                "nombre_tarea": nombre_tarea,
                                "empresa_tarea": empresa_tarea,
                                "descripcion_tarea": descripcion_tarea,
                                "fecha_de_inicio_tarea": fecha_inicio_tarea,
                                "fecha_de_vencimiento_tarea": fecha_vencimiento_tarea,
                                "estado_tarea": estado_tarea,
                                "porcentaje": porcentaje_tarea,
                            }
                            print(
                                "La Tarea a sido actualizada, su ID es "
                                + str(id_tarea_consulta)
                            )
                        else:
                            print("El ID del Proyecto o de la Tarea no existe")

                    elif opcion == "3":
                        print("Opciones para consultar Tareas.")
                        print("(1) Consultar una Tarea Especifica.")
                        print("(2) Consultar la Tarea Prioritaria.")
                        print("(3) Consultar Tarea proxima a Vencer.")
                        print("(0) Salir al Menu de Tareas.")
                        print("")
                        opcion = input(
                            "Indique la Opcion que desea de manera númerica: "
                        )
                        if opcion == "1":
                            id_proyecto = int(input("Ingrese el ID del Proyecto: "))
                            id_tarea_consulta = int(
                                input("Ingrese el ID de la Tarea que desea consultar: ")
                            )
                            if (
                                id_proyecto in gestor
                                and "tareas" in gestor[id_proyecto]
                                and id_tarea_consulta in gestor[id_proyecto]["tareas"]
                            ):
                                tarea = gestor[id_proyecto]["tareas"][id_tarea_consulta]
                                print(f"ID del Proyecto: {id_proyecto}")
                                print(f"ID de la Tarea: {id_tarea_consulta}")
                                print(f"Nombre: {tarea['nombre_tarea']}")
                                print(f"Empresa/Cliente: {tarea['empresa_tarea']}")
                                print(f"Descripcion: {tarea['descripcion_tarea']}")
                                print(
                                    f"Fecha de inicio: {tarea['fecha_de_inicio_tarea'].strftime('%d/%m/%Y')}"
                                )
                                print(
                                    f"Fecha de vencimiento: {tarea['fecha_de_vencimiento_tarea'].strftime('%d/%m/%Y')}"
                                )
                                print(f"Estado actual: {tarea['estado_tarea']}")
                                print(f"Porcentaje: {tarea['porcentaje']}")
                            else:
                                print("El ID del Proyecto o de la Tarea no existe")
                        elif opcion == "2":
                            tarea_prioritaria = pila_prioridades.consultar_cima()
                            tiempo_total_prioridades = pila_prioridades.tiempo_total()
                            print(
                                f"ID del Proyecto: {tarea_prioritaria['id_proyecto']}"
                            )
                            print(f"ID de la Tarea: {tarea_prioritaria['id_tarea']}")
                            print(f"Nombre: {tarea_prioritaria['nombre_tarea']}")
                            print(
                                f"Empresa/Cliente: {tarea_prioritaria['empresa_tarea']}"
                            )
                            print(
                                f"Descripcion: {tarea_prioritaria['descripcion_tarea']}"
                            )
                            print(
                                f"Fecha de inicio: {tarea_prioritaria['fecha_de_inicio_tarea'].strftime('%d/%m/%Y')}"
                            )
                            print(
                                f"Fecha de vencimiento: {tarea_prioritaria['fecha_de_vencimiento_tarea'].strftime('%d/%m/%Y')}"
                            )
                            print(f"Estado actual: {tarea_prioritaria['estado_tarea']}")
                            print(f"Porcentaje: {tarea_prioritaria['porcentaje']}")
                            print(
                                f"Tiempo total de tareas prioritarias: {tiempo_total_prioridades}"
                            )
                        elif opcion == "3":
                            tarea_proxima_vencer = cola_vencimiento.consultar_frente()
                            tiempo_total_vencimientos = cola_vencimiento.tiempo_total()
                            print(
                                f"ID del Proyecto: {tarea_proxima_vencer['id_proyecto']}"
                            )
                            print(f"ID de la Tarea: {tarea_proxima_vencer['id_tarea']}")
                            print(f"Nombre: {tarea_proxima_vencer['nombre_tarea']}")
                            print(
                                f"Empresa/Cliente: {tarea_proxima_vencer['empresa_tarea']}"
                            )
                            print(
                                f"Descripcion: {tarea_proxima_vencer['descripcion_tarea']}"
                            )
                            print(
                                f"Fecha de inicio: {tarea_proxima_vencer['fecha_de_inicio_tarea'].strftime('%d/%m/%Y')}"
                            )
                            print(
                                f"Fecha de vencimiento: {tarea_proxima_vencer['fecha_de_vencimiento_tarea'].strftime('%d/%m/%Y')}"
                            )
                            print(
                                f"Estado actual: {tarea_proxima_vencer['estado_tarea']}"
                            )
                            print(f"Porcentaje: {tarea_proxima_vencer['porcentaje']}")
                            print(
                                f"Tiempo total de tareas próximas a vencer: {tiempo_total_vencimientos}"
                            )
                        elif opcion == "0":
                            pass
                        else:
                            print("Opción no válida")

                    elif opcion == "4":
                        print("Opciones para eliminar Tareas.")
                        print("(1) Eliminar una Tarea Especifica.")
                        print("(2) Eliminar la Tarea más Prioritaria.")
                        print("(3) Eliminar Tarea proxima a Vencer.")
                        print("(0) Salir al Menu de Tareas.")
                        print("")
                        opcion = input(
                            "Indique la Opcion que desea de manera númerica: "
                        )
                        if opcion == "1":
                            id_proyecto = int(input("Ingrese el ID del Proyecto: "))
                            id_tarea_eliminar = int(
                                input("Ingrese el ID de la Tarea que desea eliminar: ")
                            )
                            if (
                                id_proyecto in gestor
                                and "tareas" in gestor[id_proyecto]
                                and id_tarea_eliminar in gestor[id_proyecto]["tareas"]
                            ):
                                gestor[id_proyecto]["tareas"].pop(id_tarea_eliminar)
                                print(
                                    f"La tarea con ID {id_tarea_eliminar} ha sido eliminada."
                                )
                            else:
                                print(
                                    "El ID del Proyecto o de la Tarea no existe o ya fue eliminado."
                                )
                        elif opcion == "2":
                            pila_prioridades.eliminar()
                            print(
                                "La Tarea más prioritaria ha sido eliminada. \n Consulte si hay otra Tarea Prioritaria la cual tenga que realizar."
                            )
                        elif opcion == "3":
                            cola_vencimiento.eliminar()
                            print(
                                "La Tarea proxima a vencer ha sido eliminada. \n Consulte si hay otra Tarea proxima a vencer la cual tenga que realizar."
                            )
                        elif opcion == "0":
                            pass
                        else:
                            print("Opción no válida")
                    else:
                        print("Opcion no valida")
            else:
                print("Debe de Crear un Proyecto antes de crear una Tarea.")


if __name__ == "__main__":
    main()
