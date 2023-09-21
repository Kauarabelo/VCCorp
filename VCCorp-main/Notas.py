alunos = [] 

for _ in range(2):
    nome_aluno = str(input("Insira o nome do aluno: "))
    notas_aluno = []

    for _ in range(2):
        materia = str(input("Insira a matéria: ")) # 9 matérias no total
        trab1 = float(input("Quanto o aluno tirou no primeiro trabalho (0-5)? "))
        trab2 = float(input("Quanto o aluno tirou no segundo trabalho (0-5)? "))
        p1 = float(input("Quanto o aluno tirou na primeira prova (0-10)? "))
        p2 = float(input("Quanto o aluno tirou na segunda prova (0-10)? "))

        if materia.strip().lower() == 'português':
            nota_final = (trab1 + p1 / 2) / 2 + (trab2 + p2 / 2) / 2
        else:
            nota_final = (trab1 + p1 / 2) / 2 + (trab2 + p2 / 2) / 2

        notas_aluno.append({
            'Matéria': materia,
            'Nota Final': nota_final
        })

    aluno = {
        'Nome': nome_aluno,
        'Notas': notas_aluno
    }

    alunos.append(aluno) 

for aluno in alunos: 
    print(f"Nome: {aluno['Nome']}")
    for nota in aluno['Notas']:
        print(f"Matéria: {nota['Matéria']}, Nota Final: {nota['Nota Final']}")


