import cadastrar_aluno
import aluno_ciclo
import editar_turmas
import editar_aluno

# Função para exibir opções de menu
def exibir_menu():
    print("O que você quer fazer hoje?")
    print("1. Cadastros")
    print("2. Editar")
    print("3. Relatório")
    print("4. Sair")

# Loop do menu
while True:
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        escolha_1 = str(input("A. Cadastro de aluno / B. Cadastro de Turmas / C. Grupos de Aluno / D. Ciclos/Notas: ")).strip().lower()
        if escolha_1 == 'a':
            cadastrar_aluno.cadastrar_alunos()

        #elif escolha_1 == 'b'
        #elif escolha_1 == 'c'

        elif escolha_1 == 'd':
            aluno_ciclo.registrar_ciclos_e_notas()

    elif opcao == "2":
        escolha_2 = str(input("A. Editar Aluno / B. Editar Turma / C. Editar Grupos de Alunos / D. Editar Notas: ")).strip().lower()
        if escolha_2 == 'a':  
            editar_aluno.editar_aluno()
            
        elif escolha_2 == 'b':  
            editar_turmas.editar_turmas()

        #elif escolha_2 == 'c'
        #elif escolha_2 == 'd'

    elif opcao == "3":
        print("A. Relatório Json das turmas") 
        print("B. Relatório Json dos ciclos das notas") 
        escolha_relatorio = str(input("Qual relatório deseja ver? ")).strip().lower()
        if escolha_relatorio == 'a':
            cadastrar_aluno.relatorio_turmas()
        elif escolha_relatorio == 'b':
            aluno_ciclo.relatorio_ciclos_notas()

    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")