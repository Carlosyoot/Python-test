import streamlit as st
import sqlite3

# Função para criar a tabela se não existir
def criar_tabela():
    conn = sqlite3.connect("salas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reunioes (
            id INTEGER PRIMARY KEY,
            sala TEXT,
            data DATE,
            participantes TEXT
        )
    """)
    conn.commit()
    conn.close()

# Função para registrar a reunião
def registrar_reuniao(sala, data, participantes):
    conn = sqlite3.connect("salas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reunioes (sala, data, participantes) VALUES (?, ?, ?)",
                   (sala, data, participantes))
    conn.commit()
    conn.close()

# Função para recuperar as reuniões de uma sala específica
def obter_reunioes(sala):
    conn = sqlite3.connect("salas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reunioes WHERE sala=?", (sala,))
    reunioes = cursor.fetchall()
    conn.close()
    return reunioes

# Criar a tabela se não existir
criar_tabela()

st.title("Monitoramento de Salas de Reunião")

sala = st.selectbox("Selecione a sala:", ["Sala A", "Sala B", "Sala C"])
data = st.date_input("Data da reunião:")
participantes = st.text_area("Participantes (separados por vírgula):")

# Definir um identificador exclusivo para o botão baseado na sala selecionada
botao_id = f"registrar_reuniao_{sala}"

# Usar o botão com o identificador exclusivo
if st.button("Registrar Reunião", key=botao_id):
    registrar_reuniao(sala, data, participantes)
    st.success("Reunião registrada com sucesso!")

# Obter e exibir as reuniões registradas para a sala selecionada
reunioes = obter_reunioes(sala)
if reunioes:
    st.write(f"Reuniões na {sala}:")
    for reuniao in reunioes:
        st.write(f"- Data: {reuniao[2]}, Participantes: {reuniao[3]}")
else:
    st.write(f"Nenhuma reunião encontrada na {sala}.")
