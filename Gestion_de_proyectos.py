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

    def agregar_tarea(self, tarea):
        self.tarea.append(tarea)


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
