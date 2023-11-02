import criar_grupos
grupos = {}

def editar_grupo():

    def adicionar_aluno_a_grupo():
        # Exibir os grupos disponíveis
        print("Grupos disponíveis:")
        for grupo in grupos:
            print(f"- Nome do Grupo: {grupo}")

        nome_grupo = input("Selecione o nome do grupo para adicionar um aluno: ")

        # Verificar se o grupo existe
        grupo_encontrado = grupos.get(nome_grupo)

        if grupo_encontrado:
            id_turma = grupo_encontrado['turma']['id_turma']

            # Exibir os alunos disponíveis na turma
            print(f"Alunos da turma {id_turma}:")
            alunos_turma = grupo_encontrado['turma']['alunos']
            for aluno in alunos_turma:
                print(f"- Nome do Aluno: {aluno['nome']} (RA: {aluno['ra']})")

            ra_aluno = input("Digite o RA do aluno para adicionar ao grupo: ")

            # Verificar se o aluno existe na turma
            aluno_encontrado = None
            for aluno in alunos_turma:
                if aluno['ra'] == ra_aluno:
                    aluno_encontrado = aluno
                    break

            if aluno_encontrado:
                if aluno_encontrado not in grupo_encontrado['alunos']:
                    grupo_encontrado['alunos'].append(aluno_encontrado)
                    print(f"Aluno adicionado ao grupo '{nome_grupo}'.")
                else:
                    print("Aluno já está no grupo.")
            else:
                print("Aluno não encontrado na turma.")
        else:
            print("Grupo não encontrado.")

    # Função para remover um aluno de um grupo
    def remover_aluno_de_grupo():
        # Exibir os grupos disponíveis
        print("Grupos disponíveis:")
        for grupo in grupos:
            print(f"- Nome do Grupo: {grupo}")

        nome_grupo = input("Selecione o nome do grupo para remover um aluno: ")

        # Verificar se o grupo existe
        grupo_encontrado = grupos.get(nome_grupo)

        if grupo_encontrado:
            # Exibir os alunos no grupo
            alunos_no_grupo = grupo_encontrado['alunos']
            if not alunos_no_grupo:
                print(f"Grupo '{nome_grupo}' está vazio.")
            else:
                print(f"Alunos no grupo '{nome_grupo}':")
                for aluno in alunos_no_grupo:
                    print(f"- Nome do Aluno: {aluno['nome']} (RA: {aluno['ra']})")

                ra_aluno = input("Digite o RA do aluno para remover do grupo: ")

                # Verificar se o aluno está no grupo
                aluno_encontrado = None
                for aluno in alunos_no_grupo:
                    if aluno['ra'] == ra_aluno:
                        aluno_encontrado = aluno
                        break

                if aluno_encontrado:
                    grupo_encontrado['alunos'].remove(aluno_encontrado)
                    print(f"Aluno removido do grupo '{nome_grupo}'.")
                else:
                    print("Aluno não encontrado no grupo.")
        else:
            print("Grupo não encontrado.")