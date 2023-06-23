import random

# Lista para almacenar los datos de las personas
personas = []

# Función para verificar el formato del NIF
def validar_nif(nif):
    if len(nif) != 12:
        return False
    if not nif[:8].isdigit():
        return False
    if nif[8] != '-':
        return False
    if not nif[9:].upper():
        return False
    return True
# Función para grabar los datos de una persona
def grabar_persona():
    nif = input("Introduce el NIF: ")
    if not validar_nif(nif):
        print("El formato del NIF es incorrecto.")
        return
    nombre = input("Introduce el nombre: ")
    if len(nombre) < 8:
        print("El nombre debe tener al menos 8 caracteres.")
        return
    edad = int(input("Introduce la edad: "))
    if edad < 0:
        print("La edad debe ser mayor o igual a 0.")
        return
    persona = {'NIF': nif, 'Nombre': nombre, 'Edad': edad}
    personas.append(persona)
    print("Persona grabada exitosamente.")
# Función para buscar a una persona por su NIF
def buscar_persona():
    nif = input("Introduce el NIF de la persona a buscar: ")
    for persona in personas:
        if persona['NIF'] == nif:
            print("Información de la persona:")
            print("NIF:", persona['NIF'])
            print("Nombre:", persona['Nombre'])
            print("Edad:", persona['Edad'])
            if persona['NIF'][:2] == 'ES':
                print("Pertenece a la Unión Europea.")
            else:
                print("No pertenece a la Unión Europea.")
            return
    print("No se encontró ninguna persona con ese NIF.")

# Función para imprimir los certificados
def imprimir_certificados():
    for persona in personas:
        print("Certificado de Nacimiento:")
        print("Nombre:", persona['Nombre'])
        print("NIF:", persona['NIF'])
        print("Estado conyugal: Soltero/a")
        if persona['NIF'][:2] == 'ES':
            print("Pertenece a la Unión Europea.")
        else:
            print("No pertenece a la Unión Europea.")
        print()

# Función principal que muestra el menú
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Grabar")
        print("2. Buscar")
        print("3. Imprimir certificados")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            grabar_persona()
        elif opcion == '2':
            buscar_persona()
        elif opcion == '3':
            imprimir_certificados()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

# Ejecutar el programa
menu()
