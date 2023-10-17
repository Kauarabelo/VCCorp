import tkinter as tk
import json

#Função para adicionar ciclos
def adicionar_ciclo():
    ciclo = ciclo_entry.get()
    if ciclo:
        ciclos_listbox.insert(tk.END, ciclo)
        ciclos_entry_list.append(ciclo)
        ciclo_entry.delete(0, tk.END)
        criar_campo_notas(ciclo)

#Função para coletar as notas dos alunos e calcular a média ponderada
def coletar_notas():
    nome_aluno = nome_entry.get()
    notas_aluno = []

    #Coletar os pesos dos ciclos
    pesos = {}
    for ciclo in ciclos_entry_list:
        peso = peso_entries[ciclo].get()
        pesos[ciclo] = int(peso) if peso else 1.0

    for ciclo in ciclos_entry_list:
        nota_ciclo = float(nota_ciclo_entries[ciclo].get())
        notas_aluno.append({
            'Ciclo': ciclo,
            'Nota': nota_ciclo
        })

    #Calcular a média ponderada
    soma_notas = sum(nota['Nota'] * pesos[ciclo] for ciclo, nota in zip(ciclos_entry_list, notas_aluno))
    soma_pesos = sum(pesos.values())
    if soma_pesos == 0:
        media_ponderada = 0.0
    else:
        media_ponderada = soma_notas / soma_pesos

    aluno = {
        'Nome': nome_aluno,
        'Notas': notas_aluno,
        'Média Ponderada': media_ponderada
    }

    alunos.append(aluno)

    #Limpar campos de entrada
    nome_entry.delete(0, tk.END)
    for ciclo in ciclos_entry_list:
        nota_ciclo_entries[ciclo].delete(0, tk.END)
        peso_entries[ciclo].delete(0, tk.END)
    ciclos_listbox.delete(0, tk.END)

#Função para exibir informações dos alunos
def exibir_notas():
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)

    for aluno in alunos:
        resultado_text.insert(tk.END, f"Nome: {aluno['Nome']}\n")
        for nota in aluno['Notas']:
            resultado_text.insert(tk.END, f"Ciclo: {nota['Ciclo']}, Nota: {nota['Nota']}\n")
        resultado_text.insert(tk.END, f"Média Ponderada: {aluno['Média Ponderada']}\n")
    
    resultado_text.config(state=tk.DISABLED)

#Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Notas")

#Lista para armazenar os alunos
alunos = []

#Campos de entrada para o nome do aluno
nome_label = tk.Label(janela, text="Nome do Aluno:")
nome_label.pack()
nome_entry = tk.Entry(janela)
nome_entry.pack()

#Campos de entrada para os ciclos
ciclos_label = tk.Label(janela, text="Ciclos:")
ciclos_label.pack()

ciclo_entry = tk.Entry(janela)
ciclo_entry.pack()
adicionar_ciclo_button = tk.Button(janela, text="Adicionar Ciclo", command=adicionar_ciclo)
adicionar_ciclo_button.pack()

ciclos_listbox = tk.Listbox(janela)
ciclos_listbox.pack()

#Campos de entrada para as notas
ciclos_entry_list = []
nota_ciclo_entries = {}
peso_entries = {}

def criar_campo_notas(ciclo):
    ciclo_frame = tk.Frame(janela)
    ciclo_frame.pack()
    ciclo_label = tk.Label(ciclo_frame, text=f"{ciclo}:")
    ciclo_label.pack(side=tk.LEFT)
    
    nota_ciclo_entry = tk.Entry(ciclo_frame)
    nota_ciclo_entry.pack(side=tk.LEFT)
    nota_ciclo_entries[ciclo] = nota_ciclo_entry

    peso_entry = tk.Entry(ciclo_frame)
    peso_entry.pack(side=tk.LEFT)
    peso_entries[ciclo] = peso_entry

#Botão para coletar notas
coletar_notas_button = tk.Button(janela, text="Coletar Notas", command=coletar_notas)
coletar_notas_button.pack()

#Botão para exibir notas
exibir_notas_button = tk.Button(janela, text="Exibir Notas", command=exibir_notas)
exibir_notas_button.pack()

#Área de texto para exibir resultados
resultado_text = tk.Text(janela, height=10, width=50, state=tk.DISABLED)
resultado_text.pack()

#Função para criar o arquivo JSON com as notas dos alunos
def criar_json():
    if not alunos:
        return

    arquivo_json = []

    #Verificar se o arquivo JSON já existe
    try:
        with open('notas_alunos.json', 'r') as json_file:
            arquivo_json = json.load(json_file)
    except FileNotFoundError:
        arquivo_json = []

    for aluno in alunos:
        nome_aluno = aluno['Nome']
        notas = aluno['Notas']
        media_ponderada = aluno['Média Ponderada']
        arquivo_json.append({
            'nome': nome_aluno,
            'notas': notas,
            'média ponderada': media_ponderada
        })

    with open('notas_alunos.json', 'w') as json_file:
        json.dump(arquivo_json, json_file, indent=4)

    resultado_text.config(state=tk.NORMAL)
    resultado_text.insert(tk.END, "Novas notas adicionadas ao arquivo JSON: 'notas_alunos.json'\n")
    resultado_text.config(state=tk.DISABLED)

#Botão para criar arquivo JSON com as notas
criar_json_button = tk.Button(janela, text="Criar JSON das Notas dos Alunos", command=criar_json)
criar_json_button.pack()

#Iniciar a interface gráfica
janela.mainloop()
