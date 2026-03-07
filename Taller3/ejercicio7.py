from io import *

class AgendaContactos:
    def __init__(self, nombre ="", telefono = 0, correo = "", direccion = ""):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre},{self.telefono},{self.correo},{self.direccion}"
    
    def save(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\contacts.txt", "a") as file:
            file.write(f"{self}\n")

    def searchContact(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\contacts.txt", "r") as file:
            contacts = file.read().strip().split("\n")

            tels = []
            for contact in contacts:
                temp = contact.split(",")
                tels.append(int(temp[1]))

            telToSearch = int(input("Ingrese el telefono del contacto a buscar: "))

            if telToSearch in tels:
                print(f"Se ha encontrado el contacro con numero {telToSearch}:")
                print(contacts[tels.index(telToSearch)])
            else:
                print(f"El contacto con numero de telefono {telToSearch} no fue encontrado.")

def main():
    while 1:
        nombre = input("Ingrese el nombre: ")
        telefono = int(input("Ingrese el telefono: "))
        correo = input("Ingrese el correo: ")
        direccion = input("Ingrese la direccion: ")

        contact = AgendaContactos(nombre, telefono, correo, direccion)
        contact.save()

        flag = input("¿Desea registrar otro contacto?(s/n): ")
        if flag != "s":
            break

    temp = AgendaContactos()
    temp.searchContact()

main()