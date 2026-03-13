def main():
    print("Punto 4 del parcial I\n")
    num = int(input("Ingrese un numero de 4 cifras: "))

    firstDigit = num // 1000
    secondDigit = (num % 1000) // 100
    thirdDigit = (num % 100) // 10
    fourthDigit = num % 10
    if fourthDigit != 0:
        if firstDigit % fourthDigit == 0:
            print(f"\n{firstDigit} SI es multiplo de {fourthDigit}")
        else:
            print(f"\n{firstDigit} NO es multiplo de {fourthDigit}")
    else:
        print(f"El cuarto digito es '{fourthDigit}' entonces no se puede comprobar si el primer digito es multiplo del cuarto digito.\n")

    sumSecondThird = secondDigit + thirdDigit
    print (f"La suma del secondDigit y el tercer numero es: {sumSecondThird}")

main()