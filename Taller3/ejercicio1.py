from io import *

class Libro:
    def __init__(self, titulo = "", autor = "", año = 0, editorial = "", genero = ""):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.editorial = editorial 
        self.genero = genero

    def __str__(self):
        return f"{self.titulo},{self.autor},{self.año},{self.editorial},{self.genero}"
    
    def save(self):
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\books.txt", "+a") as file:
            file.write(f"{self}\n")
    
    def searhcByAutor(self):
        autor = input("Ingrese el autor para buscar sus libros: ")
        with open(r"C:\JuanJose\UTP\Semestre5\Programacion4\Taller3\files\books.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if data[1] == autor:
                    print(f"Titulo: {data[0]} - Año: {data[2]} - Editorial: {data[3]} - Género: {data[4]}")
    

def main():
    while 1:
        titulo = input("Ingrese el titulo: ")
        autor = input("Ingrese el autor: ")
        año = int(input("Ingrese el año cuando se publico: "))
        editorial = input("Ingrese la editorial: ")
        genero = input("Ingrese el género: ")

        book = Libro(titulo, autor, año, editorial, genero)
        print(book)
        book.save()

        flag = input("¿Desea registrar otro libro?(s/n): ")
        if flag != "s":
            break

    temp = Libro()
    temp.searhcByAutor()

main()