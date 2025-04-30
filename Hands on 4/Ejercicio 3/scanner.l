%{
#include "parser.tab.h"   // Incluye tokens de Bison
#include <string.h>       // Para strdup
#include <stdlib.h>       // Para atoi
%}

%%

"func"              { return FUNC; }                       // Palabra clave 'func'
[a-zA-Z_][a-zA-Z0-9_]* { yylval.str = strdup(yytext); return ID; }  // Identificadores
[0-9]+               { yylval.num = atoi(yytext); return NUM; }      // Literales numéricas
"("                 { return PARIZQ; }                     // Paréntesis izquierdo
")"                 { return PARDER; }                     // Paréntesis derecho
";"                 { return PUNTOYCOMA; }                 // Punto y coma
","                 { return COMA; }                        // Coma
[ \t\r\n]+         ;                                      // Ignorar espacios y saltos de línea
.                    { return yytext[0]; }                   // Cualquier otro carácter

%%

int yywrap(void) { return 1; }