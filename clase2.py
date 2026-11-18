class Impresora:
    HORAS_MANTENIMIENTO = 200  # atributo de clase: igual para todas
    total = 0  # atributo de clase: contador compartido

    def __init__(self, nombre, tipo):
        self.nombre = nombre  # atributo de instancia: propios de cada una
        self.tipo = tipo
        self.horas_uso = 0
        Impresora.total += 1  # se modifica a través de la CLASE

    def imprimir(self, horas):
        self.horas_uso += horas

    def necesita_mantenimiento(self):
        return self.horas_uso >= self.HORAS_MANTENIMIENTO

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.horas_uso} h."


principal = Impresora("A1 Mini", "FDM")
secundaria = Impresora("Ender 3 V3 KE", "FDM")

principal.imprimir(210)

print(principal)
print(secundaria)
print(f"Impresora: {principal}")

print(Impresora.total)
print(principal.HORAS_MANTENIMIENTO)
print(principal.necesita_mantenimiento())
