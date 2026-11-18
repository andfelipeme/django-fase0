class Maquina:
    HORAS_MANTENIMIENTO = 200

    def __init__(self, nombre):
        self.nombre = nombre
        self.horas_uso = 0

    def usar(self, horas):
        self.horas_uso += horas

    def necesita_mantenimiento(self):
        return self.horas_uso >= self.HORAS_MANTENIMIENTO

    def __str__(self):
        return f"{self.nombre} - {self.horas_uso} h"


class Dron(Maquina):
    HORAS_MANTENIMIENTO = 50


# print(f"__name__ en maquinas.py: {__name__}")  # línea de demostración

if __name__ == "__main__":
    prueba = Dron("Prueba")
    prueba.usar(60)
    print(f"Prueba interna: {prueba}")
