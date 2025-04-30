%{
#include "parser.tab.h"   // Archivo de encabezado generado por Bison
#include <string.h>       // Para strdup
#include <stdlib.h>       // Para malloc, free, etc.
%}
%%
"int"               { return INT; }
[a-zA-Z_][a-zA-Z0-9_]*  { yylval.str = strdup(yytext); return ID; }
"="                 { return IGUAL; }
";"                 { return PUNTOYCOMA; }
[ \t\r\n]+          ;  // Ignora espacios, tabs y saltos de línea
.                   { return yytext[0]; } // Cualquier otro carácter como error
%%
int yywrap(void) { return 1; }  // Evita error de referencia a yywrap
