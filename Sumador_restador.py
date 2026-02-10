
# Esta función simula una compuerta XOR usando solo AND, OR y NOT
# Básicamente devuelve 1 si los bits son diferentes
def XOR(a, b):
    # (a AND NOT b) OR (NOT a AND b)
    return (a & ~b) | (~a & b)


# Este es un sumador (full adder)
# Suma dos bits (a y b) y además el carry de entrada (cin)
# Devuelve:
#   - suma: el bit resultado
#   - carry: el acarreo que se va para el siguiente bit
def full_adder(a, b, cin):

    # Primero hacemos XOR entre a y b
    # Esto da una suma parcial
    s1 = XOR(a, b)

    # Luego hacemos XOR de esa suma parcial con el carry de entrada
    # Esto nos da la suma final del bit
    suma = XOR(s1, cin)

    # Aquí calculamos posibles carries:
    # c1 es carry si a y b son 1
    c1 = a & b

    # c2 es carry si s1 y cin son 1
    c2 = s1 & cin

    # El carry final sale si cualquiera de los dos es 1
    carry = c1 | c2

    # Retornamos el bit de suma y el carry
    return suma, carry


# Esta función es el sumador/restador de 4 bits
# A y B son listas de 4 bits (LSB primero)
# mode:
#   0 = suma
#   1 = resta (usando complemento a dos)
def add_sub_4bit(A, B, mode):

    # Aquí guardamos el resultado final bit por bit
    result = [0, 0, 0, 0]

    # El carry inicial es igual al modo
    # Si es resta, arrancamos con +1 (complemento a dos)
    carry = mode

    # Recorremos los 4 bits (del menos significativo al más)
    for i in range(4):

        # Si es resta, invertimos B usando XOR con mode
        # Si mode = 0 -> B queda igual
        # Si mode = 1 -> B se invierte (NOT)
        b_mod = XOR(B[i], mode)

        # Usamos el sumador completo para este bit
        # Le pasamos:
        #   A[i], B modificado, y el carry anterior
        result[i], carry = full_adder(A[i], b_mod, carry)

    # Devolvemos la lista resultado y el carry final
    return result, carry


# Esta función convierte un número decimal (0 a 15)
# a una lista de 4 bits
# Ejemplo:
#   5 -> 0101 -> [1,0,1,0] (LSB primero)
def decimal_to_4bit_list(n):

    # Validamos que esté en rango de 4 bits
    if n < 0 or n > 15:
        print(" Error: Solo números entre 0 y 15")
        return None

    # Convertimos a binario de 4 bits con ceros
    bin_str = format(n, '04b')

    # Convertimos a lista de enteros
    # reversed es para que quede LSB primero
    return [int(bit) for bit in reversed(bin_str)]


# Esta es la función principal del programa
# Aquí está el menú y la interacción con el usuario
def menu():

    # Bucle infinito para que el menú siga hasta que el usuario salga
    while True:

        print("\n====== SUMADOR - RESTADOR 4 BITS ======")
        print("1. Sumar")
        print("2. Restar")
        print("3. Salir")

        # Leemos la opción del usuario
        opcion = input("Seleccione una opción: ")

        # Si elige salir, rompemos el ciclo
        if opcion == "3":
            print("Saliendo del programa...")
            break

        # Pedimos los números en decimal
        A_dec = int(input("Ingrese A (0 a 15): "))
        B_dec = int(input("Ingrese B (0 a 15): "))

        # Convertimos a binario de 4 bits
        A = decimal_to_4bit_list(A_dec)
        B = decimal_to_4bit_list(B_dec)

        # Si hubo error, volvemos al menú
        if A is None or B is None:
            continue

        # Si eligió suma
        if opcion == "1":
            result, carry = add_sub_4bit(A, B, 0)
            print("\n--- SUMA ---")

        # Si eligió resta
        elif opcion == "2":
            result, carry = add_sub_4bit(A, B, 1)
            print("\n--- RESTA ---")

        # Opción inválida
        else:
            print("Opción inválida")
            continue

        # Mostramos todo bonito
        print("A (bin):", list(reversed(A)))
        print("B (bin):", list(reversed(B)))
        print("Resultado (bin):", list(reversed(result)))
        print("Carry:", carry)


# Aquí arranca el programa
# Llamamos al menú
menu()
