import json

def calcular_media_ponderada():
    notas = dados.get('notas', {})
    
    total_pesos = 0
    soma_notas_pesadas = 0

    for nota in notas.values():
        peso_ciclo = float(nota['ciclo']['peso_da_nota'])
        score = float(nota['score'])

        total_pesos += peso_ciclo
        soma_notas_pesadas += (score * peso_ciclo)

    if total_pesos == 0:
        return 0  # Evitar divisão por zero

    media_ponderada = soma_notas_pesadas / total_pesos
    return round(media_ponderada, 2)

# Carrega os dados do arquivo JSON
try:
    with open('dados.json', 'r') as arquivo_json:
        dados = json.load(arquivo_json)
except FileNotFoundError:
    print('Arquivo "dados.json" não encontrado. Certifique-se de que o arquivo existe.')
    exit(1)

# Verifica se existem notas nos dados
if 'notas' not in dados:
    print('Não há notas disponíveis para calcular a média ponderada.')
    exit(1)

# Calcula a média ponderada
media_ponderada_fee = calcular_media_ponderada()

# Exibe o resultado
print(f'A média ponderada (fee) é: {media_ponderada_fee}')
