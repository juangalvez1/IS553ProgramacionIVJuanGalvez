from io import *

class Encuesta:

    def __init__(self, edad = 0, genero = "", ciudad = "", opinion = ""):
        self.edad = int(edad)
        self.genero = genero
        self.ciudad = ciudad
        self.opinion = opinion

    def __str__(self):
        return f"{self.edad},{self.genero},{self.ciudad},{self.opinion}"
    
    def save(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\encuesta-" + f"{self.ciudad}.txt", "+a") as file:
            file.write(f"{self}\n")

    def statistics(self, cities = []):
        males = []
        females = []
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\encuesta-cities.txt", "r") as cities:
            for line in cities:
                city = line.strip()
                with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\encuesta-" + f"{city}.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        # print(data)
                        if data[1] == "m":
                            males.append(data[3])
                        else:
                            females.append(data[3])
                
        print("\nOpiniones de los hombres: \n")
        for opinion in males:
            print(opinion)
        print()
        
        print("\nOpiniones de las mujeres: \n")
        for opinion in females:
            print(opinion)


def main():
    while 1:
        edad = int(input("Ingrese la edad: "))
        genero = input("Ingrese el genero (m/f): ")
        ciudad = input("Ingrese la ciudad: ")
        opinion = input("Ingrese la opinion: ")

        response = Encuesta(edad, genero, ciudad, opinion)
        # print(response)
        response.save()

        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\encuesta-cities.txt", "r+") as cities:
            data = cities.read().split("\n")

            if ciudad not in data:
                cities.write(f"{ciudad}\n")
            else:
                pass


        flag = input("¿Desea registrar otra respuesta?(s/n): ")
        if flag != "s":
            break
    
    print()
    temp = Encuesta
    temp.statistics(ciudad)

main()