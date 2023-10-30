import json

def editar_turmas(ra_aluno):
    # Verifique se o RA do aluno existe no arquivo JSON
    with open('dados_alunos.json', 'r+') as arquivo_dados_alunos_json:
        dados_alunos = json.load(arquivo_dados_alunos_json)

        aluno = dados_alunos.get('alunos', {}).get(ra_aluno)
        if aluno:
            print(f'\nEditando turmas do aluno com RA: {ra_aluno}')
            while True:
                print(f'Turmas atuais do aluno: {aluno["turmas"]}')

                acao = input('Escolha a ação:\n1-Adicionar Turma\n2-Remover Turma\n3-Para sair: ')
                if acao == '1':
                    codigo_turma = input('Digite o código da turma que deseja adicionar: ')
                    if codigo_turma not in aluno["turmas"]:
                        aluno["turmas"].append(codigo_turma)
                    else:
                        print(f'O aluno já está na turma com código: {codigo_turma}')
                elif acao == '2':
                    codigo_turma = input('Digite o código da turma que deseja remover: ')
                    if codigo_turma in aluno["turmas"]:
                        aluno["turmas"].remove(codigo_turma)
                        print(f'O aluno foi removido da turma com código: {codigo_turma}')
                    else:
                        print(f'O aluno não está na turma com código: {codigo_turma}')
                elif acao == '3':
                    break
                else:
                    print('Opção inválida. Tente novamente.')

            # Atualiza a seção de alunos no arquivo JSON com as turmas atualizadas
            dados_alunos['alunos'][ra_aluno] = aluno
            arquivo_dados_alunos_json.seek(0)  # Volta para o início do arquivo
            json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
            arquivo_dados_alunos_json.truncate()
            print('Turmas do aluno atualizadas com sucesso.')
            return True
        else:
            print(f'O aluno com RA {ra_aluno} não foi encontrado.')
            return False