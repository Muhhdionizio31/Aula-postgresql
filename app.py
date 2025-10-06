import streamlit as st
from crud import criar_alunos, listar_alunos, atualizar_idade, deletar_aluno

st.set_page_config(page_title="Gerenciamento de Alunos", page_icon="👨‍🎓👩‍🎓")

st.title("Sistema de alunos com PostgreSQL")

menu = st.sidebar.selectbox("Menu", ["Inserir", "Listar", "Atualizar", "Deletar"])

if menu == "Inserir":
    st.subheader("➕ Inserir Alunos")
    nome = st.text_input("Nome", placeholder="Seu Nome")
    idade = st.number_input("Idade", min_value=16, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            criar_alunos(nome, idade)
            st.success(f"Aluno {nome} inserido com sucesso!")
        else:
            st.warning("O campo nome não pode estar vazio")