import json

# Carregar os dados existentes do arquivo JSON (se existir)
try:
    with open('alunos.json', 'r') as arquivo_json:
        alunos = json.load(arquivo_json)
except FileNotFoundError:
    alunos = []

# Loop para cada aluno
while True:
    nome_aluno = input(f"Cadastre o nome do {len(alunos) + 1}º aluno (Nome completo): ")
    turma_aluno = input(f"Em qual turma o aluno {nome_aluno} está? ")
    
    # Criar um dicionário com o nome e a turma do aluno
    aluno = {
        'nome': nome_aluno,
        'turma': turma_aluno
    }
    
    # Adicionar o aluno à lista de alunos
    alunos.append(aluno)

    continuar = input("Deseja adicionar mais um aluno(a)? (S/N)").strip().lower()
    if continuar != 's':
        break

# Exibir a lista de alunos cadastrados
print("Lista de Alunos Cadastrados:")
for idx, aluno in enumerate(alunos, start=1):
    print(f"{idx}. nome: {aluno['nome']}, turma: {aluno['turma']}")

# Exemplo de como salvar os dados em JSON
with open('alunos.json', 'w') as arquivo_json:
    json.dump(alunos, arquivo_json)



