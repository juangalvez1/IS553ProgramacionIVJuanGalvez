from io import *

class InventarioProducto:

    def __init__(self, nombre = "", precio = 0, cantidad = 0):
        self.nombre = nombre
        self.precio = int(precio)
        self.cantidad = int(cantidad)

    def __str__(self):
        return f"{self.nombre},{self.precio},{self.cantidad}"

    def save(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\inventory.txt", "+a") as file:
            file.write(f"{self}\n")

    def stockTotalPrice(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\inventory.txt", "r") as file:
            totalPrice = 0
            for line in file:
                data = line.strip().split(",")

                totalPrice += int(data[1]) * int(data[2])

            print(f"El valor total del inventario es: {totalPrice}")


def main():
    while 1:
        nombre = input("Ingrese el nombre: ")
        precio = int(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))

        product = InventarioProducto(nombre, precio, cantidad)
        print(product)
        product.save()

        flag = input("¿Desea registrar otro producto?(s/n): ")
        if flag != "s":
            break

    temp = InventarioProducto()
    temp.stockTotalPrice()

main()