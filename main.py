import cadastrar_aluno
import aluno_ciclo
import editar_turmas
import editar_aluno

# Função para exibir opções de menu
def exibir_menu():
    print("Onde você quer ir hoje?")
    print("1. Alunos")
    print("2. Turmas")
    print("3. Grupos de Alunos")
    print("4. Ciclos e Notas")
    print("5. Sair")

# Loop do menu
while True:
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        escolha_1 = str(input("A. Cadastro de aluno / B. Editar Aluno")).strip().lower()
        if escolha_1 == 'a':
            cadastrar_aluno.cadastrar_alunos()

        else:
            editar_aluno.editar_aluno()

    elif opcao == "2":
        escolha_2 = str(input("A. Cadastrar Turma / B. Editar Turma")).strip().lower()
        if escolha_2 == 'a':  
           cadastrar_aluno.cadastrar_alunos()
        else:
            editar_turmas.editar_turmas() 

    elif opcao == "3":
        escolha_3 = str(input("A. Cadastrar Grupo / B. Editar Grupo")).strip().lower()
        if escolha_3 == 'a':
            pass

    elif opcao == "4":
        escolha_4 = str(input("A. Criar Ciclo/Nota / B. Editar Ciclo/Notas")).strip().lower()
        if escolha_4 == 'a':
            aluno_ciclo.registrar_ciclos_e_notas()
        else:
            pass

    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")