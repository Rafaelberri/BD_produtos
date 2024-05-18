import sqlite3

def conectar(nome_banco):
    return sqlite3.connect(nome_banco)

def criar_banco(nome_banco):
    try:
        conn = conectar(nome_banco)
        print(f'Banco de dados {nome_banco} criado com sucesso ou já existe.')
        return conn
    except Exception as e:
        print(f'Erro ao criar o banco de dados: {e}')
        return None
