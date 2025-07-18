import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://db_bitcoin_v03k_user:Ul1aWsJpksDAx6LGGiffjqVkpGjB4E3B@dpg-d1sgqqbe5dus739mqp40-a.ohio-postgres.render.com/db_bitcoin_v03k"

def ler_dados_postgres():
    # Lê os dados do banco PostgreSQL e retorna como DataFrame
    try:
        engine = create_engine(DATABASE_URL)
        query = "SELECT * FROM bitcoin_dados ORDER BY timestamp DESC"
        
        # O pandas usa o engine para conectar, executar a query e fechar a conexão
        df = pd.read_sql(query, engine)
        
        return df
    except Exception as e:
        st.error(f"Erro ao conectar ao PostgreSQL: {e}")
        return pd.DataFrame()

def main():
    st.set_page_config(page_title="Dashboard de Preços do Bitcoin", layout="wide")
    st.title("📊 Dashboard de Preços do Bitcoin")
    st.write("Este dashboard exibe os dados do preço do Bitcoin coletados periodicamente de um banco PostgreSQL.")

    df = ler_dados_postgres()

    if not df.empty:
        st.subheader("📋 Dados Recentes")
        st.dataframe(df.head())

        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values(by='timestamp')

        st.subheader("📈 Evolução do Preço do Bitcoin")

        fig = px.line(
            df, 
            x='timestamp', 
            y='valor', 
            title='Preço do Bitcoin ao Longo do Tempo',
            labels={'timestamp': 'Data', 'valor': 'Preço (USD)'}
        )
        
        fig.update_layout(
            xaxis_title='Data',
            yaxis_title='Preço (USD)',
            title_x=0.5,
            template='plotly_white'
        )
        
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🔢 Estatísticas Gerais")
        col1, col2, col3 = st.columns(3)
        col1.metric("Preço Atual", f"${df['valor'].iloc[-1]:,.2f}")
        col2.metric("Preço Máximo", f"${df['valor'].max():,.2f}")
        col3.metric("Preço Mínimo", f"${df['valor'].min():,.2f}")
    else:
        st.warning("Nenhum dado encontrado no banco de dados PostgreSQL.")

if __name__ == "__main__":
    main()