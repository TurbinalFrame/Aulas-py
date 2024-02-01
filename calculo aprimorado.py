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
        return "Divisao por 0"

num1 = 227
num2 = 5

print(f"SOMA : {adicao(num1, num2)} \nMENOS : {subtracao(num1, num2)} \nVEZES : {multiplicacao(num1, num2)} \nDIVIDIR : {divisao(num1, num2)}")