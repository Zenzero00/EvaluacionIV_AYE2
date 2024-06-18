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
