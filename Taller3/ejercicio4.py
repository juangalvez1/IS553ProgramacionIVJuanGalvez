from io import *
from datetime import datetime

class Vehiculo:

    def __init__(self, marca = "", modelo = "", año = 0, tipo = "", placa = ""):
        self.marca = marca
        self.modelo = modelo
        self.año = int(año)
        self.tipo = tipo
        self.placa = placa

    def __str__(self):
        return f"{self.marca},{self.modelo},{self.año},{self.tipo},{self.placa}"

    def save(self):
        if self.año == datetime.now().year:
            with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\vehicles.txt", "+a") as file:
                file.write(f"{self}\n")
            print("\n\nSe ha guardado exitosamente el vehiculo!\n\n")
        else:
            print("\n\nEl vehiculo no es de este año!\n\n")
    

def main():
    while 1:
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        año = int(input("Ingrese el año: "))
        tipo = input("Ingrese el tipo: ")
        placa = input("Ingrese la placa: ")

        car = Vehiculo(marca, modelo, año, tipo, placa)
        print(car)
        car.save()

        flag = input("¿Desea registrar otro vehiculo?(s/n): ")
        if flag != "s":
            break

main()