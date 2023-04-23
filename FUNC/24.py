# Usando una expresión regular
import re
texto = "Hola mundo"
patron = r"H(\d)l(\d) mund(\d)"
reemplazo = r"H\1o\2a mund\3o"
nuevo_texto = re.sub(patron, reemplazo, texto)
print(nuevo_texto)