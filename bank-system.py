menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Por favor, insira um valor válido.")

    elif opcao == "s":
        valor = float(input("Valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saque não realizado. Saldo insuficiente.")

        elif excedeu_limite:
            print("Saque não realizado. Valor limite excedido.")

        elif excedeu_saques:
            print("Limite de saques diários excedido. Tente novamente amanhã.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Por favor, informa um valor válido.")

    elif opcao == "e":
        print("\n#### EXTRATO ####")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###################")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.")