# Función para validar si una cadena contiene solo caracteres alfabéticos
def validate_alpha(s):
    return s.isalpha()

# Función principal
def main():
    test_strings = [
        "HelloWorld",  # Válida
        "PythonRocks",  # Válida
        "PruebaDeTexto",  # Válida
        "SoloLetras",  # Válida
        "Hello123",  # Inválida (contiene números)
        "Python!",  # Inválida (contiene carácter especial)
        "Test_Valid",  # Inválida (contiene guion bajo)
        "ABC 123"  # Inválida (contiene espacio y números)
    ]
    
    for input_str in test_strings:
        if validate_alpha(input_str):
            print(f"'{input_str}': Cadena válida.")
        else:
            print(f"'{input_str}': Cadena inválida.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
    

# Función para validar si una cadena representa un número real
def validate_real(s):
    try:
        float(s)  # Intenta convertir la cadena a float
        return True
    except ValueError:
        return False

# Función principal
def main():
    test_numbers = [
        "-123.456",  # Válido (número negativo con decimales)
        "789.01",  # Válido (número positivo con decimales)
        "0.0",  # Válido (cero con decimales)
        "42",  # Válido (número entero, sigue siendo convertible a float)
        "3.14159",  # Válido (número decimal)
        "-0.5",  # Válido (número decimal negativo)
        "abc",  # Inválido (caracteres no numéricos)
        "12.34.56",  # Inválido (formato incorrecto con múltiples puntos decimales)
        "4.5e3",  # Válido (notación científica: 4.5 × 10³ = 4500)
        ""  # Inválido (cadena vacía)
    ]
    
    for input_str in test_numbers:
        if validate_real(input_str):
            print(f"'{input_str}': Número válido.")
        else:
            print(f"'{input_str}': Número inválido.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()


# Función para validar si una cadena contiene 'if' y 'else'
def validate_if_else(s):
    return "if" in s and "else" in s

# Función principal
def main():
    test_statements = [
        "if x > 0: pass else: pass",  # Válido (contiene 'if' y 'else')
        "if condition: do_something() else: do_other()",  # Válido
        "if True: print('Yes') else: print('No')",  # Válido
        "if a == b: print('Equal')",  # Inválido (falta 'else')
        "else: print('Only else')",  # Inválido (falta 'if')
        "print('No conditions here')",  # Inválido (no tiene 'if' ni 'else')
        "if x: pass if y: pass else: pass",  # Válido (contiene 'if' y 'else')
        "if this and that or else: print('Confusing')"  # Inválido ('else' no es parte de una estructura condicional)
    ]
    
    for input_str in test_statements:
        if validate_if_else(input_str):
            print(f"'{input_str}': Sentencia válida.")
        else:
            print(f"'{input_str}': Sentencia inválida.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()