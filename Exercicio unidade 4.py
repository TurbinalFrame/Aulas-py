"""
velocidade = int(input("Qual velocidade você estava?\n "))

if velocidade <= 80:
    print("Voce nao foi multado")
elif velocidade > 80:
    print(f"Voce foi multado\nO valor a ser pago sera de:\nR${(velocidade - 80) * 7:.2f}")
 
########################################################################################################    
velocidade = int(input("Qual velocidade você estava?\n "))

if velocidade <= 80:
    print("Voce nao foi multado")
else:
    print(f"Voce foi multado\nO valor a ser pago sera de:\nR${(velocidade - 80) * 7:.2f}")
    
""" 
"""
numero = int(input("Escreva um numero:\n "))

if numero % 2 == 0:
    print("O numero e PAR")
else:
    print("O numero e IMPAR")
"""
"""
distancia = float(input("Escreva a distancia da viagem:\n"))

if distancia <= 200:
    print(f"O total a pagar e R${distancia * 0.50:.2f}")
elif distancia > 200:
    print(f"O total a pagar e R${distancia * 0.45:.2f}")
    
print("Fim da consulta")

"""
"""
salario = float(input("Qual o salario do colaborador?\n"))

if salario > 1250:
    print(f"O salario tera aumento de 10%.\nO salario sera de:\n{salario + (salario * 0.1)}")
elif salario <= 1250:
    print(f"O salario tera aumento de 15%.\nO salario sera de:\n {salario + (salario * 0.15)}")
    
print("Fim da consulta")

"""

"""
import math

num = float(input("Insira um numero:\n"))
if num < 0:
    print("numero invalido!!\nColoque um numero positivo")
else:
    raiz = math.sqrt(num)
    print(f"A raiz do numero que foi colocado é:\n{raiz:.2f}")
   
"""

"""

# Um teste para ver se eu conseguia colocar em laço de repetição...
#No caso tenho que colocar o while com valor boolean e sinalizar que acabou o laço com o "break"

import math


while True:
    num = float(input("Insira um numero:\n"))
    if num < 0:
        print("numero invalido!!\nColoque um numero positivo")
    else:
        break
if num >= 0:
    raiz = math.sqrt(num)
    print(f"A raiz do numero que foi colocado é:\n{raiz:.2f}") 
    
print("Fim do programa")

"""

"""
lado1 = int(input("Escreva a primeira reta:\n"))
lado2 = int(input("Escreva a segunda reta:\n"))
lado3 = int(input("Escreva a terceira reta:\n"))

if lado1 + lado2 < lado3:
    print("Nao e possivel formar um triangulo")
elif lado1 + lado3 < lado2:
    print("Nao e possivel formar um triangulo")
elif lado2 + lado3 < lado1:
    print("Nao e possivel formar um triangulo")
else:
    print("E possivel formar um triangulo")
    
print("Fim do programa")
"""

'''
controle = int(input("""
                     
Qual operacao voce deseja uetilizar?                     

[1] - Soma
[2] - subtracao
[3] - multiplicacao
[4] - divisao                    
"""))

if controle == 1:
    soma1 = float(input("Escreva um numero a ser somado:\n"))
    soma2 = float(input("Escreva outro numero a ser somado com o primeiro:\n"))
    print(f"O resultado e:\n{soma1 + soma2}")
elif controle == 2:
    sub1 = float(input("Escreva um numero a ser subtraido:\n"))
    sub2 = float(input("Escreva o segundo numero a ser subtraido:\n"))
    print(f"A subtracao e:\n{sub1 - sub2}")
elif controle == 3:
    mult1 = float(input("Escreva um numero a ser multiplicado:\n"))
    multi2 = float(input("Escreva o segundo numero a ser multiplicado:\n"))
    print(f"A multiplicacao deu:\n{mult1 * multi2}")
elif controle == 4:
    divi1 = float(input("Escreva um numero a ser divido:\n"))
    divi2 = float (input("Escreva o numero que ira divir o de cima\n"))
    print(f"O resultado da divisao e:\n{divi1 // divi2}")
else:
    print("O numero de opcao que voce colocou nao atende ao menu de selecao")

print("Fim do programa")

'''

"""
valor1 = int(input("Escreva um valor:\n"))
valor2 = int(input("Escreva um valor:\n"))

if valor1 > valor2:
    print(f"O {valor1} e maior que o {valor2}\nA diferença deles e de:\n{valor1 - valor2}")
elif valor2 > valor1:
    print(f"O {valor2} e maior que o {valor1}\nA diferença deles e de:\n{valor2 - valor1}")
else:
    print(f"O {valor1} e o {valor2} sao iguais")
    
print("Fim")
"""

"""
v__casa = float(input("Qual o valor da casa?\n"))
salario = float(input("Qual o seu salario?\n"))
tempo_pg = float(input("Em quantos anos voce pretende pagar?\n"))
temp_pg_m = 12 * tempo_pg 

if v__casa // (tempo_pg * 12) > salario * 0.3:
    print("O emprestimo NAO foi aprovado")
else:
    print("O emprestimo FOI aprovado")

print("FIM")

"""
'''
valor_prod = float(input("Digite o valor do produto:\n"))
controlador = str(input("""
                        
Digite o estado que o produto sera enviado
[MG]                        
[SP]
[RJ]
[MS]

Escreva aqui a sigla do estado:\n

"""))

if controlador == str("MG" or "mg"):
    print(f"O valor que o cliente ira pagar sera de:\n{valor_prod + (valor_prod * 0.07):.2f}")
elif controlador == str("SP" or "sp"):
    print(f"O valor que o cliente ira pagar sera de:\n{valor_prod + (valor_prod * 0.12):.2f}")
elif controlador == str("RJ" or "rj"):
    print(f"O valor que o cliente ira pagar sera de:\n{valor_prod + (valor_prod * 0.15):.2f}")
elif controlador == str("MS" or "ms"):
    print(f"O valor que o cliente ira pagar sera de:\n{valor_prod + (valor_prod * 0.08):.2f}")
else:
    print("Estado invalido, escreva apenas um das opcoes acima")
    
print("FIM")

'''

'''
valor_a_pagar = float(input("Qual o valor a ser pago?\n"))
controlador = int(input(""" 

[1] - A vista no dinheiro                        
[2] - A vista no cartao
[3] - Parcelado
"""))

if controlador == 1:
    print(f"Nesse meio de pagamento, tera desconto de 10%OFF\nO valor total:\nR${valor_a_pagar - (valor_a_pagar * 0.10):.2f}")
elif controlador == 2:
    print(f"Nesse meio de pagamento, tera desconto de 5%OFF\nO valor total:\nR${valor_a_pagar - (valor_a_pagar * 0.05):.2f}")
elif controlador == 3:
    Xnocard = int(input("Quantas vezes irá parcelar?\n"))
    if Xnocard == 2:
        print(f"O valor total fica:\nR${valor_a_pagar}")
    else:
        print(f"Por conta do parcelamento, o valor do produto tera 20% de juros\nTotal:R${valor_a_pagar + (valor_a_pagar * 0.2):.2f}")
else:
    print("Opcao invalida, escolha uma das opcoes")
    
print ("FIM")

'''

'''
altura = float(input("Qual sua altura em metros?\n"))
sexo = int(input(""" 

Qual seu sexo?

[1] - Masculino
[2] - Feminino

"""))

if sexo == 1:
    print(f"O seu peso ideal e:\n{(72.7 * altura) - 58:.2f}")
elif sexo == 2:
    print(f"O seu peso ideal e:\n {(62.1 * altura) - 44.7:.2f}")
else:
    print("Escolha uma opcao valida")
print("FIM")

'''