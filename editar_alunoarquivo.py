import json

def editar_aluno(ra_aluno):
    # Check if the RA exists in the JSON file
    with open('dados_alunos.json', 'r+') as arquivo_dados_alunos_json:
        dados_alunos = json.load(arquivo_dados_alunos_json)

        aluno = dados_alunos.get('alunos', {}).get(ra_aluno)
        if aluno:
            print(f'\nEditando dados do aluno RA: {ra_aluno}')
            while True:
                print(f'1-Nome: {aluno["Nome"]}')
                print(f'2-Idade: {aluno["Idade"]}')
                print(f'3-E-mail: {aluno["E-mail"]}')

                campo = input('Escolha o campo que deseja editar (1/2/3), 4 para cancelar ou 5 - PARA SALVAR: ')
                if campo == '1':
                    aluno["Nome"] = input('Novo Nome: ')
                elif campo == '2':
                    aluno["Idade"] = input('Nova Idade: ')
                elif campo == '3':
                    aluno["E-mail"] = input('Novo E-mail: ')
                elif campo == '4':
                    break
                elif campo == '5':
                    arquivo_dados_alunos_json.seek(0)  # Volta para o início do arquivo
                    json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                    arquivo_dados_alunos_json.truncate()
                    print('Cadastro atualizado com sucesso.')
                    return True
                else:
                    print('Opção inválida. Tente novamente.')
            if campo != '4':
                # Atualiza a seção de alunos no arquivo JSON
                dados_alunos['alunos'][ra_aluno] = aluno
                arquivo_dados_alunos_json.seek(0)  # Volta para o início do arquivo
                json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                arquivo_dados_alunos_json.truncate()
                print('Cadastro atualizado com sucesso.')
            else:
                return False
        else:
            print(f'O aluno com RA {ra_aluno} não foi encontrado.')
            return False
