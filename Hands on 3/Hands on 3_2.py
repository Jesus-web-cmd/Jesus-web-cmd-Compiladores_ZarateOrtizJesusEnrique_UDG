from pyparsing import infixNotation, opAssoc, Word, Literal, Forward, Suppress, Group

def crear_analizador():
    expr = Forward()
    
    # Definir valores booleanos
    boolean = Word("01")
    
    # Definir operadores lógicos
    lpar, rpar = map(Suppress, "()")
    and_op = Literal("AND")
    or_op = Literal("OR")
    not_op = Literal("NOT")
    
    # Definir factores
    factor = boolean | Group(lpar + expr + rpar)
    
    # Definir términos y expresiones
    term = infixNotation(factor, [(not_op, 1, opAssoc.RIGHT)])
    expr <<= infixNotation(term, [(and_op, 2, opAssoc.LEFT), (or_op, 2, opAssoc.LEFT)])
    
    return expr

def validar_expresion(expresion):
    analizador = crear_analizador()
    try:
        analizador.parseString(expresion, parseAll=True)
        return "Expresión válida"
    except:
        return "Expresión inválida"

# Pruebas
expresiones = ["(1 AND 0) OR (NOT 1)", "(1 AND (0 OR 1)"]
for exp in expresiones:
    print(f"Entrada: {exp}\nSalida: {validar_expresion(exp)}\n")
