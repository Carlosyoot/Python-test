import streamlit as st
from streamlit.components.v1 import html

def sidebar_with_calendar():
    # Adiciona uma barra lateral com título "Calendário"
    st.sidebar.title("Calendário")
    
    # Adiciona um ícone de calendário usando HTML
    html("""
    <div style="display: flex; align-items: center; padding: 10px;">
        <img src="https://image.flaticon.com/icons/png/512/1177/1177568.png" alt="Calendário" style="width:24px;height:24px;">
        <span style="margin-left: 10px;">23 de Fevereiro de 2024</span>
    </div>
    """)

def main():
    st.title("App com Barra Lateral e Ícone de Calendário")
    sidebar_with_calendar()

if __name__ == "__main__":
    main()
