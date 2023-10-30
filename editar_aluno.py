import json

def editar_aluno(ra_aluno):
    with open('dados_alunos.json', 'r+') as arquivo_dados_alunos_json:
        dados_alunos = json.load(arquivo_dados_alunos_json)
        aluno = dados_alunos['alunos'].get(ra_aluno)

        if aluno:
            print(f'\nEditando dados do aluno RA: {ra_aluno}')
            while True:
                print(f'1-Nome: {aluno["Nome"]}')
                print('2-Remover aluno')
                campo = input('Escolha o campo que deseja editar (1), (2) para remover, 3 para sair: ')

                if campo == '1':
                    aluno["Nome"] = input('Novo Nome: ')

                elif campo == '2':
                    confirmacao = input('Tem certeza que deseja remover o aluno? (S/N): ')
                    if confirmacao.lower() == 's':
                        del dados_alunos['alunos'][ra_aluno]
                        arquivo_dados_alunos_json.seek(0)
                        json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                        arquivo_dados_alunos_json.truncate()
                        print(f'O aluno com RA {ra_aluno} foi removido com sucesso.')
                        return True

                elif campo == '3':
                    # Se o campo for '3', apenas saia do loop
                    break

                else:
                    print('Opção inválida. Tente novamente.')

            # Se o campo não for '3' e a opção para remover não foi escolhida, atualiza os dados do aluno
            dados_alunos['alunos'][ra_aluno] = aluno
            arquivo_dados_alunos_json.seek(0)
            json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
            arquivo_dados_alunos_json.truncate()
            print('Cadastro atualizado com sucesso.')

        else:
            print(f'O aluno com RA {ra_aluno} não foi encontrado.')
            return False

# Exemplo de uso:
ra_aluno = input('Digite o RA do aluno que deseja editar ou remover: ')
editar_aluno(ra_aluno)
