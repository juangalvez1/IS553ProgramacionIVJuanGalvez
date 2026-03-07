from io import *

class SistemaNotas:
    def __init__(self, nombre = "", grade1 = .0, grade2 = .0, grade3 = .0):
        self.nombre = nombre
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
    
    def __str__(self):
        return f"{self.nombre},{self.grade1},{self.grade2},{self.grade3}"
    
    def save(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\notas.txt", "a") as file:
            file.write(f"{self}\n")

    def averageGrades(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\notas.txt", "r") as file:
            print("\nPromedio de notas por materia:\n")
            averageGrade1 = .0
            averageGrade2 =.0
            averageGrade3 = .0
            
            numberStudents = 0
            for line in file:
                data = line.strip().split(",")

                averageGrade1 += float(float(data[1]))
                averageGrade2 += float(data[2])
                averageGrade3 += float(data[3])
                numberStudents += 1

            averageGrade1 /= numberStudents
            averageGrade2 /= numberStudents
            averageGrade3 /= numberStudents

            print(f"Promedio materia 1: {averageGrade1}")
            print(f"Promedio materia 2: {averageGrade2}")
            print(f"Promedio materia 3: {averageGrade3}")

    def bestStudents(self):
        highestGrade1 = [float("-inf"), ""]
        highestGrade2 = [float("-inf"), ""]
        highestGrade3 = [float("-inf"), ""]
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\notas.txt", "r") as file:
            print("\n\nMejor estudiante por materia:\n")


            for line in file:
                data = line.strip().split(",")

                if float(data[1]) > highestGrade1[0]:
                    highestGrade1[0] = float(data[1])
                    highestGrade1[1] = data[0]
                
                if float(data[2]) > highestGrade2[0]:
                    highestGrade2[0] = float(data[2])
                    highestGrade2[1] = data[0]

                if float(data[3]) > highestGrade3[0]:
                    highestGrade3[0] = float(data[3])
                    highestGrade3[1] = data[0]

            print(f"Mejor estudiante materia 1: {highestGrade1[1]} - {highestGrade1[0]}")
            print(f"Mejor estudiante materia 2: {highestGrade2[1]} - {highestGrade2[0]}")
            print(f"Mejor estudiante materia 3: {highestGrade3[1]} - {highestGrade3[0]}")

        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\notas-best-students.txt", "w") as file:
            file.write(f"Materia 1: {highestGrade1[1]} - {highestGrade1[0]}\n")
            file.write(f"Materia 2: {highestGrade2[1]} - {highestGrade2[0]}\n")
            file.write(f"Materia 3: {highestGrade3[1]} - {highestGrade3[0]}\n")

def main():
    while 1:
        nombre = input("Ingrese el nombre: ")
        nota1 = float(input("Ingrese la nota 1: "))
        nota2 = float(input("Ingrese la nota 2: "))
        nota3 = float(input("Ingrese la nota 3: "))

        student = SistemaNotas(nombre, nota1, nota2, nota3)
        student.save()

        flag = input("¿Desea registrar otro estudiante?(s/n): ")
        if flag != "s":
            break

    temp = SistemaNotas()
    temp.averageGrades()
    temp.bestStudents()

main()
