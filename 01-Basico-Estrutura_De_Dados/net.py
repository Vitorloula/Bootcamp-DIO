def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50 Mbps"
    elif consumo > 10 and consumo <= 20:
        return "Plano Prata Fibra - 100 Mbps"
    else:
        return "Plano Premium Fibra - 300 Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo_mensal = float(input("Insira o seu consumo médio mensal (em GB): "))

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo_mensal))

