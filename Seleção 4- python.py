"""
nm1 = "Vinicius"
nm2 = "Beatriz"


print(f"dado 1:\n{type(nm1)}\nDado 2:\n{type(nm2)}")
print(nm1 != nm2 )  
if nm1 == nm2:
    print("Os nomes são iguais")

if nm1 != nm2:
    print("Os nomes sao diferentes")
    
if type(nm1) == type(nm2):
    print("Os dados são iguais")

if type(nm1) != type(nm2):
    print("Os dados são diferente")
    
print("Fim do programa")
"""
"""
valor1 = 19
valor2 = 19

if valor1 > valor2:
    print(f"{valor1} e maior que {valor2}")
    
else:
    print(f"{valor1} e menor que {valor2}")
    if valor1 == valor2:
        print("Os dois valores sao iguais")
    if valor1 == 10:
        print(f"Alguem tirou 10!")
    else:
        print(f"Nao me importo mais com os resultados")

print("Fim do Programa")

"""
"""
valor1 = 19
valor2 = 1

print(f"Valor 1: {valor1}\nValor 2: {valor2}")

if valor1 == valor2:
    print(f"Os valores sao iguais")
elif valor1 > valor2:
    print("Valor e maior")
elif valor1 < valor2:
    print("Valor menor")
    
else:
    print("Os valores sao diferentes")
print("FIM DO PROGRAMA, CARO GAFANHOTO")

"""
"""
valor = int(input("Insira um valor:\n"))

if valor % 2 == 0:
    print(f"O valor {valor} é PAR")
else:
    print(f"O valor {valor} e IMPAR")
"""

"""
nome = str(input("Insira sua nome:\n"))
idade = int(input("Inisra sua idade:\n"))
peso = float(input("Insira seu peso:\n"))

if nome == "Vinicius" or "vinicius":
    print("Prazer te ver aqui novamente")
else:
    print("Nome registrado com sucesso")
print(f"Seja bem vindo {nome}")

print(f"Idade registrada com sucesso")
if idade >= 18:
    print("Voce e maior de idade")
else:
    print("voce e menor de idade")

if peso < 85:
    print("Voce esta com um peso legal... dependendo da sua altura")
elif peso > 130:
    print("TA PESADO HEIN??")
else:
    print("Ta precisando treinar")
"""

controle = int(input("""
                      
Escolha o tipo de dado que vc quer:                       
                      
[1] - Int                       
[2] - Float                    
[3] - String                    
[4] - Boolean                                       
                      
"""))
if controle == 1:
    dado1 = int(input("Insira seu numero:\n"))
elif controle == 2:
    dado1 = float(input("Insira seu numero:\n"))
elif controle == 3:
    dado1 = str(input("Insira sua mgs:\n"))
elif controle == 4:
    dado1 = bool(input("Insira seu valor:\n"))
    
    
    
controle = int(input("""
                      
Escolha o tipo de dado que vc quer para comparar com o dado 1:                      
                      
[1] - Int                       
[2] - Float                    
[3] - String                    
[4] - Boolean                                         
                      
"""))
if controle == 1:
    dado2 = int(input("Insira seu numero:\n"))
elif controle == 2:
    dado2 = float(input("Insira seu numero:\n"))
elif controle == 3:
    dado2 = str(input("Insira sua mgs:\n"))
elif controle == 4:
    dado2 = bool(input("Insira seu valor:\n"))
 
print(f"Tipo1:      {type(dado1)}           Tipo2:       {type(dado2)}")    
if type(dado1) == type(dado2):
    print("Sao iguais")
else:
    print("Sao diferentes")