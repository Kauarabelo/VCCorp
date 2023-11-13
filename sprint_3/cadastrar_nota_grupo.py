import json

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        # Se o arquivo não existir, cria uma estrutura vazia
        dados = {
            "alunos": {},
            "turmas": {},
            "ciclos": {},
            "grupos": {},
            "notas": {
                "grupos": {}
            }
        }
    return dados

# Função para cadastrar notas para grupos
def cadastrar_notas_grupos():
    dados = carregar_dados()
    id_grupo = input('Informe o ID do grupo para lançar a nota: ')
    
    # Verifica se o ID do grupo está nos dados
    if id_grupo not in dados['alunos']:
        print('O ID do grupo não foi encontrado.')
        return False

    turmas_aluno = dados['alunos'][id_grupo]['turmas'] 

    print('Turmas disponíveis para lançar nota:')
    for turma_id in turmas_aluno:
        if turma_id in dados['turmas']:
            print(f'Turma ID: {turma_id}, Nome: {dados["turmas"][turma_id]["Nome"]}')

    turma_id = input('Informe o ID da turma para lançar a nota: ')

    ciclos_turma = dados['turmas'][turma_id].get('ciclos', [])
    
    # Verifica se a turma possui ciclos cadastrados
    if not ciclos_turma:
        print('A turma não possui ciclos cadastrados.')
        return False

    print('Ciclos disponíveis para lançar nota:')
    for ciclo in ciclos_turma:
        print(f'Ciclo ID: {ciclo["ID"]}, Nome: {ciclo["Nome"]}, Data de Início: {ciclo["Data de Início"]}, Data de Fim: {ciclo["Data de Fim"]}')

    ciclo_id = input('Informe o ID do ciclo para lançar a nota: ')
    ciclo_encontrado = next((c for c in ciclos_turma if c["ID"] == ciclo_id), None)

    # Verifica se o ciclo existe no grupo
    if not ciclo_encontrado:
        print('O grupo não possui este ciclo.')
        return False

    nota = float(input('Informe a nota a ser lançada: '))
    
    # Verifica se a nota está no intervalo permitido
    if nota < 0 or nota > 10:
        print('A nota deve estar entre 0 e 10.')
        return False

    # Adiciona a nota aos dados
    nova_nota = {
        'IDgrupo': id_grupo,
        'CicloID': ciclo_id,
        'Nota': nota
    }

    # Adiciona a nota à seção de notas dos grupos
    dados['notas']['grupos'][get_next_nota_id(dados['notas']['grupos'])] = nova_nota

    # Salva os dados atualizados no arquivo JSON
    with open('dados.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
    print('Nota lançada com sucesso.')
    return True

# Função para obter o próximo ID de nota
def get_next_nota_id(notas):
    if not notas:
        return 'ID1'
    max_id = max([int(id[2:]) for id in notas.keys()])
    return f'ID{max_id + 1}'


