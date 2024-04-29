class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BiBiBi")

    def parar(self):
        print("Bicicleta Parada")
    
    def correr(self):
        print("Vrummm")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor 
                                                        in self.__dict__.items()])}"
    

b1 = Bicicleta("Vermelha","Venzo","2022","2300")

print(b1)

b1.buzinar()
b1.correr()
b1.parar()