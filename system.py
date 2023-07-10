menu = """

[d] Depositar
[s] Sacar
[e] Extract
[q] Sair

=> """

balance = 0
limit = 500
extract =  ""
number_withdrawals = 0 
LIMIT_WITHDRAWALS = 3

while True:

    option = input(menu)

    if option == "d":
        value = float(input("informe o valor do deposito: "))

        if value > 0:
            balance += value
            extract += f"Depósito: R$ {value:.2f}\n"
        
        else:
            print("Operação falhou! o valor informado é invalido.")

    elif option == "s":
        value = float(input("Informe o valor do saque: "))

        excedeu_balance = value > balance
        excedeu_limit = value > limit
        excedeu_saques = number_withdrawals >= LIMIT_WITHDRAWALS
       
        if excedeu_balance:
            print("Operação falhou! você não tem saldo sufuciente.")
        
        elif excedeu_limit:
            print("Operação falhou!, o valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou!, Número máximo de saques excedido.")

        elif value > 0:
            balance -= value
            extract += f"Saque: R$ {value:.2f}\n"
            number_withdrawals += 1
        
        else:
            print("Operação falhou! O valor informado é invalido.")

    elif option == "e":
        print("====================== Extrato ================================")
        print("Não foram realizadas movimentações." if not extract else extract)
        print(f"\nSaldo: R$ {balance:.2f}\n")
        print("===============================================================")

    elif option == "q":
       break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")