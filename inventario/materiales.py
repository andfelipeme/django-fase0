class Material:
    UNIDAD = "unidades"
    LIMITE_POCO = 100

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def usar(self, cantidad_uso):
        if cantidad_uso > self.cantidad:
            return f"No alcanza: {self.cantidad}{self.UNIDAD} de {self.nombre}"
        else:
            self.cantidad -= cantidad_uso

    def queda_poco(self):
        return self.cantidad < self.LIMITE_POCO

    def __str__(self):
        return f"{self.nombre} - {self.cantidad}{self.UNIDAD}"


class Filamento(Material):
    UNIDAD = "g"

    def __init__(self, nombre, cantidad, color):
        super().__init__(nombre, cantidad)
        self.color = color

    def __str__(self):
        return f"{super().__str__()} ({self.color})"


class Resina(Material):
    UNIDAD = "ml"
    LIMITE_POCO = 200


class Tornillo(Material):
    pass


if __name__ == "__main__":
    tornillo = Tornillo("Tornillo M3 5mm", 500)
    print(tornillo)
