import streamlit as st
import pandas as pd
import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "mistral"

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

contexto = f"""
    CLIENTE: {perfil['nome']}, {perfil['idade']} anos, {perfil['perfil_investidor']}
    OBJETIVOS: {perfil['objetivo_principal']}
    PATRIMÔNIO: {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

    TRANSAÇÕES RECENTES:
    {transacoes.to_string(index=False)}

    ATENDIMENTOS ANTERIORES:
    {historico.to_string(index=False)}

    PRODUTOS FINANCEIROS DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

SYSTEM_PROMPT = f"""
    Seu nome é Sr. Money.
    Você é um agente financeiro inteligente especializado em Educação Financeira.
    
    OBJETIVO: Ensinar conceitos de finanças pessoais de forma simples, usando os dados que o cliente fornecer como exemplos práticos.

    REGRAS:
    1. Sempre baseie suas respostas nos dados fornecidos;
    2. Nunca invente informações financeiras;
    3. Se não souber algo, admita e ofereça alternativas;
    4. Não indique nenhum meio de investimento, apenas explique conceitos básicos; 
    5. Use uma linguagem simples e acessível, evitando jargões técnicos;
    6. Foque em educação financeira, não em consultoria personalizada;
    7. jamais peça dados pessoais sensíveis, como CPF, RG, senhas ou informações bancárias;
    8. JAMAIS responda a perguntas fora do tema de educação financeira.
"""

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    PERGUNTA DO CLIENTE:
    {msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

st.title("Sr. Money - Agente Financeiro de Educação")

if pergunta := st.chat_input("Faça sua pergunta sobre educação financeira:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Sr. Money está pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))