import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração do logotipo
st.sidebar.image("logo.png", use_column_width=True)  # Insira o caminho para o logotipo

# Menu de navegação
menu = st.sidebar.radio("Navegação", ["Home",  "Dashboard",])

if menu == "Home":
    st.title("Página Inicial")
    st.write("Bem-vindo ao sistema de análise de questões do ENEM!")


elif menu == "Dashboard":
    st.title("Dashboard ENEM - Ocorrência de Questões por Assunto")

    data = {
    "Disciplina": ["Química", "Química","Química", "Química","Química","Química","Química",
                   "Química","Química","Química","Química","Química","Química","Química","Química","Química","Química","Língua Portuguesa"],
    "Assunto": [
        "Reações Orgânicas", "Assuntos variados", "Equilíbrio químico","Gases","Estequiometria",
        "Eletroquímica","Soluções","Grandezas Químicas","Termoquímica", "Radioatividade", "Teoria de Ácido e Base","Cinética",
        "Propriedades Coligativas","Reações Inorgânicas","Geometria Molecular","Ligações químicas","Atomística","Interpretação Textual"
        
    ],
    "Ano": [2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024,2024],
    "Percentual de Ocorrência (%)": [20, 17.30, 13, 6.57, 6.57, 6.57, 6.1, 4.25, 4.25, 4.25, 4.25, 2.13, 2.13, 2.13, 2.13, 2.13, 2.13,
                                     20],
    "Número de Questões": [9, 8, 6, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1,9]
    }
    df = pd.DataFrame(data)

    # Filtros no dashboard
    disciplina_selecionada = st.sidebar.selectbox("Selecione a Disciplina", options=df["Disciplina"].unique())
    ano_selecionado = st.sidebar.selectbox("Selecione o Ano", options=df["Ano"].unique())

    # Filtra os dados com base nas seleções
    df_filtrado = df[(df["Disciplina"] == disciplina_selecionada) & (df["Ano"] == ano_selecionado)]
    
    st.subheader(f"Análise de Questões - {disciplina_selecionada} ({ano_selecionado})")
    st.dataframe(df_filtrado)

     # Filtro de assunto baseado na disciplina e ano selecionados
    assunto_selecionado = st.sidebar.selectbox("Selecione o Assunto", options=df_filtrado["Assunto"].unique())
    df_assunto = df_filtrado[df_filtrado["Assunto"] == assunto_selecionado]
    
    # Mostrando informações filtradas
    st.subheader("Dados Filtrados")
    st.write(f"Disciplina Selecionada: {disciplina_selecionada}")
    st.write(f"Ano Selecionado: {ano_selecionado}")
    st.write(f"Assunto Selecionado: {assunto_selecionado}")
    st.dataframe(df_assunto)
    

    # Gráfico comparativo por assunto
    fig, ax = plt.subplots()
    assuntos = df_filtrado["Assunto"].unique()
    cores = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6"]

    for i, assunto in enumerate(assuntos):
        questoes = df_filtrado[df_filtrado["Assunto"] == assunto]["Número de Questões"].values[0]
        ax.bar(assunto, questoes, color=cores[i % len(cores)])

    ax.set_xlabel("Assunto")
    ax.set_ylabel("Número de Questões")
    plt.xticks(rotation=45)
    st.pyplot(fig)

