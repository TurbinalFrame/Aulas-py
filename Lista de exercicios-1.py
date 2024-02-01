"""
Hello = "ola mundo"
print(f"{Hello}")

print("Ola mundo")

nome = "Vinicius"
idade = 23
peso = 121.8

print(f"Ola, meu nome é {nome}\nTenho {idade} anos\nPeso {peso}Kg.")

numero = int(input("Coloque um numero: "))
antes = numero - 1
depois = numero + 1

print(f"O numero que foi inserido e: {numero}\nO numero que vem antes e: {antes}\n o numero que vem depois e: {depois}")


#OU

valor = int(input("Insira um valor:\n"))
print(f"O valor inserido foi:\n{valor}\nSeu antecessor e {valor - 1} e seu sucessor é {valor + 1}")


"""
"""
import math

num = float(input("Insira um numero: "))
dobro =  num * 2 
triplo = num * 3
raiz = math.sqrt(num) 

print(f"o numero digitado foi: {num}\nSeu dobro e: {dobro}\nSeu triplo e: {triplo}\nE sua raiz e: {raiz}")

"""

"""
ano_nascimento = int(input("qual o ano de seu nascimento "))
idade = 2024 - ano_nascimento 

print(f"voce tem ou ira fazer:\n{idade} anos")


ano_nascimento = int(input("qual o ano de seu nascimento "))

print(f"voce tem ou ira fazer:\n{2024 - idade} anos")

"""
"""
valor = float(input("qual valor do produto? "))
#ou pode ser colocado assim desconto = valor - (valor * 25 / 100)  assim elimina as duas linhas de baixo e já pode passar para o print
desconto = (valor * 25 / 100)
valor_desconto = valor - desconto

print(f"O valor do produto é de {valor} reais\nDesconto de 25% vai para {valor_desconto} reais")

OU

produto = float(input("insira o preço do produto:\n"))
print(f"O valor com desconto de 25% fica:\n{produto - produto * (25/100):.2f}")

"""
"""
salario = float(input("qual valor do salario? "))
porcent_aumento = float(input("qual a porcentagem de aumento? "))
calc_aumento = salario + (salario * porcent_aumento / 100)

print(f"Seu salario vai para {calc_aumento:.2f} reais")


Ou 


salario = float(input("Qual o salario?\n"))
print(f"O salario e {salario}, com aumento de 75% fica:\n{salario + salario * 75/100}")


"""
"""
#Leia um valor e imprima sua tabuada de multiplicação na tela

num = int(input("escreva um numero de 0 a 9: "))
tabuada = num * 1, num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10

print(f"A tabuada do valor que vc colocou e:\n{tabuada}")

#ou colocar um print para cada valor e tirar a variavel
"""

"""
num1 = int (input("escreva qualquer valor ou numero:\n"))
num2 = float (input("escreva qualquer valor ou numero:\n"))
num3 = 4.3
num4 = 5

print(f"O valor 1 e: {num1}\nO valor 2 e: {num2}")
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
"""
"""
Km_percorrido = float(input("Quantos KM rodou com o carro?\n"))
Dias_com_carro = int(input("Quantos dias ficou com o carro?\n"))

calc_km = Km_percorrido * 0.15
calc_dia = Dias_com_carro * 60
calc_total = calc_dia + calc_km

print(f"Você ficou com o carro:\n{Dias_com_carro} dias\nVoce andou com o carro:\n{Km_percorrido}Km")
print(f"O valor do dia do carro e 60 reais e por Km rodado e 0,15 reais")
print("Calculando...")
print(f"O dia ficou: {calc_dia}\nO valor da quilometragem ficou: {calc_km}\nTotal a pagar: {calc_total}")

"""

import datetime

d2 = datetime.datetime.strptime('2024-01-12', '%Y-%m-%d')

#d1 = input(datetime.strptime("Insira a data de seu nasciemnto ano/mes/dia", "%Y-%m-%d"))

d1_str = input("Insira a data de seu nascimento ano/mes/dia (no formato YYYY-MM-DD): ")
d1 = datetime.datetime.strptime(d1_str, "%Y-%m-%d")

diferenca = d2 - d1
anos, dias_restantes = divmod(diferenca.days, 365)
meses, _ = divmod(dias_restantes, 30.44)  # considerando a média de 30.44 dias por mês

Quantidade_de_dia = diferenca.days

print(f"Você tem {int(anos)} anos, {int(meses)} meses e {int(dias_restantes)} dias de vida, o que equivale a {Quantidade_de_dia} dias.")

#Quantidade_de_dia = abs((d2-d1).days)

#print(f"Seus dias vivo sao {Quantidade_de_dia}")




idade = int(input("insira a sua idade\n"))
meses = 12 * idade 
dias = 30.5 * meses 
print(f"Minha idade e {idade} anos")
print(f"Tenho {meses} meses de vida")
print(f"Logo tenho {dias} dias de vida")



"""
valor_total = 780
G1 = 780000 * 0.46
G2 = 780000 * 0.32
G3 = 780000 - (G1 + G2)

print(f"O PRIMEIRO ganhador levara para casa a quantia de R${float(G1):.2f} Reais")
print(f"O SEGUNDO ganhador levara para casa a quantia de R${float(G2):.2f} Reais")
print(f"O TERCEIRO ganhador levara para casa a quantia de R${float(G3):.2f} Reais")

"""
"""
Temp_C = int(input("Qual a temperatura de hoje?\n"))
Conv_F = Temp_C * (9/5)+32

print(f" Temperatura em Fahrenheit:\n{Conv_F}ºF")
"""
"""
altura = float(input("Escreva a altura em metros:\n"))
largura = float(input("escreva a largura em metros:\n"))
calculo_area  = altura * largura

L_tinta = calculo_area / 2

print(f"Será necessario {L_tinta}L de tinta")

"""