
# Función para sumar dos números
def sumar(num1, num2):
    return num1 + num2

# Función para restar dos números
def restar(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicar(num1, num2):
    return num1 * num2

# Función para dividir dos números
def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero"

# Menú de opciones
print("Calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Seleccione una opción (1-4): ")

if opcion == "1":
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    resultado = sumar(numero1, numero2)
    print("El resultado es:", resultado)
elif opcion == "2":
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    resultado = restar(numero1, numero2)
    print("El resultado es:", resultado)
elif opcion == "3":
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    resultado = multiplicar(numero1, numero2)
    print("El resultado es:", resultado)
elif opcion == "4":
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    resultado = dividir(numero1, numero2)
    print("El resultado es:", resultado)
else:
    print("Opción inválida")
