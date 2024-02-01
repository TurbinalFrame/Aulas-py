def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

# Exemplos de uso
num1 = 10
num2 = 5

print(f"Soma: {adicao(num1, num2)}")
print(f"Subtração: {subtracao(num1, num2)}")
print(f"Multiplicação: {multiplicacao(num1, num2)}")
print(f"Divisão: {divisao(num1, num2)}")
