import json

# Lista para armazenar os alunos
alunos = []

ciclos_entry_list = []
pesos_ciclos = {}
id_turma = ""  # Variável para armazenar o ID da turma


def registrar_ciclos_e_notas():
    # Função para adicionar ciclos
    def adicionar_ciclo():
        global id_turma  # Utilize a variável global id_turma
        ciclo = input("Digite o nome do ciclo: ")
        if ciclo:
            id_turma = input("Digite o ID da turma: ")  # Defina o id_turma
            peso_ciclo = float(input(f"Digite o peso para o ciclo '{ciclo}': "))
            data_inicio = input(f"Quando começará o ciclo '{ciclo}'? ")
            data_final = input(f"Quando terminará o ciclo '{ciclo}'? ")
            pesos_ciclos[ciclo] = peso_ciclo
            ciclos_entry_list.append({
                'ciclo': ciclo,
                'data_inicio': data_inicio,
                'data_final': data_final,
            })

    # Função para coletar as notas dos alunos e calcular a média ponderada
    def coletar_notas():
        notas_aluno = []

        for ciclo in ciclos_entry_list:
            nota_ciclo = float(input(f"Digite a nota para o ciclo '{ciclo['ciclo']}': "))
            notas_aluno.append({
                'Ciclo': ciclo['ciclo'],
                'Nota': nota_ciclo,
                'Data de Início': ciclo['data_inicio'],
                'Data de Término': ciclo['data_final'],
                'ID da Turma': id_turma  # Utilize o id_turma definido na função adicionar_ciclo
            })

        # Calcular a média ponderada
        soma_notas = sum(nota['Nota'] * pesos_ciclos[nota['Ciclo']] for nota in notas_aluno)
        soma_pesos = sum(pesos_ciclos[nota['Ciclo']] for nota in notas_aluno)
        if soma_pesos == 0:
            media_ponderada = 0.0
        else:
            media_ponderada = soma_notas / soma_pesos

        nome_aluno = input("Digite o nome do aluno: ")

        aluno = {
            'Nome': nome_aluno,
            'id_turma': id_turma,
            'Notas': notas_aluno,
            'Média Ponderada': media_ponderada
        }

        alunos.append(aluno)

        print("Notas coletadas com sucesso!")

    # Função para exibir informações dos alunos
    def exibir_notas():
        for aluno in alunos:
            print(f"Nome: {aluno['Nome']}")
            print(f"ID da Turma: {aluno['id_turma']},")
            for nota in aluno['Notas']:
                print(f"Ciclo: {nota['Ciclo']}, Nota: {nota['Nota']}")
                print(f"Data de Início: {nota['Data de Início']}, Data de Término: {nota['Data de Término']}")
            print(f"Média Ponderada: {aluno['Média Ponderada']}\n")

    while True:
        print("\nMenu:")
        print("1. Adicionar Ciclo")
        print("2. Coletar Notas")
        print("3. Exibir Notas")
        print("4. Sair e criar Json")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_ciclo()
        elif escolha == '2':
            coletar_notas()
        elif escolha == '3':
            exibir_notas()
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

if alunos:
    # Ao sair do loop, crie o arquivo JSON com as notas
    def relatorio_ciclos_notas(alunos):
        with open('notas_alunos.json', 'w') as json_file:
            json.dump(alunos, json_file, indent=4)
    print("Arquivo JSON criado com as notas dos alunos: 'notas_alunos.json'")

