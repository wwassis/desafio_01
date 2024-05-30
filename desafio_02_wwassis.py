from math import e
import textwrap


def menu():
    menu = """\n
    =============================== MENU ===============================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ====================================================================
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /): #passado por posição
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n====== Depósito realizado com sucesso! ======")
    else:
        print("\n###### Operação falhou! O valor informado é inválido. ######")

    return saldo, extrato


def sacar(*,saldo, valor, extrato, limite_saque_dy, numero_saques, limite_de_saques):
    excedeu_saques = numero_saques >= limite_de_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_saque_dy
    
    if excedeu_saques:
        print("\n###### Operação falhou! Número máximo de saques diarios excedido. Você ja sacou: ",numero_saques , "vezes hoje!!! ######")

    elif excedeu_saldo:
        print("\n###### Operação falhou! Você não tem saldo suficiente. #######")
        print(f"\n****** Seu saldo atual é de R$  {saldo:.2f} ******")

    elif excedeu_limite:
        print("\n###### Operação falhou! O valor do saque excede o limite diaro. ######")
        print(f"\n***** Seu limite diario de saque é de R$ {limite_saque_dy:.2f} ")



    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        print("\n====== Saque realizado com sucesso! ======")
          

    else:
        print("\n###### Operação falhou! O valor informado é inválido. ######")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato): # posicional saldo / nomeado extrato
    print("\n=============================== EXTRATO ===============================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("//\\=================================================================//\\")


def criar_usuario(usuarios):
    cpf = input("Informe o número do seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n###### Já existe cadastro de usuário com esse CPF! ######")
        return

    nome = input("Informe o nome completo sem abreviações: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("====== Novo usuário criado com sucesso! ======")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n====== Conta criada com sucesso! ======")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n###### Usuário não encontrado, fluxo de criação de conta encerrado! ######")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    
    AGENCIA = "0001"
    qdade_saques = 3
    saldo = 0
    limite_saque_dy = 500.00
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Qual o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato) #passado por posição

        elif opcao == "s":
            valor = float(input("Qual o valor do saque: ")) # passagem por chave valor

            saldo, extrato, numero_de_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_saque_dy=limite_saque_dy,
                numero_saques=numero_de_saques,
                limite_de_saques=qdade_saques,
            )
            

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida, por favor selecione uma das opções válidas!!!.")


main()
