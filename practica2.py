class Filamento:
    PESO_ROLLO = 1000
    LIMITE_ROLLO = 100
    rollos_creados = 0

    def __init__(self, material, color, precio):
        self.material = material
        self.color = color
        self.precio = precio
        self.gramos = self.PESO_ROLLO
        Filamento.rollos_creados += 1

    def usar(self, gramos_uso):
        if gramos_uso > self.gramos:
            return f"No alcanza el filamento de {self.material} color {self.color}. Quedan disponibles {self.gramos}g"
        else:
            self.gramos -= gramos_uso
            return f"Hay {self.gramos} g de filamento de {self.material} color {self.color}"

    def queda_poco(self):
        return self.gramos < self.LIMITE_ROLLO

    def costo_pieza(self, gramos_uso):
        costo = gramos_uso * self.precio / self.PESO_ROLLO
        return costo

    def recargar(self):
        self.gramos += self.PESO_ROLLO

    def __str__(self):
        return f"{self.material} {self.color} - {self.gramos} g"


pla_negro = Filamento("PLA", "Negro", 70000)
petg_blanco = Filamento("PETG", "Blanco", 85000)

print(pla_negro)
print(pla_negro.usar(400))
print(pla_negro)

print(Filamento.rollos_creados)

tpu_rojo = Filamento("TPU", "Rojo", 95000)

print(Filamento.rollos_creados)

print(pla_negro.queda_poco())
print(petg_blanco.queda_poco())

pla_negro.recargar()
print(pla_negro)
