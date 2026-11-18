from inventario.materiales import Filamento, Resina, Tornillo

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
