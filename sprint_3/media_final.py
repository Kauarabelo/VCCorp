import json

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

def calcular_media_ponderada():
    while True:
        dados = carregar_dados()
        notas = dados.get('notas', {})
    
        media_por_aluno = {}
    
        for nota_id, nota in notas.items():
            aluno_ra = nota['aluno_ra']
            ciclo_id = nota['ciclo_id']
            score = nota['score']
            peso_ciclo = dados['ciclos'][ciclo_id]['peso_da_nota']
    
            if aluno_ra not in media_por_aluno:
                media_por_aluno[aluno_ra] = {'total_score': 0, 'total_peso': 0}
    
            media_por_aluno[aluno_ra]['total_score'] += float(score) * float(peso_ciclo)
            media_por_aluno[aluno_ra]['total_peso'] += float(peso_ciclo)
    
        for aluno_ra, media_info in media_por_aluno.items():
            total_score = media_info['total_score']
            total_peso = media_info['total_peso']
            
            if total_peso == 0:
                media_final = 0
            else:
                media_final = total_score / total_peso
            
            media_por_aluno[aluno_ra]['fee'] = round(media_final, 2)
    
        # Salva as médias ponderadas em um arquivo JSON
        with open('dados.json', 'w') as arquivo_json:
            json.dump(media_por_aluno, arquivo_json, indent=4)
    
        print("Médias calculadas e salvas")
    
        opcao = input("Deseja calcular as médias de outros alunos? (s/n): ").lower()
        if opcao != 's':
            break
