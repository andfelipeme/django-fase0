# ---------- Clase padre ----------
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
        return f"{self.nombre} - {self.horas_uso} horas de uso"


# ---------- 1, Herencia simple: hereda TODO ----------
class Compresor(Maquina):
    pass


# ---------- 2, Sobreescribir un atributo de clase ----------
class Dron(Maquina):
    HORAS_MANTENIMIENTO = 50


# ---------- 3, super(): agregar datos propios y extender un método ----------
class Impresora3D(Maquina):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)  # Maquina pone nombre y horas_uso
        self.tipo = tipo  # dato propio de la impresora

    def __str__(self):
        return f"{super().__str__()} ({self.tipo})"


compresor = Compresor("Truper 24L")
dron = Dron("DJI Pro Mini 3")
impresora = Impresora3D("A1 Mini", "FDM")

compresor.usar(120)
dron.usar(60)
impresora.usar(210)

print(compresor)
print(dron)
print(impresora)

print(compresor.necesita_mantenimiento())
print(dron.necesita_mantenimiento())
print(impresora.necesita_mantenimiento())
