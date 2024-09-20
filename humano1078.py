print("Actividad 9 clase humano")
print("Leysi Mejia Mat: 22308051281078")
print("")

# Zona de clases

class Humano1078:
    # Zona de atributos dentro de la clase
    edad=0
    genero=0
    peso=0
    estatura=0
    pelo=0
    ojos=0

    # Zona de funciones dentro de la clase
    def correr1078(self,n):
        print(f"{n} esta corriendo...")

    def caminar1078(self,n):
        print(f"{n} esta caminando...")

    def cantar1078(self,n):
        print(f"{n} esta cantando...")

    def comer1078(self,n):
        print(f"{n} esta comiendo...")

    def dormir1078(self,n):
        print(f"{n} esta durmiendo...")

# Zona de creacion de objetos
leysi=Humano1078()
marcos=Humano1078()

# Zona de usando objetos
print("  Resultados para Leysi")
leysi.edad=18
print(f"Edad: {leysi.edad}")
leysi.genero="Femenino"
print(f"Genero: {leysi.genero}")
leysi.peso=50
print(f"Peso: {leysi.peso} kg")
leysi.estatura=1.59
print(f"Estatura: {leysi.estatura} m")
leysi.ojos="Cafe"
print(f"Ojos: {leysi.ojos}")

print("")

leysi.correr1078("Leysi")
leysi.caminar1078("Leysi")
leysi.dormir1078("Leysi")

print("-------------------------------------")

print("  Resultados para Marcos")
marcos.edad=16
print(f"Edad: {marcos.edad}")
marcos.genero="Masculino"
print(f"Genero: {marcos.genero}")
marcos.peso=70
print(f"Peso: {marcos.peso} kg")
marcos.estatura=1.85
print(f"Estatura: {marcos.estatura} m")
marcos.ojos="Azul"
print(f"Ojos: {marcos.ojos}")
marcos.pelo="Negro"
print(f"Color de pelo: {marcos.pelo}")

print("")

marcos.correr1078("Marcos")
marcos.caminar1078("Marcos")
marcos.dormir1078("Marcos")
marcos.cantar1078("Marcos")
marcos.comer1078("Marcos")