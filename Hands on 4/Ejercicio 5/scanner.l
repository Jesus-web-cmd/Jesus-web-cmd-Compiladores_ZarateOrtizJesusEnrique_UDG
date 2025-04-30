%{
#include "parser.tab.h"   // Tokens generados por Bison
#include <string.h>       // Para strdup
#include <stdlib.h>       // Para malloc, free
%}

%%
"int"               { return INT; }
"func"              { return FUNC; }
"return"            { return RETURN; }
[a-zA-Z_][a-zA-Z0-9_]* { yylval.str = strdup(yytext); return ID; }
"="                 { return IGUAL; }
"("                 { return PARIZQ; }
")"                 { return PARDER; }
"{"                 { return LLAVEIZQ; }
"}"                 { return LLAVEDER; }
";"                 { return PUNTOYCOMA; }
","                 { return COMA; }
[ \t\r\n]+         ;  // Ignorar espacios y saltos de línea
.                    { return yytext[0]; }
%%

int yywrap(void) { return 1; }