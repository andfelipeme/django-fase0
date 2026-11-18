class Filamento:
    def __init__(self, material, color, precio):
        self.material = material
        self.color = color
        self.precio = precio
        self.gramos = 1000

    def usar(self, gramos_uso):
        if gramos_uso > self.gramos:
            return f"No alcanza el filamento de {self.material} color {self.color}. Quedan disponibles {self.gramos}g"
        else:
            self.gramos -= gramos_uso
            return f"Hay {self.gramos} g de filamento de {self.material} color {self.color}"

    def queda_poco(self):
        return self.gramos < 100

    def costo_pieza(self, gramos_uso):
        costo = gramos_uso * self.precio / 1000
        return costo

    def recargar(self):
        self.gramos += 1000


pla_negro = Filamento("PLA", "Negro", 70000)
petg_blanco = Filamento("PETG", "Blanco", 85000)

print(pla_negro.usar(400))
print(pla_negro.usar(350))
print(pla_negro.usar(200))

print(pla_negro.queda_poco())
print(petg_blanco.queda_poco())

print(pla_negro.usar(80))

print(f"Quedan disponibles {pla_negro.gramos}g")

print(f"Esa pieza tiene un costo de ${pla_negro.costo_pieza(45)}")

pla_negro.recargar()

print(
    f"Cantidad de filamento {pla_negro.material} de color {pla_negro.color} disponible es de {pla_negro.gramos}g"
)
