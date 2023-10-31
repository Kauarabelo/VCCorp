import cadastro_turma
import aluno_ciclo
import editar_turmas
import editar_aluno

# Função para exibir opções de menu
def exibir_menu():
    print("O que você quer fazer hoje?")
    print("1. Cadastro de turmas e Ciclos de Notas")
    print("2. Editar alunos")
    print("3. Relatório")
    print("4. Sair")

# Loop do menu
while True:
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        escolha_1 = str(input("A. Cadastro de turmas / B. Ciclos de Notas: ")).strip().lower()
        if escolha_1 == 'a':
            cadastro_turma.cadastrar_turma()
        elif escolha_1 == 'b':
            aluno_ciclo.registrar_ciclos_e_notas()

    elif opcao == "2":
        escolha_2 = str(input("A. Editar Aluno / B. Editar Turma: ")).strip().lower()
        if escolha_2 == 'a':  # Corrigido de escolha_1 para escolha_2
            editar_aluno.editar_aluno()
        elif escolha_2 == 'b':  # Corrigido de escolha_1 para escolha_2
            editar_turmas.editar_turmas()

    elif opcao == "3":
        print("A. Relatório Json das turmas")  # Removido o .strip().lower()
        print("B. Relatório Json dos ciclos das notas")  # Removido o .strip().lower()
        escolha_relatorio = str(input("Qual relatório deseja ver? ")).strip().lower()
        if escolha_relatorio == 'a':
            cadastro_turma.relatorio_turmas()
        elif escolha_relatorio == 'b':
            aluno_ciclo.relatorio_ciclos_notas()

    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")