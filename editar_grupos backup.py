import json

def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo_dados_alunos_json:
            dados_alunos = json.load(arquivo_dados_alunos_json)
    except FileNotFoundError:
        # Se o arquivo não existir, cria uma estrutura vazia
        dados_alunos = {
            "alunos": {},
            "turmas": {},
            "ciclos": {},
            "grupos": {},
            "notas": {}
        }
    return dados_alunos

def editar_grupo():
    dados_alunos = carregar_dados()
    grupo_id = input("Informe o ID do grupo a ser editado: ")
    if grupo_id in dados_alunos['grupos']:
        grupo = dados_alunos['grupos'][grupo_id]
        print(f'Editando dados do grupo ID: {grupo_id}')
        while True:
            print(f'1 - Nome: {grupo["Nome"]}')

            campo = input('Escolha o campo que deseja editar (1), 2 para cancelar ou 3 para salvar: ')
            if campo == '1':
                grupo['Nome'] = input('Novo Nome: ')
            elif campo == '2':
                break
            elif campo == '3':
                dados_alunos['grupos'][grupo_id] = grupo
                with open('dados.json', 'w') as arquivo_json:
                    json.dump(dados_alunos, arquivo_json, indent=4)
                print('Cadastro atualizado com sucesso.')
                return True
            else:
                print('Opção inválida. Tente novamente.')
        if campo != '2':
            print('Cadastro atualizado com sucesso.')
            return False
    else:
        print(f'O grupo com ID {grupo_id} não foi encontrado.')
        return False

# Se você desejar que este arquivo possa ser usado em outros contextos, pode ser necessário ajustar o nome do arquivo onde os dados são salvos ('dados.json') e a estrutura do arquivo 'dados.json' de acordo com o seu sistema.
