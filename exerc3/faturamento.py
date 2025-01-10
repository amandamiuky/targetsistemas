import json

def carregar_dados_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def analisa_faturamento(faturamento):
    dias_com_faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    
    if not dias_com_faturamento:
        return "Não há dados de faturamento válido."

    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_media

caminho_arquivo = '/home/miuky/Documents/eu/processo/exerc3/dados.json' 

faturamento_diario = carregar_dados_faturamento(caminho_arquivo)

menor, maior, dias_acima_media = analisa_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: R${menor}")
print(f"Maior valor de faturamento: R${maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
