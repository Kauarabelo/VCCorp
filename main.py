import cadastrar_aluno
import cadastro_turma
import aluno_ciclo
import editar_turmas
import editar_aluno
import criar_grupos
import editar_grupos

# Função para exibir opções de menu
def exibir_menu():
    print("\nOnde você quer ir hoje?")
    print("1. Alunos")
    print("2. Turmas")
    print("3. Grupos de Alunos")
    print("4. Ciclos e Notas")
    print("5. Sair\n")

# Loop do menu
while True:
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        # Se digitado a ou A, leva para Cadastrar Aluno ou Editar Aluno
        escolha_1 = str(input("\nA. Cadastro de aluno / B. Editar Aluno: ")).strip().lower()
        if escolha_1 == 'a' or escolha_1 == 'A':
            cadastrar_aluno.cadastrar_alunos()

        elif escolha_1 == 'b' or escolha_1 == 'B':
            editar_aluno.editar_alunos()
            
        else:
            print("\nOpção inválida. Tente novamente.")

    elif opcao == "2":
        # Se digitado a ou A, leva para Cadastrar Turma ou Editar Turma
        escolha_2 = str(input("\nA. Cadastrar Turma / B. Editar Turma: ")).strip().lower()
        if escolha_2 == 'a' or escolha_2 == 'A':  
           cadastro_turma.cadastrar_turma()
        
        elif escolha_2 == 'b' or escolha_2 == 'B':
            editar_turmas.editar_turmas()
            
        else:
            print("\nOpção inválida. Tente novamente.") 

    elif opcao == "3":
        # Se digitado a ou A, leva para Cadastrar Grupo ou Editar Grupo
        escolha_3 = str(input("\nA. Cadastrar Grupo / B. Editar Grupo: ")).strip().lower()
        if escolha_3 == 'a' or escolha_3 == 'A':
            criar_grupos.criacao_de_grupo()
            
        elif escolha_3 == 'b' or escolha_3 == 'B':
            editar_grupos.editar_grupo()
            
        else:
            print("\nOpção inválida. Tente novamente.")

    elif opcao == "4":
        # Se digitado a ou A, leva para Criar ciclo ou Editar Ciclo
        escolha_4 = str(input("\nA. Criar Ciclo/Nota / B. Editar Ciclo/Notas: ")).strip().lower()
        if escolha_4 == 'a' or escolha_4 == 'A':
            aluno_ciclo.registrar_ciclos_e_notas()
            
        elif escolha_4 == 'b' or escolha_4 == 'B':
            pass
            
        else:
            print("\nOpção inválida. Tente novamente.")

    elif opcao == "5":
        break
    else:
        print("\nOpção inválida. Tente novamente.\n")