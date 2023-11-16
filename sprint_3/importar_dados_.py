import os
import openpyxl
import json

def excel_para_json(nome_arquivo_excel):
    # Carregar o arquivo Excel
    workbook = openpyxl.load_workbook(nome_arquivo_excel)
    sheet = workbook['alunos']  # Substitua 'alunos' pelo nome da sua planilha no arquivo Excel

    # Converter os dados para um formato que pode ser convertido em JSON
    dados_json = {"alunos": {}}
    contador = 1
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Começando da segunda linha, considerando cabeçalhos na primeira
        # Verificar se pelo menos uma célula na linha está preenchida
        if any(value is not None and value != '' for value in row):
            aluno = {
                "ra": row[0],
                "nome": row[1],
                "idade": str(row[2]),
                "email": row[3],
                "turmas": [],
                "grupos": []
            }
            dados_json["alunos"][f"Ra{contador}"] = aluno  # Utilizando um contador para criar chaves únicas (Ra1, Ra2, etc.)
            contador += 1

    # Salvar os dados no formato JSON
    with open('dadoss.json', 'w') as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=4)
        print('Importação salva com sucesso')

# Chamada da função para importar o arquivo Excel e transformar em JSON
def iniciar_importacao():
    nome_arquivo = input('Digite o nome do seu arquivo .xlsx (sem o caminho): ')  # Solicita apenas o nome do arquivo
    nome_arquivo_excel = os.path.join(os.getcwd(), f"{nome_arquivo}.xlsx")  # Adiciona o caminho do diretório atual ao nome do arquivo
    excel_para_json(nome_arquivo_excel)
