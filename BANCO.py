menu = """

DEPOSITO Depositar
SACAR Sacar
EXTRATO Extrato
SAIR Sair

=> """

saldo = 0
limite = 1000
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).upper()

    if opcao =='DEPOSITO':
        valor = float(input("INFORME O VALOR: "))

        if valor > 0:
            saldo += valor
            extrato += f"DEPÓSITO DE: R$ {valor:.2f}\n"
        else:
            print("NÃO FOI POSSIVEL REALIZAR A OPERAÇÃO")
    
    elif opcao == 'SACAR':
        valor = float(input("INFORME O VALOR A SER RETIRADO: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("OPERAÇÃO NÃO CONCLUÍDA!! O VALOR É MAIOR QUE O SALDO EXISTENTE")
        
        elif excedeu_limite:
            print("OPERAÇÃO NÃO CONCLUÍDA!! O VALOR DO SAQUE EXCEDE O LIMITE") 

        elif excedeu_saques:
            print("OPERAÇÃO FALHOU!! NÚMERO DE SAQUES ESGOTADOS")

        elif valor > 0:
            saldo -= valor
            extrato += f"SAQUE DE: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("O VALOR INSERIDO ESTÁ INVÁLIDO")

    elif opcao == "EXTRATO":
        print("\n================ EXTRATO ================")
        print("NÃO HOUVERAM MOVIMENTAÇÕES" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "SAIR":
        break

    else:
        print("ALGO NÃO ESTÁ CORRETO")
