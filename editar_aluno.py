import json

def editar_alunos():
    try:
        ra_aluno = input("Informe o RA do aluno que deseja editar: ")
        
        with open('dados_alunos.json', 'r+') as arquivo_dados_alunos_json:
            dados_alunos = json.load(arquivo_dados_alunos_json)
            aluno = dados_alunos['alunos'].get(ra_aluno)

            if aluno:
                print(f'\nEditando dados do aluno RA: {ra_aluno}\n')
                while True:
                    print('Dados:')
                    print(f'1- Nome: {aluno["Nome"]}')
                    print(f'2- Idade: {aluno["Idade"]}')
                    print(f'3- E-mail: {aluno["E-mail"]}')
                    print('\n2-Remover aluno')
                    campo = input('Escolha o campo que deseja editar (1), (2) para remover, 3 para sair: ')

                    if campo == '1':
                        novo_nome = input('Novo Nome: ')
                        aluno["Nome"] = novo_nome

                    elif campo == '2':
                        confirmacao = input('Tem certeza que deseja remover o aluno? (S/N): ')
                        if confirmacao.lower() == 's':
                            del dados_alunos['alunos'][ra_aluno]
                            arquivo_dados_alunos_json.seek(0)
                            json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                            arquivo_dados_alunos_json.truncate()
                            print(f'O aluno com RA {ra_aluno} foi removido com sucesso.')
                            break

                    elif campo == '3':
                        # Se o campo for '3', apenas saia do loop
                        break

                    else:
                        print('Opção inválida. Tente novamente.')

                # Se o campo não for '3' e a opção para remover não foi escolhida, atualiza os dados do aluno
                else:
                    dados_alunos['alunos'][ra_aluno] = aluno
                    arquivo_dados_alunos_json.seek(0)
                    json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                    arquivo_dados_alunos_json.truncate()
                    print('Cadastro atualizado com sucesso.')

            else:
                print(f'O aluno com RA {ra_aluno} não foi encontrado.')

    except FileNotFoundError:
        print("Arquivo 'dados_alunos.json' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


