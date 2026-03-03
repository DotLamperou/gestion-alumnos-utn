def validar_email(correo):
    # Agregamos .strip() para evitar errores por espacios accidentales
    correo = correo.strip()
    return "@" in correo and correo.endswith(".com")

def validar_nombre(nombre):
    # .strip() elimina espacios. .isalpha() asegura que sean letras (UTN: Programación I)
    nombre_limpio = nombre.strip()
    return len(nombre_limpio) >= 3