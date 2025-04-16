class Inventario:
    def __init__(self, capacidad=5):
        self.objetos = []
        self.capacidad = capacidad

    def agregar_objeto(self, objeto):
        for o in self.objetos:
            if o.nombre == objeto.nombre:
                o.cantidad += 1
                return True

        if len(self.objetos) < self.capacidad:
            self.objetos.append(objeto)
            return True
        return False

    def eliminar_objeto(self, nombre):
        for o in self.objetos:
            if o.nombre == nombre:
                if o.cantidad > 1:
                    o.cantidad -= 1
                else:
                    self.objetos.remove(o)
                return True
        return False

    def esta_lleno(self):
        return len(self.objetos) >= self.capacidad

    def esta_vacio(self):
        return len(self.objetos) == 0
