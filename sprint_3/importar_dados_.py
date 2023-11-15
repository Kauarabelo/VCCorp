import pandas as pd
import json


def excel_para_json(nome_arquivo_excel):
    # Carregar o arquivo Excel
    df = pd.read_excel(nome_arquivo_excel, sheet_name='alunos')  # Substitua 'alunos' pelo nome da sua planilha no arquivo Excel

    # Converter o DataFrame do pandas para um dicionário
    dados_json = {"alunos": {}}
    for index, row in df.iterrows():
        aluno = {
            "ra": row['ra'],
            "nome": row['nome'],
            "idade": str(row['idade']),
            "email": row['email'],
            "turmas": [],
            "grupos": []
        }
        dados_json["alunos"][f"Ra{index + 1}"] = aluno  # Adicionando alunos com chaves únicas (Ra1, Ra2, etc.)

    # Salvar os dados no formato JSON
    with open('dados_alunos.json', 'w') as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=4)

# Chamada da função para importar o arquivo Excel e transformar em JSON
def iniciar_importacao():
    nome_arquivo_excel = input('Copie e cole o caminho do seu arquivo .xlsx, no seguinte formato: \n caminho/do/seu/arquivo.xlsx')  
    excel_para_json(nome_arquivo_excel)
