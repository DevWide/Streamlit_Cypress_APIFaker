import streamlit as st
from faker import Faker

# Configuração da página
st.set_page_config(page_title="PoC Sistema de Login", page_icon="🔒")

# Função para gerar dados falsos
def generate_fake_data():
    fake = Faker()
    return {"username": fake.user_name(), "password": fake.password()}

# Função para autenticação
def authenticate(username, password, fake_data):
    # Aceita qualquer combinação de login e senha durante os testes
    # Em uma aplicação real, você usaria uma lógica segura de autenticação aqui
    return True

# Título da aplicação
st.title("Sistema de Login PoC")

# Geração de dados falsos
fake_data = generate_fake_data()

# Formulário de login
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")
login_button = st.button("Login")

# Lógica de autenticação
if login_button:
    if authenticate(username, password, fake_data):
        st.success("Login bem-sucedido!")
    else:
        st.error("Usuário ou senha incorretos.")
