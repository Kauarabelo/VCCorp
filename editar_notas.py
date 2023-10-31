import json


def carregar_dados():
    try:
        with open('dados_alunos.json', 'r') as arquivo_dados_alunos_json:
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

def editar_nota(nota_id):
    dados = carregar_dados()
    if nota_id in dados['notas']:
        nota = dados['notas'][nota_id]
        print(f'Editando nota com ID: {nota_id}')
        while True:
            print(f'1 - Aluno: {dados["alunos"].get(nota["AlunoRA"], {}).get("Nome")}')
            print(f'2 - Ciclo: {dados["ciclos"].get(nota["CicloID"], {}).get("Nome")}')
            print(f'3 - Turma: {dados["turmas"].get(nota["TurmaID"], {}).get("Nome")}')
            print(f'4 - Nota: {nota["Nota"]}')

            campo = input('Escolha o campo que deseja editar (1/2/3/4) ou 0 para salvar e sair: ')

            if campo == '1':
                aluno_ra = input('Informe o novo RA do aluno: ')
                if aluno_ra in dados['alunos']:
                    nota["AlunoRA"] = aluno_ra
                else:
                    print('Aluno não encontrado. O RA não foi alterado.')

            elif campo == '2':
                ciclo_id = input('Informe o novo ID do ciclo: ')
                if ciclo_id in dados['ciclos']:
                    nota["CicloID"] = ciclo_id
                else:
                    print('Ciclo não encontrado. O ID não foi alterado.')

            elif campo == '3':
                turma_id = input('Informe o novo ID da turma: ')
                if turma_id in dados['turmas']:
                    nota["TurmaID"] = turma_id
                else:
                    print('Turma não encontrada. O ID não foi alterado.')

            elif campo == '4':
                nova_nota = float(input('Informe a nova nota: '))
                if 0 <= nova_nota <= 10:
                    nota["Nota"] = nova_nota
                else:
                    print('Nota inválida. A nota não foi alterada.')

            elif campo == '0':
                with open('dados.json', 'w') as arquivo_json:
                    json.dump(dados, arquivo_json, indent=4)
                print('Edição de nota realizada com sucesso.')
                return True

            else:
                print('Opção inválida. Tente novamente.')

    else:
        print(f'A nota com ID {nota_id} não foi encontrada.')
        return False
