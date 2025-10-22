from datetime import date
iniciar = input("Quisiera iniciar? (si/no):").lower()

def pedir_datos():
    P = float(input("Dame tu peso en kg: "))
    A = float(input("Dame tu altura en cm: "))
    E = float(input("Dame tu edad: "))
    objetivo = int(input("Dime cuál es tu objetivo (subir = 1, bajar = 2, mantener = 3): "))
    return P, A, E, objetivo

def calorias_necesarias(objetivo, P, A, E):
    objetivos = {1: "subir", 2: "bajar", 3: "mantener"}
    objetivo_elegido = objetivos[objetivo]
    if objetivo_elegido == "subir":
        return 66.47 + (13.75 * P) + (5 * A) - (6.74 * E) + 500
    elif objetivo_elegido == "bajar":
        return 66.47 + (13.75 * P) + (5 * A) - (6.74 * E) - 500
    elif objetivo_elegido == "mantener":
        return 66.47 + (13.75 * P) + (5 * A) - (6.74 * E)

def calcular_calorias_ideales(objetivo, P, A, E):
    calorias_ideales = calorias_necesarias(objetivo, P, A, E)
    print("Tu cantidad ideal de calorías:", calorias_ideales)
    return calorias_ideales

def registrar_comida():
    while True:
        comida = input("Comida del día (desayuno, comida, cena, snack): ")
        if comida in ["desayuno", "comida", "cena", "snack"]:
            break
        else:
            print("Opción inválida. Elige: desayuno, comida, cena o snack")
    calorias = float(input("Ingresa las calorías de la comida: "))
    return comida, calorias

def registrar_dia(objetivo, calorias_ideales):
    comidas_dia = []
    total_dia = 0
    continuar_comida = "si"

    while continuar_comida == "si":  
        comida, calorias = registrar_comida()
        comidas_dia.append([comida, calorias])
        total_dia += calorias

        while True:
            continuar_comida = input("Quieres seguir registrando comidas (si/no)?: ").lower()
            if continuar_comida in ["si", "no"]:
                break
            else:
                print("Opción inválida. Escribe 'si' o 'no'.")
    print("Total de este día:", total_dia)
    evaluar_objetivo(objetivo, total_dia, calorias_ideales)
    return comidas_dia, total_dia

def guardar_csv(objetivo, calorias_ideales):
    comidas_dia, total_dia = registrar_dia(objetivo, calorias_ideales)
    fecha = date.today()

    with open('calorias.csv', 'a') as file:
        for comida, calorias in comidas_dia:
            file.write(f"{fecha},{comida},{calorias},{total_dia}\n")

def evaluar_objetivo(objetivo, total_dia, calorias_ideales):
    if calorias_ideales > 0:
        if objetivo == 1:
            if total_dia >= calorias_ideales:
                print("Lograste tu objetivo")
            else:
                print("No lograste tu objetivo")
        elif objetivo == 2:
            if total_dia <= calorias_ideales:
                print("Lograste tu objetivo")
            else:
                print("No lograste tu objetivo")
        elif objetivo == 3:
            if (total_dia >= calorias_ideales - 200) and (total_dia <= calorias_ideales + 200):
                print("Lograste tu objetivo")
            else:
                print("No lograste tu objetivo")
    else:
        print("Aún no se establece cantidad ideal")

if iniciar == "si":
    print("""
1. Pedir datos del usuario
2. Establecer cantidad ideal de calorías
3. Registrar datos de comidas
4. Salir
""")
    P = A = E = 0
    objetivo = 0
    calorias_ideales = 0

    while True:
        opcion = int(input("Elige tu opción: "))

        if opcion == 1:
            P, A, E, objetivo = pedir_datos()
        elif opcion == 2:
            if P and A and E and objetivo:
                calorias_ideales = calcular_calorias_ideales(objetivo, P, A, E)
            else:
                P, A, E, objetivo = pedir_datos()
                calorias_ideales = calcular_calorias_ideales(objetivo, P, A, E)
        elif opcion == 3:
            if P == 0 or objetivo == 0 or calorias_ideales == 0:
                P, A, E, objetivo = pedir_datos()
                calorias_ideales = calcular_calorias_ideales(objetivo, P, A, E)
                guardar_csv(objetivo, calorias_ideales)
            else:
                guardar_csv(objetivo, calorias_ideales)
        elif opcion == 4:
            print("Adiós")
            break
        else:
            print("Opción inválida")
else:
    print("Okay")
