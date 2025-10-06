from db import conectar

def criar_alunos(nome, idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome, idade) VALUES (%s, %s)",
                (nome, idade)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erroa ao criar aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()

def listar_alunos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("SELECT * FROM alunos ORDER BY id")
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao tentar listar alunos: {erro}")
        return None, None
