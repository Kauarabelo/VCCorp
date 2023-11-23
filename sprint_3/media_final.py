import json
from cadastrar_notas import func_cadastrar_notas

def calcular_media_ponderada():
    global dados
    notas = dados.get('notas', {})

    total_pesos = 0
    soma_notas_pesadas = 0

    for nota_id, nota in notas.items():
        peso_ciclo = float(nota['ciclo']['peso_da_nota'])
        score = float(nota['score'])

        total_pesos += peso_ciclo
        soma_notas_pesadas += (score * peso_ciclo)

    if total_pesos == 0:
        return 0  # Evitar divisão por zero

    media_ponderada = soma_notas_pesadas / total_pesos
    return round(media_ponderada, 2)

# Carrega os dados do arquivo JSON
with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)

# Calcula a média ponderada
media_ponderada_fee = calcular_media_ponderada()

# Exibe o resultado
print(f'A média ponderada (fee) é: {media_ponderada_fee}')
