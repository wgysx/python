def identificar_estado_cpf(cpf):
    cpf_numerico = ''.join(filter(str.isdigit, cpf))

    # Verifica se tem 11 dígitos
    if len(cpf_numerico) != 11:
        return "CPF INVÁLIDO"

    # Pega o nono dígito (índice 8)
    digito_estado = cpf_numerico[8]

    estados_por_digito = {
        '0': 'Rio Grande do Sul',
        '1': 'Distrito Federal, Goiás, Mato Grosso, Mato Grosso do Sul e Tocantins',
        '2': 'Pará, Amazonas, Acre, Amapá, Rondônia e Roraima',
        '3': 'Ceará, Maranhão e Piauí',
        '4': 'Pernambuco, Rio Grande do Norte, Paraíba e Alagoas',
        '5': 'Bahia e Sergipe',
        '6': 'Minas Gerais',
        '7': 'Rio de Janeiro e Espírito Santo',
        '8': 'São Paulo',
        '9': 'Paraná e Santa Catarina'
    }

    return f"O CPF informado é registrado em: {estados_por_digito[digito_estado]}"

cpf_usuario = input("Digite seu CPF (com ou sem pontuação): ")
resultado = identificar_estado_cpf(cpf_usuario)
print(resultado)
