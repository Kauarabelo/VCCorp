import aluno_ciclo
import cadastro_turma

# Função para exibir opções de menu
def exibir_menu():
    print("O que você quer fazer hoje?")
    print("1. Cadastro de turmas")
    print("2. Ciclos e Notas")
    print("3. Relatório")
    print("4. Sair")

# Loop do menu
while True:
    exibir_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        cadastro_turma.cadastrar_turma()  # Chama a função para cadastrar turmas
    elif opcao == "2":
        aluno_ciclo.registrar_ciclos_e_notas()  # Chama a função para registrar ciclos e notas
    elif opcao == "3":
        # Adicione aqui a lógica para a opção de relatório
        print("Opção de relatório ainda não implementada.")
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
