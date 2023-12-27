#Inicio do projeto que busca desenvolver um consultor para aplicações financeiras usando o ChatGPT

#Bibliotecas:

#yfinance, pandas, numpy, streamlit/matplotlib

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf

#Modelo Lanchain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from decouple import config


prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""Você é um consultor de finanças chamado "Primo Rico" sendo uma IA gentil, 
                 Estará falando com seres humanos, responda-os de modo amigável, e apresentando soluções eficientes para as perguntas.
                 
                 chat_history: {chat_history}
                 
                Humano: {question}    
                
                AI: """
)


llm = ChatOpenAI(openai_api_key=config("OPEN_AI_KEY"))
memory = ConversationBufferWindowMemory(memory_key="chat_history")
llm_chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt    
)


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
    st.session_state.mensagem.append({"role": "user", "content": prompt_user})
    with st.chat_message("user"):
        st.write(prompt_user)


if st.session_state.mensagem[-1]["role"] == "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Carregando.."):
            ai_response = llm_chain.predict(question=prompt_user)
            st.write(ai_response)
    new_ai_message = {"role": "assistent", "content": ai_response}
    st.session_state.mensagem.append(new_ai_message)

try:
    ai_response = llm_chain.predict(question=prompt_user)
    st.write(ai_response)
except Exception as e:
        st.error(f"Erro ao prever resposta da IA: {e}")
