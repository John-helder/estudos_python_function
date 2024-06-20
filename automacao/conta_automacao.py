
def exibir_menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova conta
    [l] Listar Contatos
    [u] Novo Usuário
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Deposito realizado!")
        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou. Você não tem saldo suficiente!")
    elif excedeu_limite:
        print("Operação falou. O valor de saque excedeu o limite")
    elif excedeu_saques:
        print("Operação falho. Você excedeu o numero de saques permitidos")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Falha na operação. Valor inválido")
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def novo_usuario(usuarios):
    cpf = input("Digite seu CPF (Somente Número): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("CPF já cadastrado")
        return
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento no formato(DD-MM-AA): ")
    endereco = input("Informe seu endereço: (Logradouro - nº - Cidade/Sigla estado) ")

    usuarios.append({"nome" : nome, "data_nascimento":data_nascimento, "endereco":endereco})

    print("usuário criado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe seu CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuarios":usuario}
    
    print("Usuário não encontrado. Criação de conta encerrada!")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                limite=limite,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            extrato(saldo, extrato=extrato)
        
        elif opcao == "u":
            novo_usuario(usuarios)
        
        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")