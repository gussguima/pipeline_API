📊 Dashboard de Monitoramento do Preço do Bitcoin
📖 Sobre o Projeto
Este projeto consiste em um pipeline de dados e um dashboard interativo para monitorar o preço do Bitcoin (BTC) em tempo real.

O sistema é composto por dois componentes principais:

Coletor de Dados (main.py): Um script Python que, a cada 15 segundos, faz uma requisição à API da Coinbase para obter o preço atual do Bitcoin em dólares (USD). O dado coletado é então armazenado em um banco de dados PostgreSQL hospedado na nuvem (Render).

Dashboard Interativo (dashboard.py): Uma aplicação web desenvolvida com Streamlit que se conecta ao mesmo banco de dados para exibir os dados de forma visual. O dashboard apresenta um gráfico de linha com a evolução do preço ao longo do tempo e métricas chave como o preço atual, máximo e mínimo registrados.

🖼️ Visualização do Dashboard
(Sugestão: tire um print da sua tela com o dashboard rodando e substitua a imagem abaixo!)

✨ Funcionalidades
Coleta Contínua: O script main.py roda em um loop infinito, garantindo dados sempre atualizados.

Armazenamento Robusto: Utiliza SQLAlchemy para mapear os dados e salvá-los em um banco PostgreSQL.

Dashboard Interativo: Interface web amigável com Streamlit para fácil visualização e análise.

Gráficos Dinâmicos: Usa a biblioteca Plotly para criar um gráfico de linha que mostra a tendência dos preços.

Métricas em Destaque: Exibe cartões com o preço atual, máximo e mínimo para uma rápida consulta.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Banco de Dados: PostgreSQL (hospedado na Render)

API: Coinbase API v2

Coleta e Armazenamento:

requests: Para as chamadas de API.

SQLAlchemy: ORM para interagir com o PostgreSQL.

psycopg2-binary: Driver de conexão com o PostgreSQL.

Dashboard e Visualização:

Streamlit: Framework para criação do dashboard web.

Pandas: Para manipulação e análise dos dados.

Plotly Express: Para a criação de gráficos interativos.
