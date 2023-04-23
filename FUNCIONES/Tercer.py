# Método exec() de un objeto code: El método exec() de un objeto code 
# también permite ejecutar una cadena de caracteres como un bloque de código de Python.

cadena = "print('Hola, mundo!')"
bloque = compile(cadena, "<string>", "exec")
exec(bloque)  # Imprime "Hola, mundo!"
