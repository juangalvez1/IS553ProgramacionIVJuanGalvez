class Animal: # clase padre
    def hablar(self):
        return "Este animal hace un ruido no identificado"

class Gato(Animal):
    def hablar(self):
        return "miau"
    
class Perro(Animal):
    def hablar(self):
        return "guau"
    
class Vaca(Animal):
    def hablar(self):
        return "muuu"


def main():
    animals = [Gato(), Perro(), Vaca()]

    for i in animals:
        print(i.hablar())
main()