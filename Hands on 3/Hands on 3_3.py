from pyparsing import infixNotation, opAssoc, Word, nums, Literal, Forward, Suppress, Group

def crear_analizador():
    expr = Forward()
    logical = Forward()
    
    # Definir números y booleanos
    number = Word(nums)
    boolean = Word("01")
    
    # Definir operadores
    lpar, rpar = map(Suppress, "()")
    plus, minus = map(Literal, "+-")
    mult, div = map(Literal, "*/")
    and_op, or_op, not_op = map(Literal, ["AND", "OR", "NOT"])
    
    # Definir factores
    factor = number | boolean | Group(lpar + expr + rpar)
    
    # Definir términos y expresiones aritméticas
    term = infixNotation(factor, [(mult | div, 2, opAssoc.LEFT)])
    expr <<= infixNotation(term, [(plus | minus, 2, opAssoc.LEFT)])
    
    # Definir expresiones lógicas
    logical_factor = expr | boolean | Group(lpar + logical + rpar)
    logical_term = infixNotation(logical_factor, [(not_op, 1, opAssoc.RIGHT)])
    logical <<= infixNotation(logical_term, [(and_op, 2, opAssoc.LEFT), (or_op, 2, opAssoc.LEFT)])
    
    return logical

def validar_expresion(expresion):
    analizador = crear_analizador()
    try:
        analizador.parseString(expresion, parseAll=True)
        return "Expresión válida"
    except:
        return "Expresión inválida"

# Pruebas
expresiones = ["(4 + 5) * (2 AND 1)", "(2 AND 3) / (4 - 1"]
for exp in expresiones:
    print(f"Entrada: {exp}\nSalida: {validar_expresion(exp)}\n")
