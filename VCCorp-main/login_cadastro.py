# Dicionário para armazenar informações do usuário (login e senha)
usuarios = {}

def login():
    nome_login = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")

    if nome_login in usuarios:
        print("Nome de usuário já existe. Tente novamente.")
    else:
        usuarios[nome_login] = senha
        print("Conta criada com sucesso!")

def cadastro():
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

while True:
    print("\nEscolha uma opção:")
    print("1. Cadastrar usuário")
    print("2. Fazer login")
    print("3. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        login()
    elif opcao == "2":
        cadastro()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")
