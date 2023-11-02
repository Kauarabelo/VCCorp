import json

# Carregar os dados existentes do arquivo JSON (se existir)
try:
    with open('turmas.json', 'r') as arquivo_json:
        turmas = json.load(arquivo_json)
except FileNotFoundError:
    turmas = []

def cadastrar_turma():
    id_turma = input("Digite o ID da turma: ")
    data_inicio = input("Digite a data de início da turma: ")

    # Criar um dicionário com as informações da turma
    turma = {
        'id_turma': id_turma,
        'data_inicio': data_inicio,
        'alunos': []  # Inicialmente, a lista de alunos está vazia
    }

    # Adicionar a turma à lista de turmas
    turmas.append(turma)

    print(f"Turma '{id_turma}' criada com sucesso.")

# Exemplo de como salvar os dados em JSON
def relatorio_turmas():
    with open('turmas.json', 'w') as arquivo_json:
        json.dump(turmas, arquivo_json, indent=4)

