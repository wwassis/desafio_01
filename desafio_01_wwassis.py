from math import e

menu = """
    ###### OPERAÇÕES DISPONIVEIS ######

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    ###################################
    Qual a sua opção ==>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nvalor depositado de R$: {valor:.2f}")
            print(f"\nSeu saldo atual é de R$ {saldo:.2f}")

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque R$: "))
        print(f"\nSaque solicitado no valor de R$ {valor:.2f}\n")

        excedeu_limite = valor > limite
        
        excedeu_saldo = valor > saldo

        excedeu_saques = numero_saques >= LIMITE_SAQUES                

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite permitido.\n")
            print(f"Seu limite por saque é de: R$ {limite:.2f}")

        elif excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")
            print(f"Seu saldo atual: R$ {saldo:.2f}")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido no dia. Voce ja sacou:", LIMITE_SAQUES , "vezes hoje!!!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso no valor de R$: {valor:.2f}")
            print("\nRetire o dinheiro!!!")

        else:
            print("\nOperação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços bancários!!!")
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada válida.")
