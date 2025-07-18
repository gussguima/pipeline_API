import requests
from time import sleep
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuração do banco de dados
DATABASE_URL = "postgresql://db_bitcoin_v03k_user:Ul1aWsJpksDAx6LGGiffjqVkpGjB4E3B@dpg-d1sgqqbe5dus739mqp40-a.ohio-postgres.render.com/db_bitcoin_v03k"

# Criação da engine e da sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Definição do modelo de dados
class BitcoinDados(Base):
    __tablename__ = "bitcoin_dados"
    
    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    moeda = Column(String(10))
    cotacao = Column(String(10))
    timestamp = Column(DateTime)

# Cria a tabela (se não existir)
Base.metadata.create_all(engine)

# Declarando as funções de request e response
def extract():
    # Extrai o JSON completo da API da Coinbase
    url = 'https://api.coinbase.com/v2/prices/spot'
    request = requests.get(url)
    return request.json()

def transform(dados_json):
    # Transforma os dados brutos da API e adiciona timestamp
    valor = float(dados_json['data']['amount'])
    moeda = dados_json['data']['base']
    cotacao = dados_json['data']['currency']
    response = BitcoinDados(
        valor=valor,
        moeda=moeda,
        cotacao=cotacao,
        timestamp=datetime.now()
    )
    return response

def saveData(dados):
    # Salva os dados no PostgreSQL usando SQLAlchemy
    with Session() as session:
        session.add(dados)
        session.commit()
        print("Dados salvos no PostgreSQL!")

if __name__ == "__main__":
    while True:
        # Extração e tratamento dos dados
        dados_json = extract()
        dados_tratados = transform(dados_json)

        # Salvar no PostgreSQL
        saveData(dados_tratados)

        # Pausar por 15 segundos
        print("Aguardando 15 segundos...")
        sleep(15)