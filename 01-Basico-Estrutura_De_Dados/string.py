import os 
MENU = """
    [d] Depositar 
    [s] Saque
    [e] Extrato
=> """

SALDO = 0 
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

while True:

    op = input(MENU)
    os.system("cls")
    if op == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0: 
            SALDO += valor
            EXTRATO += f"Deposito: R$ {valor:.2f}\n"

    elif op == "s":
        valor = float (input("Informe o valor do saque: "))
        excedeu_saldo = valor > SALDO
        excedeu_limite = valor > LIMITE
        excedeu_saques = NUMERO_SAQUES >= LIMITE_SAQUES

        if excedeu_saldo:
            print ("Operação falhou! Não saldo sucifiente")
        elif excedeu_limite:
            print ("Operação falhou ! Valor superior ao limite de saque")
        elif excedeu_saques:
            print ("Operação falhou ! Limite de saques execedido")
        elif valor > 0 :
            SALDO -= valor
            EXTRATO += f"Saque: R$ {valor:.2f}\n"
            NUMERO_SAQUES += 1
        else :
            print ("Operação falhou ! Valor informado é inválido")

    elif op == "e":
        print ("-------- Extrato --------")
        print ("Não foram realizadas movimentações. " if not EXTRATO else EXTRATO)
        print (f"\nSaldo: R$ {SALDO:.2f}")
        print ("-------------------------")
    elif op =="q":
        break
    else:
        print("Operação inválida, selecione a desejada")