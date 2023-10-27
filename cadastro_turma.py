import json

# Carregar os dados existentes do arquivo JSON (se existir)
try:
    with open('alunos.json', 'r') as arquivo_json:
        alunos = json.load(arquivo_json)
except FileNotFoundError:
    alunos = []

# Contador das RAs
contador_ra = 1

# Lista para armazenar as turmas
turmas = []

def cadastrar_turma():
    while True:
        id_turma = input("Digite o ID da turma: ")
        data_inicio = input("Digite a data de início da turma: ")

        # Lista para armazenar os alunos da turma
        alunos_turma = []

        while True:
            nome_aluno = input(f"Digite o nome do aluno (Turma {id_turma}): ")
            pergunta_turma = str(input("Esse aluno está em outra turma(S/N)? ")).strip().lower()
            if pergunta_turma == 's':
                outro_id_turma = input("Em qual outra turma ele está? ")
            else:
                continue

            # Criar a RA como uma string
            ra = str(contador_ra)

            # Criar um dicionário com o nome, o ID da turma e a RA do aluno
            aluno = {
                'nome': nome_aluno,
                'id_turma': id_turma,
                'ra': ra
            }

            # Adicionar o aluno à lista de alunos da turma
            alunos_turma.append(aluno)

            # Incrementar o número da RA
            contador_ra += 1

            continuar = input("Deseja adicionar mais um aluno(a)? (S/N)").strip().lower()
            if continuar != 's':
                break

        # Criar um dicionário com as informações da turma
        turma = {
            'id_turma': id_turma,
            'data_inicio': data_inicio,
            'alunos': alunos_turma
        }

        # Adicionar a turma à lista de turmas
        turmas.append(turma)

        continuar = input("Deseja criar outra turma? (S/N)").strip().lower()
        if continuar != 's':
            break

# Exibir as informações das turmas
print("\nInformações das Turmas:")
for turma in turmas:
    print(f"ID da Turma: {turma['id_turma']}")
    print(f"Data de Início: {turma['data_inicio']}")
    print("Alunos:")
    for aluno in turma['alunos']:
        print(f"- Nome: {aluno['nome']}, ID da Turma: {aluno['id_turma']}, RA: {aluno['ra']}")
    print("\n")

# Exemplo de como salvar os dados em JSON
with open('turmas.json', 'w') as arquivo_json:
    json.dump(turmas, arquivo_json, indent=4)
