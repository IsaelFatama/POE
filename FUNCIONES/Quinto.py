# Método exec() de un objeto AST (Abstract Syntax Tree): El módulo ast de Python proporciona una 
# forma de analizar y manipular el árbol de sintaxis abstracta de un código fuente de Python. 
# El método compile() del módulo ast permite compilar una cadena de caracteres en un objeto AST, 
# que luego se puede ejecutar utilizando el método exec().

import ast

cadena = "print('Hola, mundo!')"
arbol = ast.parse(cadena)
bloque = compile(arbol, "<string>", "exec")
exec(bloque)  # Imprime "Hola, mundo!"
