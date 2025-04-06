import re

texto = input("Ingrese una palabra o frase: ")

def termina_en_vocal_con_regex(texto):
    if not texto:
        return False
    return bool(re.search(r"[aeiou]$", texto.lower()))

if termina_en_vocal_con_regex(texto):
    resultado = texto + "!"
    print(resultado)
else:
    print(texto)
