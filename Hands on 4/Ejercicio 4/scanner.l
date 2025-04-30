%{
#include "parser.tab.h"   // Encabezados de Bison
#include <string.h>       // Para strdup
#include <stdlib.h>       // Para malloc, free
%}

%%
"int"               { return INT; }
[a-zA-Z_][a-zA-Z0-9_]* { yylval.str = strdup(yytext); return ID; }
";"                 { return PUNTOYCOMA; }
"{"                 { return LLAVEIZQ; }
"}"                 { return LLAVEDER; }
[ \t\r\n]+         ;  // Ignorar espacios y saltos de línea
.                    { return yytext[0]; }
%%

int yywrap(void) { return 1; }