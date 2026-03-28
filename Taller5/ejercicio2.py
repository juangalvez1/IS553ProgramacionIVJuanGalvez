class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada} cc"


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f", Carga: {self.carga}kg"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.velocidad} km/h, Cilindrada: {self.cilindrada}cc"
    
def catalogar(vehiculos, ruedas = None):
    contador = 0

    for v in vehiculos:
        if ruedas is None or v.ruedas == ruedas:
            print(f"{type(v).__name__} => {v}")
            contador += 1
    print("")
    if ruedas is not None:
        print(f"Se han encontrado {contador} vehículos con {ruedas} ruedas.\\nn")

def main():
    vehiculos = [
    Coche("rojo", 4, 180, 2000),
    Camioneta("blanco", 4, 160, 2500, 1000),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 220, 600)
    ]

    catalogar(vehiculos)
    catalogar(vehiculos, 4)
    catalogar(vehiculos, 2)
    catalogar(vehiculos, 0)

main()