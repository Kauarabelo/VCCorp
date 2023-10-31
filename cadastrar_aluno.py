import json
import editar_aluno
# Function to register students
def cadastrar_alunos():
    while True:
        ra_aluno = input('Informe o RA do aluno a ser cadastrado: ')

        # Check if the RA already exists in the JSON file
        with open('dados_alunos.json', 'r') as arquivo_dados_alunos_json:
            dados_alunos = json.load(arquivo_dados_alunos_json)

        if ra_aluno in dados_alunos.get('alunos', {}):
            
            ra_ja_cadastrado = input('O RA informado já está cadastrado. O que deseja?\n1-Criar um novo cadastro\n2-Editar os dados do aluno do RA informado?\n')
            if ra_ja_cadastrado == '1':
                continue  # Recomeça o loop
            elif ra_ja_cadastrado == '2':
                editar_aluno.editar_aluno(ra_aluno)
                print('Dados editados com sucesso')
                return False
        else:
            nome_aluno = input('Qual nome do aluno a ser cadastrado? ')

            novo_aluno = {
                'RA': ra_aluno,
                'Nome': nome_aluno,
                'turmas': [],  # Inicialmente, o aluno não pertence a nenhuma turma
                'grupos': []   # Inicialmente, o aluno não pertence a nenhum grupo
            }

        while True:
            # Exibir dados do aluno para confirmação e opções
            print(f'\n\n\nRA: {ra_aluno}')
            print(f'Nome: {nome_aluno}')

            menu_cad_aluno_1 = input('Para confirmar, escolha a opção:\n1-Alterar Nomel\n2-Cadastrar outro aluno\n3-Confirmar cadastro e voltar ao menu\n4-Cancelar cadastro e voltar ao menu\n')

            if menu_cad_aluno_1 == '1':
                nome_aluno = input('Novo Nome: ')
                
            elif menu_cad_aluno_1 == '2':
                break  # Sai do loop de confirmação e cadastra outro aluno
            elif menu_cad_aluno_1 == '3':
                # Salva os dados no arquivo JSON
                dados_alunos['alunos'][ra_aluno] = novo_aluno
                with open('dados_alunos.json', 'w') as arquivo_dados_alunos_json:
                    json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                print('Cadastro realizado com sucesso.')
                return True
            elif menu_cad_aluno_1 == '4':
                print('Cadastro cancelado.')
                # Encerra o programa para voltar ao menu do menu.py
                return False
