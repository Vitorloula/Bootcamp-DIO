import os

def menu():
    """
    Exibe o menu principal do sistema e solicita uma opção ao usuário.

    Returns:
        str: A opção escolhida pelo usuário.
    """
    menu = """\n
    ================ MENU ================
    [d]     Depositar
    [s]     Sacar
    [e]     Extrato
    [nc]    Nova conta
    [lc]    Listar contas
    [nu]    Novo usuário
    [q]     Sair
    ======================================
    => """
    return input(menu)

def depositar(valor, extrato, saldo):
    """
    Realiza um depósito na conta.

    Args:
        valor (float): O valor a ser depositado.
        extrato (str): O extrato da conta onde será registrada a operação.
        saldo (float): O saldo atual da conta.

    Returns:
        tuple: Uma tupla contendo o novo extrato e o novo saldo após o depósito.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("--- Depósito realizado com sucesso ---")
        return extrato, saldo
    else: 
        print("Depósito não realizado, valor inválido")

def sacar(valor, extrato, saldo, numero_saques, limite_saque, limite):
    """
    Realiza um saque na conta.

    Args:
        valor (float): O valor a ser sacado.
        extrato (str): O extrato da conta onde será registrada a operação.
        saldo (float): O saldo atual da conta.
        numero_saques (int): O número de saques já realizados.
        limite_saque (int): O limite máximo de saques permitidos.
        limite (float): O limite de saque permitido por operação.

    Returns:
        tuple: Uma tupla contendo o novo extrato, novo saldo e número de saques após o saque, se bem-sucedido.
    """
    if valor > 0 and valor <= saldo and numero_saques < limite_saque and valor <= limite:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("------ Saque realizado com sucesso ------")
        return extrato, saldo, numero_saques
    else:
        print("Saque não realizado, operação inválida")

def exibir_extrato(extrato, saldo):
    """
    Exibe o extrato e o saldo da conta.

    Args:
        extrato (str): O extrato da conta.
        saldo (float): O saldo atual da conta.
    """
    print("================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuarios(cpf, usuarios):
    """
    Filtra usuários por CPF.

    Args:
        cpf (str): O CPF a ser pesquisado.
        usuarios (list): Lista de usuários cadastrados.

    Returns:
        dict or None: O usuário encontrado ou None se não for encontrado.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def novo_usuario(usuarios):
    """
    Cadastra um novo usuário.

    Args:
        usuarios (list): Lista de usuários cadastrados.
    """
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuarios(cpf=cpf, usuarios=usuarios)

    if usuario:
        print("Usuário já existente")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def nova_conta(numero_conta, agencia, usuarios):
    """
    Cria uma nova conta bancária.

    Args:
        numero_conta (int): Número da conta a ser criada.
        agencia (str): Número da agência da conta.
        usuarios (list): Lista de usuários cadastrados.

    Returns:
        dict or None: Dicionário representando a nova conta criada ou None se não puder ser criada.
    """
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuarios(cpf=cpf, usuarios=usuarios)

    if usuario:
        print("Conta criada com sucesso !")
        return {"numero_conta": numero_conta, "agencia": agencia, "usuario": usuario}

    print("Erro ao criar a conta")

def listar_contas(contas):
    """
    Lista todas as contas bancárias cadastradas.

    Args:
        contas (list): Lista de contas bancárias.
    """
    print("======= LISTA DE CONTAS =======")
    for conta in contas:
        linha = f"""\
            C/C:     {conta['numero_conta']}
            Agência: {conta['agencia']}
            Titular: {conta['usuario']['nome']}
        """
        print(linha)
    print("================================")

def main():
    """
    Função principal que executa o sistema bancário.
    """
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        os.system("cls")  # Limpa a tela do console (para Windows)

        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))
            extrato, saldo = depositar(valor=valor, extrato=extrato, saldo=saldo)

        elif opcao == "s":
            valor = float(input("Informe o valor a ser sacado: "))
            resultado_saque = sacar(valor=valor, extrato=extrato, saldo=saldo, 
                                    numero_saques=numero_saques, limite_saque=LIMITE_SAQUES, limite=limite)
            if resultado_saque is not None:
                extrato, saldo, numero_saques = resultado_saque
        
        elif opcao == "e":
            exibir_extrato(extrato, saldo)
        
        elif opcao == "nu":
            novo_usuario(usuarios=usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = nova_conta(numero_conta=numero_conta, agencia=AGENCIA, usuarios=usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
main()