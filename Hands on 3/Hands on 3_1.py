from pyparsing import infixNotation, opAssoc, Word, nums, Literal, Forward, Suppress, Group

def crear_analizador():
    expr = Forward()
    
    # Definir un número
    number = Word(nums)
    
    # Definir paréntesis y operadores
    lpar, rpar = map(Suppress, "()")
    plus, minus = map(Literal, "+-")
    mult, div = map(Literal, "*/")
    
    # Definir factores
    factor = number | Group(lpar + expr + rpar)
    
    # Definir términos y expresiones con la nueva sintaxis de infixNotation
    term = infixNotation(factor, [(mult | div, 2, opAssoc.LEFT)])
    expr <<= infixNotation(term, [(plus | minus, 2, opAssoc.LEFT)])
    
    return expr

def validar_expresion(expresion):
    analizador = crear_analizador()
    try:
        analizador.parseString(expresion, parseAll=True)
        return "Expresión válida"
    except Exception as e:
        return f"Expresión inválida: {e}"

# Pruebas
expresiones = ["(4 + 5) * 2", "3 - (2 + )"]
for exp in expresiones:
    print(f"Entrada: {exp}\nSalida: {validar_expresion(exp)}\n")
