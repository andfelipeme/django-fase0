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
        return f"{self.nombre} - {self.cantidad} {self.UNIDAD}"


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


pla_negro = Filamento("PLA", 1000, "Negro")
resina = Resina("Resina estándar", 1000)
tornillos = Tornillo("Tornillo M3", 500)

print(pla_negro)
print(resina)
print(tornillos)

pla_negro.usar(950)
resina.usar(850)
tornillos.usar(350)

print(pla_negro.queda_poco())
print(resina.queda_poco())
print(tornillos.queda_poco())

print(pla_negro.usar(80))

print(pla_negro)
print(resina)
print(tornillos)
