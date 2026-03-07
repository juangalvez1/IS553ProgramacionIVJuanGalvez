from io import *

class Estudiante:
    
    def __init__(self, nombre = "", codigo = 0, carrera = "", edad = 0, promedio = 0.0):
        self.nombre = nombre
        self.codigo = codigo
        self.carrera = carrera
        self.edad = edad
        self.promedio = promedio

    def __str__(self):
        return f"{self.nombre},{self.codigo},{self.carrera},{self.edad},{self.promedio} - Aprobado:{"Si" if self.isApproved() else "No"}"
    
    def save(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\students.txt", "+a") as file:
            file.write(f"{self}\n")

    def isApproved(self):
        return self.promedio >= 3.0
    
def main():
    while 1:
        nombre = input("Ingrese el nombre: ")
        codigo = int(input("Ingrese el codigo: "))
        carrera = input("Ingrese la carrera: ")
        edad = int(input("Ingrese la edad: "))
        promedio = float(input("Ingrese el promedio: "))

        student = Estudiante(nombre, codigo, carrera, edad, promedio)
        print(student)
        student.save()

        flag = input("¿Desea registrar otro estudiante?(s/n): ")
        if flag != "s":
            break

main()