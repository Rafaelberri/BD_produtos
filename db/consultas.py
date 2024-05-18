def listar_tabelas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()
    cursor.close()
    return [t[0] for t in tabelas]

def consultar_dados(conn, nome_tabela):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {nome_tabela}')
    dados = cursor.fetchall()
    cursor.close()
    return dados
