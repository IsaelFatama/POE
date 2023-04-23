# Método eval() de un objeto code: El método eval() de un objeto code también 
# permite ejecutar una cadena de caracteres como una expresión de Python.

cadena = "2 + 2"
expresion = compile(cadena, "<string>", "eval")
resultado = eval(expresion)
print(resultado)  # Imprime 4

