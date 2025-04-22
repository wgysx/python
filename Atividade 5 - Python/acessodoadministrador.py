def verificar_acesso(login, senha):
    # Verifica se o login e a senha estão corretos
    if login == "admin" and senha == "1234":
        return "Acesso Permitido"
    else:
        return "Acesso Negado"

login_usuario = input("Digite o login: ")
senha_usuario = input("Digite a senha: ")

print(verificar_acesso(login_usuario, senha_usuario))
