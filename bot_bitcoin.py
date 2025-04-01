import ssl
import json

import websocket
import bitstamp.client
import os

# Credenciais (use variáveis de ambiente)
USERNAME = os.environ.get("BITSTAMP_USERNAME")
KEY = os.environ.get("BITSTAMP_KEY")
SECRET = os.environ.get("BITSTAMP_SECRET")

def cliente():
    return bitstamp.client.Trading(username=USERNAME, key=KEY, secret=SECRET)

def comprar(quantidade):
    try:
        trading_client = cliente()
        trading_client.buy_market_order(quantidade)
        print(f"Compra de {quantidade} BTC realizada com sucesso!")
    except Exception as e:
        print(f"Erro ao comprar: {e}")

def vender(quantidade):
    try:
        trading_client = cliente()
        trading_client.sell_market_order(quantidade)
        print(f"Venda de {quantidade} BTC realizada com sucesso!")
    except Exception as e:
        print(f"Erro ao vender: {e}")

def ao_abrir(ws):
    print("Conexão WebSocket aberta")
    json_subscribe = """
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    """
    ws.send(json_subscribe)

def ao_fechar(ws, close_status_code, close_msg):
    print(f"Conexão WebSocket fechada: {close_status_code} {close_msg}")

def erro(ws, error):
    print(f"Erro no WebSocket: {error}")

def ao_receber_mensagem(ws, mensagem):
    try:
        mensagem = json.loads(mensagem)
        price = float(mensagem['data']['price'])
        print(f"Preço BTC/USD: {price}")
        quantidade = 0.001 #quantidade de btc para comprar ou vender

        if price > 10000:
            vender(quantidade)
        elif price < 8100:
            comprar(quantidade)
        else:
            print("Aguardando...")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        "wss://ws.bitstamp.net.",
        on_open=ao_abrir,
        on_close=ao_fechar,
        on_message=ao_receber_mensagem,
        on_error=erro,
    )
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})