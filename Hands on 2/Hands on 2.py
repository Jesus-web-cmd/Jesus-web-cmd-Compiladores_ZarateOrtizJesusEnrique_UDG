import re

# Definir los patrones de los tokens
TOKEN_PATTERNS = {
    'PALABRA CLAVE': [r'\bint\b', r'\breturn\b'],  # Palabras clave
    'IDENTIFICADOR': [r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'],  # Identificadores
    'NÚMERO': [r'\b\d+\b'],  # Números enteros
    'CADENA': [r'"[^"]*"'],  # Cadenas entre comillas dobles
    'COMENTARIO': [r'//.*'],  # Comentarios de una línea
    'COMENTARIO MULTILÍNEA': [r'/\*[\s\S]*?\*/'],  # Comentarios multilínea
    'OPERADOR': [r'[=+\-*/<>!]'],  # Operadores básicos
    'DELIMITADOR': [r'[;(),{}]']  # Delimitadores como ; , () {}
}

def analizar_codigo(texto):
    contador_tokens = {categoria: 0 for categoria in TOKEN_PATTERNS}
    
    for categoria, patrones in TOKEN_PATTERNS.items():
        for patron in patrones:
            coincidencias = re.findall(patron, texto)
            contador_tokens[categoria] += len(coincidencias)
            for coincidencia in coincidencias:
                print(f"{categoria}: {coincidencia}")
    
    return contador_tokens

# Leer el archivo de entrada
def main():
    with open("input.txt", "r") as archivo:
        codigo = archivo.read()

    print("Análisis léxico:")
    conteo = analizar_codigo(codigo)
    
    print("\nResumen del análisis:")
    for categoria, cantidad in conteo.items():
        print(f"{categoria}: {cantidad}")

if __name__ == "__main__":
    main()
