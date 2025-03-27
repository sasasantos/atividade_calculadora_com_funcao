import os

def limpar_tela():
    os.system("cls")

def obter_Valor1():
    return int(input("Digite um número: "))

def obter_Valor2():
    return int(input("Digite um número: "))


def calculo_adicao(numero1, numero2 ):
    resultado= numero1 + numero2
    print(f"Sua soma deu: {resultado}")

def calculo_subtracao(numero1, numero2 ):
    resultado = numero1 - numero2
    print (f"Sua subtração deu: {resultado}")

def calculo_multiplicacao(numero1, numero2 ):
    resultado=  numero1 * numero2
    print(f"Sua multiplicação deu: {resultado}")

def calculo_divisao(numero1, numero2 ):
    resultado = numero1 / numero2
    print(f"Sua divisão deu: {resultado}")





