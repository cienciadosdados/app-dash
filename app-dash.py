import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import warnings

# Configuração para desativar mensagens de aviso
warnings.filterwarnings("ignore")

# Conexão com os dados
dados = pd.read_csv('bank-full.csv', delimiter=';')

# Função para criar o gráfico de rosca
def criar_grafico_rosca():
    # Agrupa os dados por "marital" e soma os valores de "balance"
    resumo = dados.groupby('marital')['balance'].sum().reset_index()

    # Cria o gráfico de rosca usando o Plotly
    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=resumo['marital'],
        values=resumo['balance'],
        hovertemplate='<b>%{label}</b> <br> Balance: %{value}',
        hole=0.4  # Define o tamanho do "buraco" no centro da rosca
    ))

    fig.update_layout(title='Sumarização de Balance por Marital')
    fig.update_layout(height=400)  # Define uma altura fixa para o gráfico

    return fig


# Função para criar o gráfico de barras
def criar_grafico_barras():
    # Agrupa os dados por "job" e "education" e soma os valores de "balance"
    resumo = dados.groupby(['job', 'education'])['balance'].sum().reset_index()

    # Ordena o resumo pelo "balance" em ordem decrescente
    resumo = resumo.sort_values('balance', ascending=False)

    # Cria o gráfico de barras usando o Plotly
    fig = px.bar(resumo, x='job', y='balance', color='education', title='Sumarização do Balance por Job e Education',
                 category_orders={'job': resumo['job'].tolist()})  # Ordena as categorias do eixo x
    fig.update_layout(height=400)  # Define uma altura fixa para o gráfico

    return fig


# Aplicação Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)  # Desativa mensagem de aviso



# Adiciona a imagem no topo do dashboard
st.image("https://cienciadosdados.com/images/logo/logo_aprovada-01.png", use_column_width=True)

st.title("Dashboard Gerencial")

# Cria um container para os gráficos
container = st.container()

# Exibe o gráfico de rosca no container
with container:
    st.subheader("Análise 1")
    fig_rosca = criar_grafico_rosca()
    st.plotly_chart(fig_rosca)

# Exibe o gráfico de barras no container
with container:
    st.subheader("Análise 2")
    fig_barras = criar_grafico_barras()
    st.plotly_chart(fig_barras)
