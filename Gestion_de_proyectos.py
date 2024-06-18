from Pilas import *
from datetime import datetime


class Proyecto:
    def __init__(
        self,
        id,
        nombre,
        descripcion,
        fecha_de_inicio,
        fecha_de_vencimiento,
        estado_actual,
        empresa,
        gerente,
        equipo,
    ):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_de_inicio = fecha_de_inicio
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.estado_actual = estado_actual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tarea = []
        self.pila_prioridades = []
        self.cola_vencimientos = []

    def agregar_tarea(self, tarea):
        self.tarea.append(tarea)

    def agregar_pila(self, pila_prioridades):
        self.pila_prioridades.append(pila_prioridades)

    def agregar_prioridad(self, tarea_prioritaria):
        if not isinstance(self.pila_prioridades, Pila):
            self.pila_prioridades = Pila()  # Inicializa la pila si aún no existe
        self.pila_prioridades.apilar(tarea_prioritaria)
        print(f"Tarea prioritaria '{tarea_prioritaria.nombre}' agregada.")

    def agregar_cola(self, cola_vencimientos):
        self.cola_vencimientos.append(cola_vencimientos)


class Tarea:
    def __init__(
        self,
        id,
        nombre,
        empresa_cliente,
        descripcion,
        fecha_inicio,
        fecha_vencimiento,
        estado,
        porcentaje,
    ):
        self.id = id
        self.nombre = nombre
        self.empresa_cliente = empresa_cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
        self.porcentaje = porcentaje
        self.subtareas = []


class Subtarea:
    def __init__(self, id, nombre, descripcion, estado):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
