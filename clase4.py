from taller.maquinas import Dron, Maquina

compresor = Maquina("Truper 24L")
dron = Dron("DJI Mini 3 Pro")

dron.usar(60)

print(compresor)
print(dron)
print(dron.necesita_mantenimiento())
