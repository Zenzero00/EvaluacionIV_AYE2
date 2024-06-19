from datetime import datetime


class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def agregar(self, tarea):
        self.elementos.append(tarea)

    def eliminar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def consultar_cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]

    def tiempo_total(self):
        hoy = datetime.now()
        total_dias = 0
        for tarea in self.elementos:
            if "fecha_de_vencimiento_tarea" in tarea:
                dias_restantes = (tarea["fecha_de_vencimiento_tarea"] - hoy).days
                total_dias += max(dias_restantes, 0)
        return total_dias


class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def agregar(self, tarea):
        if isinstance(tarea["fecha_de_vencimiento_tarea"], str):
            tarea["fecha_de_vencimiento_tarea"] = datetime.strptime(
                tarea["fecha_de_vencimiento_tarea"], "%d/%m/%Y"
            )
        elif not isinstance(tarea["fecha_de_vencimiento_tarea"], datetime):
            raise ValueError(
                "La fecha de vencimiento debe ser una cadena de texto o un objeto datetime"
            )

        self.elementos.append(tarea)
        self.elementos.sort(key=lambda x: x["fecha_de_vencimiento_tarea"])

    def eliminar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def consultar_frente(self):
        if not self.esta_vacia():
            return self.elementos[-1]

    def tiempo_total(self):
        hoy = datetime.now()
        total_dias = 0
        for tarea in self.elementos:
            if "fecha_de_vencimiento_tarea" in tarea:
                dias_restantes = (tarea["fecha_de_vencimiento_tarea"] - hoy).days
                total_dias += max(dias_restantes, 0)
        return total_dias
