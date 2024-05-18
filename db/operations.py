def criar_tabela(conn, nome_tabela, colunas):
    cursor = conn.cursor()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas})')
    conn.commit()
    cursor.close()

def inserir_dado(conn, nome_tabela, colunas, valores):
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {nome_tabela} ({colunas}) VALUES ({valores})')
    conn.commit()
    cursor.close()

def atualizar_dado(conn, nome_tabela, set_clause, where_clause):
    cursor = conn.cursor()
    cursor.execute(f'UPDATE {nome_tabela} SET {set_clause} WHERE {where_clause}')
    conn.commit()
    cursor.close()

def excluir_dado(conn, nome_tabela, where_clause):
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {nome_tabela} WHERE {where_clause}')
    conn.commit()
    cursor.close()
