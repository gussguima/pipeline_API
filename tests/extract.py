# %%
import requests
import time

def extract():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def transform(dados_json):
    valor = (dados_json['data']['amount'])
    moeda = dados_json['data']['base']
    cotação = dados_json['data']['currency']
    dados_tratados = {
        "valor": valor,
        "moeda": moeda,
        "cotação": cotação
    }
    
    return dados_tratados

# %%
if __name__ == "__main__":
    while True:
        dados_json = extract()
        dados_tratados = transform(dados_json)
        print(dados_tratados)
        time.sleep(5)