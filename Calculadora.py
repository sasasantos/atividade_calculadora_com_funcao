import funcao

while True: 
    funcao.limpar_tela()
    print ("                         CALCUADORA                                   ")

    print("------------------------------------------------------------------------")
    print("----------------------- ESCOLHA UMA OPÇÃO ------------------------------")
    print("------------------------------------------------------------------------")
    print("\nEscolha:")
    print("[1] SOMA ")
    print("[2] SUBTRAÇÃO ")
    print("[3] MULTIPLICAÇÃO ")
    print("[4] DIVISÃO ")

    opcao = int(input("Digite o número da operação: "))

    funcao.os.system("cls")

    n1 = funcao.obter_Valor1()
    n2 = funcao.obter_Valor2()

    if opcao == 1:
        resultado = funcao.calculo_adicao (n1, n2)

    elif opcao == 2:
        resultado = funcao.calculo_subtracao(n1, n2)

    elif opcao == 3:
        resultado = funcao.calculo_multiplicacao(n1, n2)
    
    elif opcao == 4:
        resultado = funcao.calculo_divisao(n1, n2)

    else:
        print("Opção inválida. Escolha entre 1 a 4.")

    input("Pressione <Enter> para continuar ...")