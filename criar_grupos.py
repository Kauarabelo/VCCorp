import json
import cadastro_turma

# Carregar os dados existentes do arquivo JSON (se existir)
try:
    with open('alunos.json', 'r') as arquivo_json:
        alunos = json.load(arquivo_json)
except FileNotFoundError:
    alunos = []

# Lista para armazenar as turmas
turmas = []

# Dicionário para mapear grupos com seus respectivos alunos
grupos = {}

def criacao_de_grupo():
# Função para criar um grupo e associá-lo a uma turma
    def criar_grupo():
        nome_grupo = input("Digite o nome do grupo: ")

        # Exibir as turmas disponíveis para seleção
        print("Turmas disponíveis:")
        for turma in turmas:
            print(f"- ID da Turma: {turma['id_turma']}")

        id_turma = input("Selecione a ID da turma para associar ao grupo: ")

        # Verificar se a turma existe
        turma_encontrada = None
        for turma in turmas:
            if turma['id_turma'] == id_turma:
                turma_encontrada = turma
                break

        if turma_encontrada:
            grupos[nome_grupo] = {'turma': turma_encontrada, 'alunos': []}
            print(f"Grupo '{nome_grupo}' criado e associado à turma '{turma_encontrada['id_turma']}'.")
        else:
            print("Turma não encontrada. Grupo não criado.")

# Função para atribuir um aluno a um grupo
def atribuir_aluno_a_grupo():
    # Exibir os grupos disponíveis
    print("Grupos disponíveis:")
    for grupo in grupos:
        print(f"- Nome do Grupo: {grupo}")

    nome_grupo = input("Selecione o nome do grupo para adicionar um aluno: ")

    # Verificar se o grupo existe
    grupo_encontrado = grupos.get(nome_grupo)

    if grupo_encontrado:
        id_turma = grupo_encontrado['turma']['id_turma']

        # Exibir os alunos disponíveis na turma
        print(f"Alunos da turma {id_turma}:")
        alunos_turma = grupo_encontrado['turma']['alunos']
        for aluno in alunos_turma:
            print(f"- Nome do Aluno: {aluno['nome']} (RA: {aluno['ra']})")

        ra_aluno = input("Digite o RA do aluno para adicionar ao grupo: ")

        # Verificar se o aluno existe na turma
        aluno_encontrado = None
        for aluno in alunos_turma:
            if aluno['ra'] == ra_aluno:
                aluno_encontrado = aluno
                break

        if aluno_encontrado:
            grupo_encontrado['alunos'].append(aluno_encontrado)
            print(f"Aluno adicionado ao grupo '{nome_grupo}'.")
        else:
            print("Aluno não encontrado na turma.")
    else:
        print("Grupo não encontrado.")


