import streamlit as st
from crud import criar_alunos, listar_alunos, atualizar_idade, deletar_aluno

st.set_page_config(page_title="Gerenciamento de Alunos", page_icon="👨‍🎓👩‍🎓")

st.title("Sistema de alunos com PostgreSQL")

menu = st.sidebar.selectbox("Menu", ["Inserir", "Listar", "Atualizar", "Deletar"])

if menu == "Inserir":
    st.subheader("➕ Inserir Alunos")
    alunos = listar_alunos()
    nome = st.text_input("Nome", placeholder="Seu Nome")
    idade = st.number_input("Idade", min_value=16, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            criar_alunos(nome, idade)
            if idade == "16":
                st.success(f"{alunos} Cadastrado com sucesso ✔")
            else:
                st.warning("Tem que ter acima de 16 anos")
        else:
            st.warning("O campo nome não pode estar vazio")

elif menu == "Listar":
    st.subheader("📝👨‍🎓Listar Alunos")
    alunos = listar_alunos()
    if alunos:
        st.dataframe(alunos)
    else:
        st.info("❌Nenhum aluno encontrado. ")

elif menu == "Atualizar":
    st.subheader ("Atualizar Aluno")
    alunos = listar_alunos()
    if alunos:
        id_alunos = st.selectbox("Escolha o id do aluno para atualizar", 
            [linha[0] for linha in alunos]
            )
        nova_idade = st.number_input("Nova Idade", min_value=16)
        if st.button("Atualizar"):
            atualizar_idade(id_alunos, nova_idade)
            if nova_idade == "16":
                st.success(f"Atualizado com sucesso ✔")
            else:
                st.warning("Tem que ter acima de 16 anos")
    else:
        st.info("❌Nenhum aluno disponivel para atualizar")

elif menu == "Deletar":
    st.subheader("❌🧧Deletar Aluno")
    alunos = listar_alunos()
    if alunos:
        id_alunos = st.selectbox("Escolha o id do aluno para deletar", 
        [linha[0] for linha in alunos]
        )
        if st.button("Deletar"):
            deletar_aluno(id_alunos)
            st.success(f"Deletado com sucesso ✔")
    else:
        st.info("❌Nenhum aluno disponivel para deletar")