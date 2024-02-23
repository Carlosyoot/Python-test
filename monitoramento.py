
import sqlite3
import streamlit as pd

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

