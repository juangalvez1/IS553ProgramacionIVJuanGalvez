from io import *
import time

class NotaMusical:
    def __init__(self, nombre = "", frecuencia = 0, duracion = 0):
        self.nombre = nombre
        self.frecuencia = frecuencia
        self.duracion = duracion

    def __str__(self):
        return f"{self.nombre},{self.frecuencia},{self.duracion}"

    def save(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\notas-musicales.txt", "a") as file:
            file.write(f"{self}\n")

    def playNotes(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\notas-musicales.txt", "r") as file:
            for line in file:
                note = line.strip().split(",")

                print(f"Reproduciendo: {note[0]} ({note[1]})")
                time.sleep(float(note[2]))

def main():
    while 1:
        nombre = input("Ingrese el nombre de la nota(Do, Re, Mi, Fa, Sol, La, Si): ")
        frecuencia = float(input("Ingrese la frecuencia de la nota (OJO, solo se guardan notas con frecuencia mayor a 128hz): "))
        duracion = float(input("Ingrese la duracion de la nota (s): "))

        note = NotaMusical(nombre, frecuencia, duracion)
        if note.frecuencia > 128.0:
            note.save()
        else:
            print("La frecuencia de la nota es muy baja y no se guardara.")

        flag = input("¿Desea registrar otra nota?(s/n): ")
        if flag != "s":
            break

    temp = NotaMusical()
    temp.playNotes()

main()