
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Elija una opción: "))
            return opcion
        except ValueError:
            pass


def validar_nombre(nombre):
    if nombre == "" or nombre.isspace():
        return False
    return True


def validar_edad(edad_str):
    try:
        edad = int(edad_str)
        if edad > 0:
            return True
        return False
    except ValueError:
        return False


def validar_nota(nota_str):
    try:
        nota = float(nota_str)
        if 1.0 <= nota <= 7.0:
            return True
        return False
    except ValueError:
        return False


def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre completo del estudiante: ")
    edad_str = input("Ingrese la edad del estudiante: ")
    nota_str = input("Ingrese la nota de la asignatura (1.0-7.0): ")


    es_valido = True

    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.")
        es_valido = False

    if not validar_edad(edad_str):
        print("Error: La edad debe ser un número entero mayor que cero.")
        es_valido = False

    if not validar_nota(nota_str):
        print("Error: La nota debe ser un número decimal entre 1.0 y 7.0.")
        es_valido = False

    # Solo cuando todos los datos son válidos se crea el diccionario y se agrega a la lista
    if es_valido:
        estudiante = {
            "nombre": nombre,
            "edad": int(edad_str),
            "nota": float(nota_str),
            "aprobado": False  # False al registrar, el sistema lo asigna automáticamente
        }
        lista_estudiantes.append(estudiante)



def buscar_estudiante(lista_estudiantes, nombre_buscar):
    for i in range(len(lista_estudiantes)):
        if lista_estudiantes[i]["nombre"] == nombre_buscar:
            return i
    return -1



def actualizar_estados(lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False



def mostrar_estudiantes(lista_estudiantes):
    # El sistema primero actualiza los estados haciendo el llamado a la función anterior
    actualizar_estados(lista_estudiantes)

    print("=== LISTA DE ESTUDIANTES ===")
    print()
    for estudiante in lista_estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota: {estudiante['nota']}")
        if estudiante["aprobado"]:
            print("Estado: APROBADO")
        else:
            print("Estado: REPROBADO")
        print("****************************************")



def main():

    lista_estudiantes = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_estudiante(lista_estudiantes)

        elif opcion == 2:
            nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")
            posicion = buscar_estudiante(lista_estudiantes, nombre_buscar)
            if posicion != -1:
                estudiante = lista_estudiantes[posicion]
                print(f"Posición en la lista: {posicion}")
                print(f"Nombre: {estudiante['nombre']}")
                print(f"Edad: {estudiante['edad']}")
                print(f"Nota: {estudiante['nota']}")
                if estudiante["aprobado"]:
                    print("Estado: APROBADO")
                else:
                    print("Estado: REPROBADO")
            else:
                print("Estudiante no encontrado.")

        elif opcion == 3:
            nombre_eliminar = input("Ingrese el nombre del estudiante que se desea eliminar: ")
            posicion = buscar_estudiante(lista_estudiantes, nombre_eliminar)
            if posicion != -1:
                lista_estudiantes.pop(posicion)
            else:
                print(f"El estudiante '{nombre_eliminar}' no se encuentra registrado.")

        elif opcion == 4:
            actualizar_estados(lista_estudiantes)

        elif opcion == 5:
            mostrar_estudiantes(lista_estudiantes)

        elif opcion == 6:
            print("“Gracias por usar el sistema. Vuelva Pronto”")
            break


main()
