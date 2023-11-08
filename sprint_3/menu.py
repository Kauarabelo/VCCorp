import json
from cadastrar_aluno import func_cadastrar_alunos
from cadastrar_turmas import func_cadastrar_turmas
from cadastrar_grupos import func_cadastrar_grupos
from cadastrar_ciclo import func_cadastrar_ciclos
from cadastrar_notas import func_cadastrar_notas
from editar_alunos import editar_aluno
from editar_turmas import editar_turma
from editar_grupos import editar_grupo
from editar_ciclos import editar_ciclo  
from editar_notas import editar_nota

def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        dados = {
            "alunos": {},
            "turmas": {},
            "ciclos": {},
            "grupos": {},
            "notas": {}
        }
    return dados

while True:
    print("\n" * 2)
    print("Olá administrador!😊 Bem-vindo (a) ao sistema de informação da PBLTex!😄")
    menu_opcao1 = input("O que você gostaria de acessar?\n1 - Alunos\n2 - Turmas\n3 - Grupos de Alunos\n4 - Ciclos\n5 - Notas\n6 - Sair\n")

    if menu_opcao1 == "1":
        menu_opcao2 = input("Qual ação você quer fazer?\nA - Cadastrar\nB - Editar\n0 - Voltar\n").strip().lower()
        if menu_opcao2 == "a":
            if func_cadastrar_alunos():
                print("\nRetornando ao menu principal.")
            else:
                print("\nO cadastro foi cancelado.\nRetornando ao menu principal.")
        elif menu_opcao2 == "b":
            ra_aluno = input("Informe o RA do aluno que você quer editar: ")
            if editar_aluno(ra_aluno):
                print("\nRetornando ao menu principal.")
            else:
                print("\nA edição foi cancelada.\nRetornando ao menu principal.")
        elif menu_opcao2 == "0":
            continue
        else:
            print("Opção inválida. Saindo.")

    elif menu_opcao1 == "2":
        menu_opcao2 = input("Qual ação você quer fazer?\nA - Cadastrar\nB - Editar\n0 - Voltar\n").strip().lower()
        if menu_opcao2 == "a":
            if func_cadastrar_turmas():
                print("\nRetornando ao menu principal.")
        elif menu_opcao2 == "b":
            if editar_turma():
                print("\nRetornando ao menu principal.")
        elif menu_opcao2 == "0":
            continue
        else:
            print("Opção inválida. Saindo.")

    elif menu_opcao1 == "3":
        menu_opcao2 = input("Qual ação você quer fazer?\nA - Cadastrar\nB - Editar\n0 - Voltar\n").strip().lower()
        if menu_opcao2 == "a":
            if func_cadastrar_grupos():
                print("\nRetornando ao menu principal.")
        elif menu_opcao2 == "b":
            if editar_grupo():
                print("\nRetornando ao menu principal.")
        elif menu_opcao2 == "0":
            continue
        else:
            print("Opção inválida. Saindo.")

    elif menu_opcao1 == "4":
        menu_opcao2 = input("Qual ação você quer fazer?\nA - Cadastrar\nB - Editar\n0 - Voltar\n").strip().lower()
        if menu_opcao2 == "a":
            if func_cadastrar_ciclos():
                print("\nRetornando ao menu principal.")
        elif menu_opcao2 == "b":
            if editar_ciclo():
                print("\nRetornando ao menu principal.")
        elif menu_opcao2 == "0":
            continue
        else:
            print("Opção inválida. Saindo.")
            
    elif menu_opcao1 == "5":
        menu_opcao2 = input("Qual ação você quer fazer?\nA - Cadastrar\nB - Editar\n0 - Voltar\n").strip().lower()
        if menu_opcao2 == "a":
            if func_cadastrar_notas():
                print("\nRetornando ao menu principal.")
        elif menu_opcao2 == "b":
            if editar_nota():
                print("\nRetornando ao menu principal.")
        elif menu_opcao2 == "0":
            continue
        else:
            print("Opção inválida. Saindo.")

    elif menu_opcao1 == "6":
        break
    else:
        print("Opção inválida. Saindo.")