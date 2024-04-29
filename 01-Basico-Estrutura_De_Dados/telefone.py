import re

def validate_numero_telefone(phone_number):
    # Definir o padrão de expressão regular para validar números de telefone no formato (XX) 9XXXX-XXXX
    pattern = r"\(\d{2}\) 9\d{4}-\d{4}"
    
    # Verificar se o padrão corresponde ao número de telefone fornecido
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicitar ao usuário que insira um número de telefone
phone_number = input()

# Chamar a função validate_numero_telefone() com o número de telefone fornecido como argumento
result = validate_numero_telefone(phone_number)

# Imprimir o resultado da validação
print(result)
