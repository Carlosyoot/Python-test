import streamlit as st
import pandas as pd
import sqlite3
import calendar

# Conectar-se ao banco de dados
conn = sqlite3.connect("salas.db")
cursor = conn.cursor()

# Crie a tabela para armazenar as reuniões
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reunioes (
        id INTEGER PRIMARY KEY,
        sala TEXT,
        data DATE,
        participantes TEXT
    )
""")

conn.commit()

# Sidebar com calendário
st.sidebar.title("Calendário")
selected_date = st.sidebar.date_input("Selecione uma data:")

# Exiba as reuniões marcadas no calendário
cursor.execute("SELECT data, participantes FROM reunioes")
reunioes = cursor.fetchall()

df = pd.DataFrame(reunioes, columns=["Data", "Participantes"])
df["Data"] = pd.to_datetime(df["Data"])
df["Dia"] = df["Data"].dt.day
df["Mês"] = df["Data"].dt.month
df["Ano"] = df["Data"].dt.year

calendario = calendar.month(df["Ano"].max(), df["Mês"].max())
dias_marcados = df[df["Mês"] == selected_date.month]["Dia"].tolist()

for semana in calendario:
    for dia in semana:
        if dia == 0:
            st.sidebar.write(" ", end="  ")
        elif dia in dias_marcados:
            st.sidebar.write(f"{dia}", end="  ")
        else:
            st.sidebar.write(dia, end="  ")

# Exiba informações sobre a reunião selecionada
if selected_date.day in dias_marcados:
    st.sidebar.write(f"### Reunião em {selected_date.strftime('%d/%m/%Y')}")
    reuniao_selecionada = df[df["Dia"] == selected_date.day]
    for _, row in reuniao_selecionada.iterrows():
        st.sidebar.write(f"- Participantes: {row['Participantes']}")

# Fechar a conexão com o banco de dados
conn.close()
