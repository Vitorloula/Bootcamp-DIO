class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando moto")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
class carro(veiculo):
    pass


class Caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado  ):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado") 


class moto(veiculo):
    pass


caminhao = Caminhao("Vermelho", "885-334", "8", True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)