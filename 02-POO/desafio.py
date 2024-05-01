import textwrap
from datetime import datetime
import os


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y")
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        if len(self.historico.transacoes) >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"Agência:\t{self.agencia}\nC/C:\t\t{self.numero}\nTitular:\t{self.cliente.nome}"


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


class Transacao:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        raise NotImplementedError(
            "Método registrar deve ser implementado nas subclasses.")


class Saque(Transacao):
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    menu_text = """\n=============== MENU ================
    [d]     Depositar
    [s]     Sacar
    [e]     Extrato
    [nc]    Nova conta
    [lc]    Listar contas
    [nu]    Novo usuário
    [q]     Sair
    => """
    return input(textwrap.dedent(menu_text))


def encontrar_cliente_por_cpf(cpf, clientes):
    return next((cliente for cliente in clientes if cliente.cpf == cpf), None)


def selecionar_conta(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None

    # Simplesmente retorna a primeira conta do cliente, pode ser expandido para escolha
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = encontrar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = selecionar_conta(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = encontrar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = selecionar_conta(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = encontrar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = selecionar_conta(cliente)
    if conta:
        print("\n================ EXTRATO ================")
        transacoes = conta.historico.transacoes

        if not transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in transacoes:
                print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f}")

        print(f"Saldo: R$ {conta.saldo:.2f}")
        print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    if encontrar_cliente_por_cpf(cpf, clientes):
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = encontrar_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    cliente.adicionar_conta(conta)
    print("\n=== Conta criada com sucesso! ===")


def listar_contas(clientes):
    for cliente in clientes:
        for conta in cliente.contas:
            print("=" * 50)
            print(str(conta))


def main():
    clientes = []

    while True:
        opcao = menu()
        os.system("cls")

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(clientes) + 1 
            criar_conta(numero_conta, clientes)
        elif opcao == "lc":
            listar_contas(clientes)
        elif opcao == "q":
            break
        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()
