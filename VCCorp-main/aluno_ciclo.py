import tkinter as tk
import json

# Função para adicionar um ciclo e campos de notas correspondentes
def adicionar_ciclo():
    ciclo = ciclo_entry.get()
    if ciclo:
        ciclos_listbox.insert(tk.END, ciclo)
        ciclos_entry_list.append(ciclo)
        ciclo_entry.delete(0, tk.END)
        criar_campos_notas(ciclo)

# Função para coletar as notas dos alunos
def coletar_notas():
    nome_aluno = nome_entry.get()
    notas_aluno = []

    for ciclo in ciclos_entry_list:
        trab1 = float(trab1_entries[ciclo].get())
        trab2 = float(trab2_entries[ciclo].get())
        p1 = float(p1_entries[ciclo].get())
        p2 = float(p2_entries[ciclo].get())

        if ciclo.strip().lower() == 'português':
            nota_final = (trab1 + p1 / 2) / 2 + (trab2 + p2 / 2) / 2
        else:
            nota_final = (trab1 + p1 / 2) / 2 + (trab2 + p2 / 2) / 2

        notas_aluno.append({
            'Ciclo': ciclo,
            'Nota Final': nota_final
        })

    aluno = {
        'Nome': nome_aluno,
        'Notas': notas_aluno
    }

    alunos.append(aluno)

    # Limpar campos de entrada
    nome_entry.delete(0, tk.END)
    for ciclo in ciclos_entry_list:
        trab1_entries[ciclo].delete(0, tk.END)
        trab2_entries[ciclo].delete(0, tk.END)
        p1_entries[ciclo].delete(0, tk.END)
        p2_entries[ciclo].delete(0, tk.END)
    ciclos_listbox.delete(0, tk.END)

# Função para exibir informações dos alunos
def exibir_notas():
    resultado_text.config(state=tk.NORMAL)
    resultado_text.delete(1.0, tk.END)

    for aluno in alunos:
        resultado_text.insert(tk.END, f"Nome: {aluno['Nome']}\n")
        for nota in aluno['Notas']:
            resultado_text.insert(tk.END, f"Ciclo: {nota['Ciclo']}, Nota Final: {nota['Nota Final']}\n")
    
    resultado_text.config(state=tk.DISABLED)

# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Notas")

# Lista para armazenar os alunos
alunos = []

# Campos de entrada para o nome do aluno
nome_label = tk.Label(janela, text="Nome do Aluno:")
nome_label.pack()
nome_entry = tk.Entry(janela)
nome_entry.pack()

# Lista de ciclos
ciclos_label = tk.Label(janela, text="Ciclos:")
ciclos_label.pack()

ciclo_entry = tk.Entry(janela)
ciclo_entry.pack()
adicionar_ciclo_button = tk.Button(janela, text="Adicionar Ciclo", command=adicionar_ciclo)
adicionar_ciclo_button.pack()

ciclos_listbox = tk.Listbox(janela)
ciclos_listbox.pack()

# Campos de entrada para as notas
ciclos_entry_list = []
trab1_entries = {}
trab2_entries = {}
p1_entries = {}
p2_entries = {}

def criar_campos_notas(ciclo):
    ciclo_frame = tk.Frame(janela)
    ciclo_frame.pack()
    ciclo_label = tk.Label(ciclo_frame, text=f"{ciclo}:")
    ciclo_label.pack(side=tk.LEFT)
    
    trab1_entry = tk.Entry(ciclo_frame)
    trab1_entry.pack(side=tk.LEFT)
    trab1_entries[ciclo] = trab1_entry

    trab2_entry = tk.Entry(ciclo_frame)
    trab2_entry.pack(side=tk.LEFT)
    trab2_entries[ciclo] = trab2_entry

    p1_entry = tk.Entry(ciclo_frame)
    p1_entry.pack(side=tk.LEFT)
    p1_entries[ciclo] = p1_entry

    p2_entry = tk.Entry(ciclo_frame)
    p2_entry.pack(side=tk.LEFT)
    p2_entries[ciclo] = p2_entry

# Botão para coletar notas
coletar_notas_button = tk.Button(janela, text="Coletar Notas", command=coletar_notas)
coletar_notas_button.pack()

# Botão para exibir notas
exibir_notas_button = tk.Button(janela, text="Exibir Notas", command=exibir_notas)
exibir_notas_button.pack()

# Área de texto para exibir resultados
resultado_text = tk.Text(janela, height=10, width=50, state=tk.DISABLED)
resultado_text.pack()

# Iniciar a interface gráfica
janela.mainloop()
