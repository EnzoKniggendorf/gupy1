def verificar_letra_a(texto):
    contagem_a = texto.lower().count('a')
    return f"A letra 'a' aparece {contagem_a} vez(es) na string." if contagem_a > 0 else "A letra 'a' não aparece na string."

string_informada = "Aprendendo Python agora!"
print(verificar_letra_a(string_informada))
