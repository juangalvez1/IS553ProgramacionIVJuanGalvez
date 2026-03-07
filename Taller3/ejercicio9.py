from io import *

class Empresa:
    def __init__(self, nombre = "", salario = .0, dpto = "", bonus = 0.1, descuento = 0.05): # bonus y descuento se trata como un porcentaje
        self.nombre = nombre
        self.salario = salario
        self.dpto = dpto
        self.bonus = bonus
        self.descuento = descuento

    def __str__(self):
        return f"{self.nombre},{self.salario},{self.dpto},{self.bonus},{self.descuento}"

    def save(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\empresa-" + f"{self.dpto}.txt", "a") as file:
            file.write(f"{self}\n")

    def statistics(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\empresa-dptos.txt", "r") as dptos:
            print("Se hara un promedio de los bonus de los empleados de la empresa por departamentos:\n")
            for line in dptos:
                dpto = line.strip()
                with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\empresa-" + f"{dpto}.txt", "r") as file:
                    employees = file.read().strip().split("\n")

                    bonuses = []
                    for employee in employees:
                        temp = employee.split(",")
                        bonuses.append(temp[3]) #guardar todos los bonus de los empleados por dpto

                    averageBonus = .0
                    numberEmployees = 0
                    for bonus in bonuses:
                        averageBonus += float(bonus)
                        numberEmployees += 1

                    averageBonus /= float(numberEmployees)

                    print(f"El promedio del departamento {dpto}: {averageBonus}")


def main():
    while 1:
        nombre = input("Ingrese el nombre: ")
        salario = float(input("Ingrese el salario: "))
        dpto = input("Ingrese el departamento: ")
        bonus = float(input("Ingrese el bonus (0 al 1): "))
        descuento = float(input("ingrese el descuento (0 al 1): "))

        employee = Empresa(nombre, salario, dpto, bonus, descuento)

        employee.save()

        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\empresa-dptos.txt", "a+") as dptos:
            dptos.seek(0)
            data = dptos.read().split("\n")

            if dpto not in data:
                dptos.write(f"{dpto}\n")
            else:
                pass

        flag = input("¿Desea registrar otro empleado?(s/n): ")
        if flag != "s":
            break

    temp = Empresa()
    temp.statistics()

main()