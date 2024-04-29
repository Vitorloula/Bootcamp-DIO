class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self):
        return self.__salario

    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas

    def registra_hora_trabalhada(self, horas=1):
        if horas > 0:
            self.__horas_trabalhadas += horas
        else:
            raise ValueError("O número de horas trabalhadas deve ser maior que zero.")

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

    def reset_horas_trabalhadas(self):
        self.__horas_trabalhadas = 0

    def __str__(self):
        return f"Funcionário: {self.nome}\nCargo: {self.cargo}\nSalário: R${self.salario:.2f} \n"

# Exemplo de uso:
if __name__ == "__main__":
    funcionario = Funcionario('Pedro', 'Gerente de Vendas', 50)
    funcionario2 = Funcionario('João', 'Caixa', 35)
    print(funcionario)
    print(funcionario2)

    funcionario.registra_hora_trabalhada(40)
    funcionario.calcula_salario()
    print(funcionario)

    funcionario2.registra_hora_trabalhada(50)
    funcionario2.calcula_salario()
    print(funcionario2)

    # Resetar horas trabalhadas
    funcionario.reset_horas_trabalhadas()
    print("Horas trabalhadas resetadas.")

    funcionario.registra_hora_trabalhada(10)
    funcionario.calcula_salario()
    print(funcionario)
