import conta

while True: 
    conta.limpar_tela()
    print ("Calculadora")

    print("----------------------------------------------------------------------")
    print("-----------------------ESCOLHA UMA OPÇÃO------------------------------")
    print("----------------------------------------------------------------------")
    print("\nEscolha:")
    print("[1] SOMA ")
    print("[2] SUBTRAÇÃO ")
    print("[3] MULTIPLICAÇÃO ")
    print("[4] DIVISÃO ")

    opcao = int(input("Digite o número da operação: "))

    conta.os.system("cls")

    n1 = conta.obter_Valor1()
    n2 = conta.obter_Valor2()

    if opcao == 1:
        resultado = conta.calculo_adicao (n1, n2)

    elif opcao == 2:
        resultado = conta.calculo_subtracao(n1, n2)

    elif opcao == 3:
        resultado = conta.calculo_multiplicacao(n1, n2)
    
    elif opcao == 4:
        resultado = conta.calculo_divisao(n1, n2)

    else:
        print("Opção inválida. Escolha entre 1 a 4.")

    input("Pressione <Enter> para continuar ...")