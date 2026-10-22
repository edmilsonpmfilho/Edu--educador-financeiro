import streamlit as st
from data import carregar_dados, montar_contexto
from modelo import perguntar

# 1. Configuração inicial da página Streamlit
st.set_page_config(page_title="Edu - Educador Financeiro", page_icon="💰")
st.title("💰 Edu, seu Educador Financeiro")

# 2. Carregar dados e criar contexto (executa uma vez)
@st.cache_data
def inicializar_contexto():
    perfil, transacoes, historico, produtos = carregar_dados()
    return montar_contexto(perfil, transacoes, historico, produtos)

contexto_cliente = inicializar_contexto()

# 3. Histórico de chat do Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores na tela
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Campo de entrada do usuário
if prompt := st.chat_input("Como posso te ajudar com suas finanças hoje?"):
    # Mostra a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Busca a resposta do Edu usando o serviço de IA
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            resposta = perguntar(prompt, contexto_cliente)
            st.markdown(resposta)
            
    st.session_state.messages.append({"role": "assistant", "content": resposta})