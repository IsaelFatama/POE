# Módulo codeop: El módulo codeop de Python proporciona varias funciones que permiten compilar y 
# ejecutar cadenas de caracteres de manera segura. Por ejemplo, la función compile_command() 
# permite compilar una cadena de caracteres en un objeto code, que luego se puede ejecutar utilizando 
# el método exec(). La función eval_command() permite evaluar una cadena de caracteres como una expresión 
# de Python. 

import codeop

cadena = "print('Hola, mundo!')"
codigo = codeop.compile_command(cadena)
exec(codigo)  # Imprime "Hola, mundo!"

cadena = "2 + 2"
resultado = codeop.eval_command(cadena)
print(resultado)  # Imprime 4
