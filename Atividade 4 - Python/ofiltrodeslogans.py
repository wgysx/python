produto = input("Qual é o nome do produto? ")


slogan = input("Qual é o slogan? ")


palavra_chave = input("Qual é a palavra-chave? ")


if palavra_chave in slogan:
    print("Slogan adequado (palavra-chave está no slogan).")
else:
    print("Slogan inadequado (palavra-chave não está no slogan).")


palavras = slogan.split()
num_palavras = len(palavras)


if num_palavras >= 7 and num_palavras <= 10:
    print("Slogan adequado (número de palavras está bom).")
else:
    print("Slogan inadequado (número de palavras está errado).")


if slogan[0].isalpha() and slogan[-1].isalpha():
    print("Slogan adequado (começa e termina com letra).")
else:
    print("Slogan inadequado (não começa e termina com letra).")


if palavra_chave in slogan and num_palavras >= 7 and num_palavras <= 10 and slogan[0].isalpha() and slogan[-1].isalpha():
    print(f'O slogan "{slogan}" está bom para o produto "{produto}".')
