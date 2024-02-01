"""

nome = str(input("Escreva um nome\n")).strip()

print(f"O {nome} tem {len(nome) - nome.count(' ')} letras no nome")

"""

"""c:\Users\pache\VSCODE\aulas python\modulo 5.py
nome = "Vinicius"
print(nome.isalpha())

"""


"""
nome = "Vinicius"
print(nome[0:7:2])
#[::] - isso significa que, mostrar de tal até tal de quanto em quanto. 
#[0:5:1]- isso significa que mostrar da primeira até a quinta de uma em uma.

nome2 = "vinicius"
print(nome[::-1])
#Quando colocado em o -1 é colocar de trás para frente

"""

# .split() serve para separar de forma de indexação
nome = str(input("Insira seu nome:\n")).strip().split()
#print(f"Prazer em te conhecer {nome}")
print(f"O primeiro nome é {nome[0]}", end=' ')
print(f"O ultimo nome é {nome[len(nome) - 1]}")
print(f"O nome do meio  é {nome[len(nome) - 2]}")