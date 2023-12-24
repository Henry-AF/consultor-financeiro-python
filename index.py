#Inicio do projeto que busca desenvolver um consultor para aplicações financeiras usando o ChatGPT

#Bibliotecas:

#yfinance, pandas, numpy, streamlit/matplotlib

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf


#Barra de navegação lateral
st.sidebar.title("Bem vindo ao PrimoGPT")
st.header("Pergunte ao PrimoGPT")

st.write("Seus problemas financeiros acabaram, pergunte para quem pratica o Skin in the Game:")

if "mensagem" not in st.session_state.keys():
    st.session_state.mensagem = [
        {"role": "assistent", "content": "Olá primo! Pergunte o que quiser!"}
    ]

for mensagem in st.session_state.mensagem:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

prompt_user = st.chat_input()

if prompt_user is not None:
    st.session_state.mensagem.append({"role": "assistent", "content": prompt_user})
    with st.chat_message("user"):
        st.write(prompt_user)



