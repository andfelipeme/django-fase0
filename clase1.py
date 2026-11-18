class Impresora:
    def __init__(self, nombre, tipo):
        self.nombre = nombre  # dato que se pasa al crearla
        self.tipo = tipo  # dato que se pasa al crearla
        self.horas_uso = 0  # dato que arranca con un valor fijo

    def imprimir(self, horas):
        self.horas_uso += horas  # modifica el dato del objeto
        print(f"{self.nombre} imprimio {horas} h. Total: {self.horas_uso} h.")

    def necesita_mantenimiento(self):
        return self.horas_uso >= 200  # devuelve un valor Boolean


principal = Impresora("A1 Mini", "FDM")
secundaria = Impresora("Ender 3 V3 KE", "FDM")

print(principal.nombre)
print(secundaria.tipo)

principal.imprimir(120)
principal.imprimir(90)
secundaria.imprimir(15)

print(principal.necesita_mantenimiento())
print(secundaria.necesita_mantenimiento())
