"""
Inteiros 123456789 -3 -34332

floats 2.9 3.14...

strings "tudo que esta dentro das aspas"

boolean true and false 0 = false 1 = true


Variaveis são espaços de alocamento na memória 

int float str bool
"""
nome = "Vinicius"
idade = 23
peso = 120.2

#print("Meu nome e", nome, "Minha idade e", idade ) [Forma antiga de usar]
#print(f"{nome} \n{idade} \n{peso}") 

#print("Ola, meu nome é {}, eu tenho {} anos, e estou com {} kg".format(nome, idade, peso))

#print(f"ola meu nome e {nome}, tenho {idade} anos e tenho {peso} kg")

pi = 3.14
part_inteira = int(pi)
texto_do_PI = str(part_inteira)
print(f"O valor de pi e {pi}\n a parte inteira e {part_inteira}")

print(type(pi))
print(type(part_inteira))
print(type(texto_do_PI))