import json

            
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



def func_cadastrar_notas():
    dados = carregar_dados()
    ra_aluno = input('Informe o RA do aluno para lançar a nota: ')
    if ra_aluno not in dados['alunos']:
        print('O RA do aluno não foi encontrado.')
        return False

    turmas_aluno = dados['alunos'][ra_aluno]['turmas']
    if not turmas_aluno:
        print('O aluno não está em nenhuma turma.')
        return False

    print('Turmas disponíveis para lançar nota:')
    for turma_id in turmas_aluno:
        if turma_id in dados['turmas']:
            print(f'Turma ID: {turma_id}, Nome: {dados["turmas"][turma_id]["Nome"]}')

    turma_id = input('Informe o ID da turma para lançar a nota: ')
    if turma_id not in turmas_aluno:
        print('O aluno não está nesta turma.')
        return False

    ciclos_turma = dados['turmas'][turma_id]['ciclos']
    if not ciclos_turma:
        print('A turma não possui ciclos cadastrados.')
        return False

    print('Ciclos disponíveis para lançar nota:')
    for ciclo_id in ciclos_turma:
        if ciclo_id in dados['ciclos']:
            ciclo = dados['ciclos'][ciclo_id]
            print(f'Ciclo ID: {ciclo_id}, Nome: {ciclo["Nome"]}, Data de Início: {ciclo["Data de Início"]}, Data de Fim: {ciclo["Data de Fim"]}')

    ciclo_id = input('Informe o ID do ciclo para lançar a nota: ')
    if ciclo_id not in ciclos_turma:
        print('A turma não possui este ciclo.')
        return False

    nota = float(input('Informe a nota a ser lançada: '))
    if nota < 0 or nota > 10:
        print('A nota deve estar entre 0 e 10.')
        return False

    # Adicione a nota aos dados
    nova_nota = {
        'AlunoRA': ra_aluno,
        'CicloID': ciclo_id,
        'TurmaID': turma_id,
        'Nota': nota
    }
    dados['notas'][get_next_nota_id(dados['notas'])] = nova_nota

    with open('dados.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
    print('Nota lançada com sucesso.')
    return True

def get_next_nota_id(notas):
    if not notas:
        return 'ID1'
    max_id = max([int(id[2:]) for id in notas.keys()])
    return f'ID{max_id + 1}'
