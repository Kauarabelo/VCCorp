import json
from editar_ciclos import editar_ciclo


def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        dados = {
            "alunos": {},
            "turmas": {},
            "ciclos": {},
            "grupos": {},
            "notas": {}
        }
    return dados

# Função para verificar se um ciclo já existe nos dados
def ciclo_existe(id_ciclo, dados):
    return id_ciclo in dados['ciclos']

# Função para cadastrar ciclos
def func_cadastrar_ciclos():
    dados = carregar_dados()

    # Pergunta em qual turma deseja acrescentar um ciclo
    id_turma = input('Informe o ID da turma em que deseja adicionar um ciclo: ')

    # Verifica se a turma existe nos dados
    if id_turma not in dados['turmas']:
        print('A turma com este ID não existe. Crie a turma antes de vincular o ciclo.')
        return False
    
    # Verifica se a turma já tem ciclos
    if 'ciclos' in dados['turmas'][id_turma]:
        print('Ciclos já vinculados à turma:')
        for ciclo in dados['turmas'][id_turma]['ciclos']:
            print(f'ID: {ciclo["ID"]}, Nome: {ciclo["Nome"]}')
    else:
        print('A turma ainda não possui ciclos vinculados.')

    while True:
        id_ciclo = input('Informe o ID do ciclo a ser cadastrado: ')

        # Verifica se o ciclo já existe nos dados
        if ciclo_existe(id_ciclo, dados):
            print('O ciclo com este ID já está cadastrado.')
            opcao = input('O que deseja fazer?\n1 - Criar um novo ciclo\n2 - Editar os dados do ciclo\n')
            if opcao == '1':
                continue
            elif opcao == '2':
                editar_ciclo(id_ciclo, dados)
                return False

        nome_ciclo = input('Qual o nome do ciclo? ')
        data_inicio = input('Qual a data de início do ciclo? ')
        data_fim = input('Qual a data de fim do ciclo? ')
        peso_nota = input('Qual o peso da nota do ciclo? ')

        novo_ciclo = {
            'ID': id_ciclo,
            'Nome': nome_ciclo,
            'Data de Início': data_inicio,
            'Data de Fim': data_fim,
            'Peso da Nota': peso_nota,
        }

        # Adiciona o ciclo à lista de ciclos da turma
        if 'ciclos' not in dados['turmas'][id_turma]:
            dados['turmas'][id_turma]['ciclos'] = []
        dados['turmas'][id_turma]['ciclos'].append(novo_ciclo)

        dados['ciclos'][id_ciclo] = novo_ciclo
        with open('dados.json', 'w') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        print('Cadastro do ciclo realizado com sucesso e vinculado à turma.')
        return True
