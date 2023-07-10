import textwrap

def menu():
    menu = """\n
    ================= MENU =================
    [d]\tDepositar
    [s]\tSacars
    [e]\tExtract
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(balance, value, extract, /):
    if value > 0:
        balance += value
        extract += f"Depósito: R$ {value:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")

    return balance, extract

def sacar(*, balance, value, extract, limit, number_withdrawals, LIMIT_WITHDRAWALS):
    excedeu_balance = value > balance
    excedeu_limit = value > limit
    excedeu_saques = number_withdrawals >= LIMIT_WITHDRAWALS
    
    if excedeu_balance:
        print("@@@ Operação falhou! você não tem saldo sufuciente. @@@")
    
    elif excedeu_limit:
        print("@@@ Operação falhou!, o valor do saque excede o limite. @@@")
    
    elif excedeu_saques:
        print("@@@ Operação falhou!, Número máximo de saques excedido. @@@")

    elif value > 0:
        balance -= value
        extract += f"Saque: R$ {value:.2f}\n"
        number_withdrawals += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("@@@ Operação falhou! O valor informado é invalido. @@@")
    
    return balance, extract

def exibir_extrato(balance, /, *, extract):
    print("====================== EXTRATO ================================")
    print("Não foram realizadas movimentações." if not extract else extract)
    print(f"\nSaldo: R$ {balance:.2f}\n")
    print("===============================================================")

def criar_usuario(users):
    cpf = input("Informe seu CPF (somente números): ")
    user = filtrar_usuario(cpf, users)

    if user:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereço = input("informe o endereço (logradouro, n - bairro - cidado/estado)")

    users.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, users):
    usuarios_filtrados = [user for user in users if user["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agency, number_account, users):
    cpf = input("Informe o CPF do usuário: ")
    user = filtrar_usuario(cpf, users)

    if user:
        print("\n=== Conta criada com sucesso! ===")
        return {"agency": agency, "number_account": number_account, "user": user}

    print("@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
def listar_contas(accounts):
    for account in accounts:
        line = f"""\
            Agência:\t{account['agencia']}
            c/c:\t\t{account['number_accounts']}
            Titular:\t\t{account['user']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))

def main():
    LIMIT_WITHDRAWALS = 3
    AGENCY = "0001"
    
    balance = 0
    limit = 500
    extract =  ""
    number_withdrawals = 0
    users = []
    accounts = []

    while True:

        option = menu()

        if option == "d":
            value = float(input("informe o valor do deposito: "))

            balance, extract = depositar(balance, value, extract)

        elif option == "s":
            value = float(input("Informe o valor do saque: "))

            balance, extract = sacar(
                balance=balance,
                value=value,
                extract=extract,
                limit=limit,
                number_withdrawals=number_withdrawals,
                LIMIT_WITHDRAWALS=LIMIT_WITHDRAWALS,
                )

        elif option == "e":
            exibir_extrato(balance, extract=extract)

        elif option == "nu":
            criar_usuario(users)

        elif option == "nc":
            number_account = len(accounts) + 1
            account = criar_conta(AGENCY, number_account, users)

            if account:
                accounts.append(account)

        elif option == "lc":
            listar_contas(accounts)

        elif option == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()