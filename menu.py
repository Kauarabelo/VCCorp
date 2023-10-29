import json
import cadastrar_aluno
import editar_alunoarquivo
import editar_turmas

while True:  # Loop infinito para manter o menu principal em execução
    print("\r\n"* 2)
    print('Olá administrador, bem-vindo ao sistema de informação da PBLtex')
    primeiromenu1 = input('Escolha uma das opções:\n1-Cadastro\n2-Editar\n')

    if primeiromenu1 == '1':
        segundomenu1 = input('O que deseja cadastrar?\n1-Alunos\n2-Turmas\n3-Ciclos\n4-Notas\n5-Grupo\n')
        if segundomenu1 == '1':
            if cadastrar_aluno.func_cadastrar_alunos():
                print("\r\n"* 2) 
                print("Retornando ao menu principal.")
            else:
                print("\r\n"* 2) 
                print(" O cadastro foi cancelado.\n Retornando ao menu principal.")
        elif segundomenu1 == '2':
            print('Opção para cadastrar Turmas')
        elif segundomenu1 == '3':
            print('Opção para cadastrar Ciclos')
        elif segundomenu1 == '4':
            print('Opção para cadastrar Notas')
        elif segundomenu1 == '5':
            print('Opção para cadastrar Grupo')
        else:
            print('Opção inválida. Saindo.')
    elif primeiromenu1 == '2':
        segundomenu = input('O que deseja editar?\n1-Alunos\n2-Turmas\n3-Ciclos\n4-Notas\n5-Grupo\n')
        if segundomenu == '1':
            RA = input('Qual o RA do aluno que você quer editar?Digite agora:  ')
            if editar_alunoarquivo.editar_aluno(RA):
                print("\r\n"* 2) 
                print("Retornando ao menu principal.")
            else:
                print("\r\n"* 2) 
                print(" A edição foi cancelada.\n Retornando ao menu principal.")
        elif segundomenu == '2':
            ra_aluno = input('Informe o RA do aluno que quer adicionar ou retirar de turmas')
            if editar_turmas.editar_turmas_aluno(ra_aluno):
                print("\r\n"* 2) 
                print("Retornando ao menu principal.")
        elif segundomenu == '3':
            print('Opção para editar Ciclos')
        elif segundomenu == '4':
            print('Opção para editar Notas')
        elif segundomenu == '5':
            print('Opção para editar Grupo')
        else:
            print('Opção inválida. Saindo.')
    else:
        print('Opção inválida. Saindo.')
