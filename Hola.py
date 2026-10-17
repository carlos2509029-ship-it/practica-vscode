# Este es solo un ejercicio para confirmar que estoy haciendo bien las cosas en git - GitHub
def adivinar(inferior, superior):
    medio = (inferior + superior) // 2

    respuesta = input(
        f"¿Tu número es {medio}? "
        "(escribe 'mayor', 'menor' o 'si'): "
    ).lower()

    if respuesta == "si":
        print(f"¡He adivinado tu número! Es {medio}.")
    elif respuesta == "mayor":
        adivinar(medio + 1, superior)
    elif respuesta == "menor":
        adivinar(inferior, medio - 1)
    else:
        print("Respuesta no válida.")
        adivinar(inferior, superior)


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

while num1 == num2:
    print("Los números deben ser distintos.")
    num2 = int(input("Introduce un segundo número diferente: "))

inferior = min(num1, num2)
superior = max(num1, num2)

print(f"\nPiensa en un número entre {inferior} y {superior}.")
input("Cuando estés listo, presiona Enter...")

adivinar(inferior, superior)