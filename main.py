import herramientas
import validaciones

# Cargamos los datos una sola vez al principio
lista_inscriptos = herramientas.cargar_datos()

while True:
    print("\n--- MENÚ SISTEMA UTN ---")
    print("1. Registrar nuevo alumno")
    print("2. Ver lista de inscriptos")
    print("3. Buscar por nombre")
    print("4. Eliminar registro de alumno")
    print("5. Actualizar registro")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        email = input("Email: ")
        
        if validaciones.validar_email(email) and validaciones.validar_nombre(nombre):
            edad = herramientas.obtener_edad_validada()
            nuevo = {"nombre": nombre, "email": email, "edad": edad}
            lista_inscriptos.append(nuevo)
            herramientas.guardar_datos(lista_inscriptos)
            print("¡Alumno guardado con éxito!")
        else:
            print("Datos inválidos. Reintente.")

    elif opcion == "2":
        print("\n--- LISTADO DE ALUMNOS ---")
        if not lista_inscriptos:
            print("No hay alumnos registrados.")
        else:
            for alu in lista_inscriptos:
                print(f"Nombre: {alu['nombre']} | Edad: {alu['edad']} | Email: {alu['email']}")
    
    elif opcion == "4":
        cantidad_antes = len(lista_inscriptos)
        alumno_a_eliminar = (input("Ingresar el correo del alumno ")).lower().strip()
        lista_inscriptos = [alu for alu in lista_inscriptos if alu["email"] != alumno_a_eliminar]
        if len(lista_inscriptos) < cantidad_antes:
            print("Registro eliminado exitosamente")
        else:
            print("No se encontro ningún alumno con ese correo")
                
    elif opcion == "3":
        nombre_a_buscar = input("Ingrese el nombre del alumno a buscar: ")
        encontrado = herramientas.buscar_alumno(lista_inscriptos, nombre_a_buscar)
        
        if encontrado:
            print(f"\n¡Alumno encontrado!")
            print(f"Nombre: {encontrado['nombre']} | Email: {encontrado['email']}")
        else:
            print("\n[!] No se encontró ningún alumno con ese nombre.")

    elif opcion == "5":
        email_buscado = (input("Ingresar email del alumno a modificar: ")).lower().strip()
        alumno = herramientas.buscar_alumno(lista_inscriptos, email_buscado)
        if alumno:
            print(f"Alumno encontrado: {alumno['nombre']}")
            while True:
                nuevo_nombre = input("Ingrese nuevo nombre: ").strip()
                if validaciones.validar_nombre(nuevo_nombre):
                    alumno ['nombre'] = nuevo_nombre
                    print("Nombre actualizado")
                    herramientas.guardar_datos(lista_inscriptos)
                    break
                else:
                    print("Error, el nombre debe contener al menos 3 letras")
        else:
            print("No se encontro alumno con ese correo!!!")

    elif opcion == "6":
        print("Saliendo del sistema. ¡Hasta luego!")
        break # Este break rompe el bucle del menú y cierra el programa

    else:
        print("Opción no válida.")