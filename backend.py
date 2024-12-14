import requests

def obter_preco_bitcoin_binance():
    """Obtém o preço atual do Bitcoin em reais na Binance."""
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCBRL"
    resposta = requests.get(url)
    dados = resposta.json()
    return float(dados['price'])

def calcular(valor_reais, desconto_percentual, fee_rede):
    """Calcula a quantidade líquida de satoshis."""
    try:
        valor_reais = float(valor_reais or 0)
        desconto_percentual = float(desconto_percentual or 0)
        fee_rede = float(fee_rede or 0)

        preco_btc_brl = obter_preco_bitcoin_binance()

        # Aplicar os descontos
        valor_liquido = valor_reais * (1 - desconto_percentual / 100) * (1 - fee_rede / 100)

        # Calcular a quantidade de satoshis
        btc_recebido = valor_liquido / preco_btc_brl
        satoshis_recebidos = btc_recebido * 1e8  # 1 BTC = 100 milhões de satoshis

        return f"{int(satoshis_recebidos):,} satoshis"
    except Exception:
        return "Erro: Verifique os valores inseridos."
