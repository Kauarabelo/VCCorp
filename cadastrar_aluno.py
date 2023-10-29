import json
import editar_alunoarquivo
# Function to register students
def func_cadastrar_alunos():
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
                editar_alunoarquivo.editar_aluno(ra_aluno)
                print('Dados editados com sucesso')
                return False
        else:
            nome_aluno = input('Qual nome do aluno a ser cadastrado? ')
            idade_aluno = input('Qual idade do aluno a ser cadastrado? ')
            email_aluno = input('Qual e-mail do aluno a ser cadastrado? ')

            novo_aluno = {
                'RA': ra_aluno,
                'Nome': nome_aluno,
                'Idade': idade_aluno,
                'E-mail': email_aluno,
                'turmas': [],  # Inicialmente, o aluno não pertence a nenhuma turma
                'grupos': []   # Inicialmente, o aluno não pertence a nenhum grupo
            }

        while True:
            # Exibir dados do aluno para confirmação e opções
            print(f'\n\n\nRA: {ra_aluno}')
            print(f'Nome: {nome_aluno}')
            print(f'Idade: {idade_aluno}')
            print(f'E-mail: {email_aluno}')

            menu_cad_aluno_1 = input('Para confirmar, escolha a opção:\n1-Alterar Nome\n2-Alterar Idade\n3-Alterar E-mail\n4-Cadastrar outro aluno\n5-Confirmar cadastro e voltar ao menu\n6-Cancelar cadastro e voltar ao menu\n')

            if menu_cad_aluno_1 == '1':
                nome_aluno = input('Novo Nome: ')
            elif menu_cad_aluno_1 == '2':
                idade_aluno = input('Nova Idade: ')
            elif menu_cad_aluno_1 == '3':
                email_aluno = input('Novo E-mail: ')
                
            elif menu_cad_aluno_1 == '4':
                break  # Sai do loop de confirmação e cadastra outro aluno
            elif menu_cad_aluno_1 == '5':
                # Salva os dados no arquivo JSON
                dados_alunos['alunos'][ra_aluno] = novo_aluno
                with open('dados_alunos.json', 'w') as arquivo_dados_alunos_json:
                    json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                print('Cadastro realizado com sucesso.')
                return True
            elif menu_cad_aluno_1 == '6':
                print('Cadastro cancelado.')
                # Encerra o programa para voltar ao menu do menu.py
                return False
