import sqlite3
import streamlit as st

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

st.title("Monitoramento de Salas de Reunião")

sala = st.selectbox("Selecione a sala:", ["Sala A", "Sala B", "Sala C"])
data = st.date_input("Data da reunião:")
participantes = st.text_area("Participantes (separados por vírgula):")

if st.button("Registrar Reunião"):
    cursor.execute("INSERT INTO reunioes (sala, data, participantes) VALUES (?, ?, ?)",
                   (sala, data, participantes))
    conn.commit()
    st.success("Reunião registrada com sucesso!")

# Exiba as reuniões registradas
cursor.execute("SELECT * FROM reunioes WHERE sala=?", (sala,))
reunioes = cursor.fetchall()

if reunioes:
    st.write("Reuniões na", sala)
    for reuniao in reunioes:
        st.write(f"- Data: {reuniao[2]}, Participantes: {reuniao[3]}")
else:
    st.write(f"Nenhuma reunião encontrada na {sala}.")

conn.close()

st.title("Monitoramento de Salas de Reunião")

sala = st.selectbox("Selecione a sala:", ["Sala A", "Sala B", "Sala C"])
data = st.date_input("Data da reunião:")
participantes = st.text_area("Participantes (separados por vírgula):")

if st.button("Registrar Reunião"):
    cursor.execute("INSERT INTO reunioes (sala, data, participantes) VALUES (?, ?, ?)",
                   (sala, data, participantes))
    conn.commit()
    st.success("Reunião registrada com sucesso!")

# Exiba as reuniões registradas
cursor.execute("SELECT * FROM reunioes WHERE sala=?", (sala,))
reunioes = cursor.fetchall()

if reunioes:
    st.write("Reuniões na", sala)
    for reuniao in reunioes:
        st.write(f"- Data: {reuniao[2]}, Participantes: {reuniao[3]}")
else:
    st.write(f"Nenhuma reunião encontrada na {sala}.")

conn.close()
