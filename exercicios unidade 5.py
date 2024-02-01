"""
nome = "Vinicius"
print(f"Nome em maiusculo {nome.upper()}\nEm minusculo {nome.lower()}")
print(f"O nome {nome} ao contrario e minusculo fica:\n{nome[::-1].lower()}")

nome1 = "Beatriz".lower()
print(f"O nome ao contario fica assim {nome1[::-1]}")


nome2 = "Vinicius Augusto Pacheco"
print(f"Nome em maiusculo {nome2.upper()}\nEm minusculo {nome2.lower()}")
print(f"ao todo o nome {nome2.capitalize()} tem {len(nome2) - nome2.count(' ') } letras")
print(f"O primeiro nome e {nome2.split()[0]} e tem {len(nome.split()[0])} letras")

texto = str(input("insira sua frase\n")).strip()

print(texto, "\n")
print(f"Na frase temos {texto.count(' ')} espacos vazios")
print(f" A vogal 'a' aparece {texto.count('a')} vezes na frase")
print(f" A vogal 'e' aparece {texto.count('e')} vezes na frase")
print(f" A vogal 'i' aparece {texto.count('i')} vezes na frase")
print(f" A vogal 'o' aparece {texto.count('o')} vezes na frase")
print(f" A vogal 'u' aparece {texto.count('u')} vezes na frase")



nome = str(input("insira seu nome\n")).strip().upper()
print(f"{nome}\n" * 5)


palavra = str(input("escreva sua palavra a verificar\n")).strip().lower()

if palavra == palavra[::-1]:
    print("É palindromo")
else:
    print("Nao e palindromo")
"""    

"""
name = str(input("Insira seu nome completo\n")).strip().split()
print(f"O nome completo e {name}")
print(f"O primeiro e o ultimo nome e {name[0]} {name[len(name) - 1]}")
print(f"O nome do meio e: {name[len(name) // 2]}")

"""

"""
nome = str(input("Escreva seu nome completo:\n")).strip()

print(f"Seu nome e {nome}")
print(f"O seu primeiro e ultimo nome e: {nome.split()[0] +' '+ nome.split()[len(nome.split()) - 1 ]}")
print(f"O nome do meio e: {nome.split()[len(nome.split()) // 2]}")

"""